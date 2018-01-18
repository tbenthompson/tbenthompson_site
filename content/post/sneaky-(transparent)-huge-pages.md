---
{
  "slug": "sneaky-(transparent)-huge-pages",
  "date": "2018-01-17",
  "subtitle": "Generic subtitle",
  "title": "Sneaky (transparent) huge pages"
}
---
<!--more-->

A week ago, I spent an afternoon on a run in with a sneaky feature of the Linux kernel that made some sparse matrix vector product operations about twice as slow as I expected. 

I've recently learned about using file backed shared memory with mmap to do efficient interprocess communication. At the most basic level, you share data between two processes by writing that data to a file. The file can be made to look a lot like a normal region of memory using `mmap`, a system call, and can be shared between multiple processes by giving `mmap` the `MAP_SHARED` flag. There's a downside though, in that the data has to synced to the hard drive continuously. So, instead of sharing a file that is written to disk, I discovered that you can share a file on a RAM disk -- just a filesystem that is backed by RAM. On Linux, a large `tmpfs` RAM disk filesystem is often mounted by default at `/dev/shm`. 

Here's some python that creates a NumPy array with `mmap`. First, let's get set up...


```python
import os
import mmap
n = int(5e7)
nb = 8 * n
filename = '/dev/shm/abc'
```

Next, we need to make sure that the file is the correct size using `ftruncate`. Finally, we memory map it into a numpy array. `np.frombuffer` is a handy function when you already have a memory buffer and just want to "view" it as a numpy array without copying the memory.


```python
with open(filename, 'w+b') as f:
    os.ftruncate(f.fileno(), nb)
    mem = mmap.mmap(f.fileno(), nb)

x = np.frombuffer(mem, dtype = np.float64)
```

And for kicks, we'll stick some random numbers in there...


```python
x[:] = np.random.rand(n)
x
```

    array([ 0.84984349,  0.5928336 ,  0.34455741, ...,  0.45909949,  0.51389915,  0.36287542])



Looks like everything is working! Right? Okay, so now I'm going to create another array of the same size with random indexes into the first array.


```python
idx = np.random.randint(0, n, n)
```

And then, benchmark an indexing operation on `x`.


```python
%timeit y = x[idx]
```

    1.39 s ± 92.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


So, this is where it gets really interesting... What if we copy `x` and then do the benchmark again?


```python
x2 = x.copy()
%timeit y = x2[idx]
```

    691 ms ± 117 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


When I finally tracked down this performance bug, I was astonished. Why would copying an array make an indexing operation run almost twice as fast?! At first, I did a whole lot of mind-blown I-dont-undestand-this googling including lots of hopelessly nondescript attempts like "numpy copy speed up" or "copy speeds up indexing operation". 

Eventually, I tried to think it through. If copying an array makes an operation faster, then by implication, not all memory is made equal. Some memory is faster to access or manipulate than other memory. I was already aware of NUMA (non-uniform memory access), a feature of multi-socket servers that means that cores can access certain chunks of memory several times faster than other "further" chunks. Maybe `mmap` is less likely to allocate memory close to the core that needs it, thus causing NUMA issues? But, this copy-speeds-everything-up behavior happens on my laptop, so it can't be a NUMA issue. 

I thought the key must be in way I've created this particular chunk of memory. It's is a bit out of the ordinary to be using mmap. Again, I tried searching all sorts of vague things about "mmap memory slower" or "mmap performance", thinking that maybe something in the way mmap synchronizes to the RAM disk was causing the performance problems. Alas, no one on the internet seemed to be having these problems! At a loss, I just started fiddling around with the mmap flags to see if different options fixed the problem and I discovered a key clue.

Using `mmap` with the `MAP_PRIVATE` flag boosted performance of the indexing operation to the same speed as when I copied `x`. 

Around the same point, I had another thought. The current indexes are random. Random indexing of a 50 million element array is bound to cause some caching problems. Does copying speed up a sequential indexing operation? Say, we just skip every other element. Let's try it!


```python
idx_seq = np.arange(0, n, 2)
```

```python
%timeit y = x[idx_seq]
```

    62.8 ms ± 2.07 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)



```python
%timeit y = x2[idx_seq]
```

    62.1 ms ± 1.47 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)


First off, sequential indexing is much faster because it has much better cache utilization (actually, pretty much ideal cache utilization). I mean it's just a copying operation! This is going to be a memory bandwidth bound operation, so let's calculate really quickly what type of memory bandwidth my little laptop is achieving.


```python
t_sec = 0.0621
total_bytes = x2.nbytes + idx_linear.nbytes + y.nbytes
print(str(total_bytes / t_sec / 1e9), 'GB/s')
```

    12.882447665056361 GB/s


Wow! I'm pretty sure that's close to the peak memory bandwidth possible from this laptop.

Secondly, the linear memory access is just as fast for the `mmap`-ed memory as it is for the memory obtained by `x.copy()` (presumably deep inside numpy there's a `malloc` call). So, while it's straightforward to say that a random memory access pattern is much slower than a sequential access pattern, there's still the problem of what would make random access slower on some blocks of memory than others. Now, I had something more concrete to start googling... "mmap slow random memory access". And, finally, the first result was my [salvation from stack overflow](https://stackoverflow.com/questions/44001260/random-mmaped-memory-access-up-to-16-slower-than-heap-data-access/44152743).

The random memory access on the `mmap`-ed memory was slower because each access had to not only load the memory all the way from RAM rather than cache, but also had to load the physical location of that virtual memory from RAM rather than cache. This is because `mmap`-ed shared memory defaults to using traditional 4kB memory pages while, for most recent Linux installation, `malloc` default to using 2MB huge pages. The 4kB pages result in far more TLB (translation lookaside buffer) cache misses. Our 400MB chunk of memory would requires 100,000 page table entries with 4kb pages -- way more than fit in the TLB cache.  

There was a whole bunch of jargon I didn't define in that last paragraph. Maybe in a future post, I'll go through the details of how virtual memory, the TLB, Huge Pages and Transparent Huge Pages all work. This [page](https://dzone.com/articles/memory-access-patterns-are) has some comprehensive descriptions. but just to finish this post out, I'll show some performance counters demonstrating the TLB cache miss problem. The first example is using 4kB pages, while the second is using 2MB huge pages. There are 200x fewer TLB cache misses using huge pages.

```

➜  examples git:(master) ✗ perf stat -e dTLB-load-misses python mmap_bench.py shmem 1
shm square 0.4846489429473877

 Performance counter stats for 'python mmap_bench.py shmem 1':

        19,313,497      dTLB-load-misses                                            

       1.159249907 seconds time elapsed

➜  examples git:(master) ✗ perf stat -e dTLB-load-misses python mmap_bench.py shmemhuge 1
shm square 0.2850306034088135

 Performance counter stats for 'python mmap_bench.py shmemhuge 1':

            91,545      dTLB-load-misses                                            

       0.895894488 seconds time elapsed
```

And let's check our original problem by using a separate `hugetlbfs` RAM disk using huge pages mounted at `/mnt/hugepages` (remember before we used `/dev/shm`).


```python
filename = '/mnt/hugepages/abc'
page_size = 2.0 ** 21
# Using huge pages requires using a number bytes that is an exact multiply of the page size
nb_rounded_to_page_size = int(page_size * np.ceil(nb / page_size))
with open(filename, 'w+b') as f:
    os.ftruncate(f.fileno(), nb_rounded_to_page_size)
    mem = mmap.mmap(f.fileno(), nb_rounded_to_page_size)
x = np.frombuffer(mem, dtype = np.float64)
%timeit y = x[idx]
```

    657 ms ± 39.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


Hurray! Success!


