+++
title="Why we need another task parallelism library?"
date=2018-01-19
+++
Over the last couple years, I've been working on and off on a task-based parallelism library called [taskloaf](https://github.com/tbenthompson/taskloaf). This raises the question: why? There are already several different library and frameworks and languages out there that aim to tackle the same question of how to easily and efficiently spread work over a parallel system. There are two answers to that question. The first and initial reason was that I find the subject really interesting and developing a library has been an incredible way to learn about a whole range of programming and computer science subjects (optimization, distributed algorithms, databases, continue this list...) 

One thing I worry about when I invest a lot of time into a software project is whether I'm simply re-inventing the wheel and am either missing or misunderstanding existing libraries.

But, as I dug into the subject, I've found several areas where I suspect existing tools are deficient. The rest of this post will describe the issues I've run into with existing tools and how taskloaf attempts to solve those issues. 

Comparable python-based tools:

* Spark 
* Celery
* Dask
* Ray

Taskloaf is aimed at being a bare bones sort of task parallelism middleware. No scheduling fanciness is done (e.g. work stealing), but implementing such a thing would be simple to do.

Compared to Spark:

* taskloaf has built in support for shared memory and zero-copy (de)serialization
* taskloaf has a fully distributed design with no centralized scheduler.
* taskloaf supports asynchronous coroutine tasks (tasks that can wait on other tasks)
* taskloaf support MPI as a communications backend

Compared to dask:

Why is a manual task scheduler the core 

explain why openmp doesn't solve the shared memory problem
explain why other tools don't solve the shared memory parallelization problem
explain why a simple manual task scheduler is the core problem

-- Spark/mapreduce
-- joblib
-- dask (AWESOME)
-- celery
-- Ray (has some similarities with dask): The taskloaf shared memory zero-copy load approach has a lot of similarities with Plasma, a shared memory service that is part of Ray. However, it differs in that the plan is to have isolated local memory stores for each core. A given core is the only one that is allowed to allocate or de-allocate in that respective region. This will eliminate a lot of the slow NUMA accesses and remove the necessity for a lot of locking. In particular, there won't be a separate thread managing the memory. Cooperative multi-tasking!


features:
------------
async design
zero-copy serialization (arrow)
shared memory
shared-nothing internals
no centralized scheduler
MPI (vs dask/ray/spark)
???

