+++
when="2015-2017"
title="Simplified distributed task parallelism"
weight = 351
+++

Task-based parallelism enables running complex parallel computations by describing them as a graph of tasks. Shared memory task-based parallelism has become an important tool as demonstrated by tools like Intel TBB, Cilk, and OpenMP v3. But, distributed memory task-based parallelism systems is still heavily researched to determine the most usable, efficient and scalable approach. Instead of waiting for the future holy grail of distributed task parallelism, I designed Taskloaf while visiting Oak Ridge National Lab in Fall 2015. Taskloaf is a minimal but reasonably efficient and scalable task parallelism library. A primary goal with the library was to keep it small and easy to maintain. The codebase has less than 2k lines of code so that a skilled C++ programmer can learn the inner workings of the entire library in a day. The interface is based around [futures](https://en.wikipedia.org/wiki/Futures_and_promises), a time-tested parallelism primitive. I use Taskloaf to parallelize my boundary element software.
