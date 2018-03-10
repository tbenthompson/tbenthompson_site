# Notes:
# -- multiprocessing + jupyter is tough because of the way pickling functions works
# -- need to be really careful benchmarking because of start up time!
# -- RawArray vs. Array, Array has a lock!
# -- frombuffer doesn't touch the array, O(1) operation, in C, just grabbing a pointer, wraps existing pointer!
# -- core affinity is really important!
# -- 0.3 seconds is pretty good --> implies 13 GB/sec
# -- shmem confounds because it is 4kb page size!

import os
import subprocess
import time
import multiprocessing as mp
import numpy as np

max_cores = 80
max_n = max_cores * int(2e6)

a = mp.RawArray('d', max_n)
b = mp.RawArray('d', max_n)
c = mp.RawArray('d', max_n)

np_a = np.frombuffer(a)
np_b = np.frombuffer(b)
np_c = np.frombuffer(c)
 
np_a[:] = np.random.rand(max_n)
np_b[:] = np.random.rand(max_n)

local_a = [0]
local_b = [0]
local_c = [0]

def start_end(args):
    idx, n, n_cores = args
    n_per_core = n // n_cores
    start = idx * n_per_core
    end = start + n_per_core
    return start, end

def identity(i):
    return i

def shmem_add(args):
    start, end = start_end(args)
    np.add(np_a[start:end], np_b[start:end], out = np_c[start:end])

def predist_add(args):
    start, end = start_end(args)
    local_a[0] = np_a[start:end].copy()
    local_b[0] = np_b[start:end].copy()
    local_c[0] = np_c[start:end].copy()
    np.add(local_a[0], local_b[0], local_c[0])
    
def setup_proc(max_identity, n, n_cores, copy):
    which_core = mp.current_process()._identity[0] - 1 - max_identity
    subprocess.run(
        ['taskset', '-p', '-c', str(which_core), str(os.getpid())], 
        stdout = subprocess.PIPE
    )
    start, end = start_end([which_core, n, n_cores])
    if copy:
        pass
        #local_a[0] = np_a[start:end].copy()
        #local_b[0] = np_b[start:end].copy()
        #local_c[0] = np_c[start:end].copy()

max_identity = 0

def bench(n, n_cores, name):
    global max_identity
    
    copy = True if name is 'predist' else False
    fnc = predist_add if name is 'predist' else shmem_add
    
    assert(n <= max_n)
    assert(n % n_cores == 0)
    
    pool = mp.Pool(
        n_cores, 
        initializer = setup_proc, 
        initargs = (max_identity, n, n_cores, copy)
    )
    max_identity += n_cores
    args = [(i, n, n_cores) for i in range(n_cores)]
    start = time.time()
    pool.map(identity, list(range(n_cores)))
    print('time to init', time.time() - start)
    
    start = time.time()
    result = pool.map(fnc, args)
    took = time.time() - start
    
    #np.testing.assert_almost_equal(np_c[:n], np_a[:n] + np_b[:n])
    return took

for nc in [1,2,4,8,10,20,40,80]:
    print(nc, 'shmem', bench(max_n, nc, 'shmem'))
    print(nc, 'predist', bench(max_n, nc, 'predist'))