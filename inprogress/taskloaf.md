Distributed computing is a big complex problem. Let's focus on the kind of parallelism done by big data and high performance computing. Normally, we want to coordinate several nodes to compute some set of quantities. Common solutions are MPI and Hadoop/Spark.

What do we do in computing? Broadly speaking, we apply operations to data. Task based parallelism takes this definition and uses it to create a very general tool for parallel computing. Klin taskloaf there are two primitives: tasks and data. Data can be anything you want it to be so long as you provide a method to serialize it to bytes. Tasks can perform any operation they want to.

Other tools have worked towards the same goal. However, none have achieved the generality and efficiency of taskloaf. Spark is a popular in memory map reduce engine used in industry big data applications. It also takes a tasks based approach. However, Spark operates from a coarse grained map reduce perspective from the beginning. That means that it has difficulty with parallel talk graphs that a aren't do flat and simple. Recursion, for example, is very hard in Spark. Furthermore, the task graph must be known ahead of time at least at a fine grained level. Tasks cannot generate new tasks.

There are several shared memory task based parallelism tools: StarPU, Quark, QuickSched.

Legion is another distributed task based parallelism toolkit. Legion has successfully demonstrated a substantial increase in speed for an 8000+ node chemistry problem. My goals differ from legion. I want a small

Taskloaf is a framework for executing complex graphs of computational tasks over a distributed network.

task-based parallelism is
