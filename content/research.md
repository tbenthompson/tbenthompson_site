+++
title = "Research"
weight = 1
menu = "main"
type = "top"
+++

### Crustal stress estimation in the Himalayan wedge
Quantitative estimates of crustal stress magnitude and orientation are hard to come by. On the other hand, geodesy is providing an increasingly accurate picture of global tectonic motions. Field and laboratory analyses contribute fault slip rates and exhumation rates. Seismology yields estimates of stress from moment tensor analyses. I am working to combine these data sources with geometrically accurate elastic boundary element models to estimate the crustal stress field and the driving forces behind those stresses -- for example, mantle tractions on the base of the crust. 

Currently, I am applying these methods to the Himalayan wedge in the vicinity of the 2015 Nepal earthquake. In the past, Coulomb wedge and elastic wedge models provided a qualitative picture of these stresses and the growth of mountain belts over long time scales. My work will make these models quantitative by constraining geometrically realistic wedge models with geodetic and geologic observations. An improved image of the stress in the crust will help answer several questions about active tectonics in the Himalayas. Are stress drops low or high compared to total stress? Is it reasonable that some stress in the Himalayas might be released as plastic strain rather than fault slip? What fault slip rates and directions are consistent with different hypotheses concerning the tectonic driving forces?

![HRF principal stresses](/images/hrf_principal_stresses.png)
*Principal stress orientations in a cross section of the Himalayan wedge including a frictional detachment and one internal MCT-like fault.* 

### Longmen Shan fault geometry and slip rates

*[GRL article](http://onlinelibrary.wiley.com/doi/10.1002/2014GL062833/abstract).*

The Longmen Shan is the steepest topographic front at the India‐Asia collision zone and the site of the Mw 7.9 Wenchuan earthquake. To explain the interseismic GPS velocities across the greater Longmen Shan region, we developed a boundary element model including earthquake cycle effects, topography, the westward dipping Beichuan Fault and a ∼20 km deep, shallowly dipping, detachment, inferred from observed afterslip and from structural considerations. Prior analyses which had neglected the detachment and earthquake cycle effects found shortening rates near zero. In contrast, we found that interseismic GPS data are consistent with a shortening rate of 5.7±1.5mm/yr and maximum surface slip‐deficit rate of 9.5±2.5mm/yr. This model unifies the interpretation of geodetic deformation throughout the earthquake cycle and suggests that the Longmen Shan is an active fold‐and‐thrust belt with Wenchuan‐like recurrence intervals as short as 600 years. 

<img src="/images/longmenshan.png" />
*A cross section of the Longmen Shan showing model-predicted velocities. Positive velocity is to the right/southwest.*

### Powerful and efficient boundary element software
Our tectonic and earthquake cycle research is supported by development of elastic boundary element software. This has required investigations into the best approaches for a wide range of computational and mathematical tasks: singular integration of Green's functions, approximation of farfield Green's function interactions with the fast multipole method, flexible treatment of equality and inequality constraints, and a big dose of computational geometry. These are a just a few of the components of this effort. This new software will be able to model arbitrary geometries including surface topography, complex data-derived fault geometries, and material boundaries. Models with millions of elements will be possible in two or three dimensions. Exciting!

<img src="/images/matrix.png" style="width: 400px;"/>

*A visualization of the structure in a boundary element matrix with rotational symmetry.*

### Taskloaf: Dynamic distributed task parallelism 

*[Taskloaf GitHub page](https://github.com/tbenthompson/taskloaf)*

Task-based parallelism enables running complex parallel computations by describing them as a graph of tasks. Shared memory task-based parallelism has become an important tool as demonstrated by tools like Intel TBB, Cilk, and OpenMP v3. But, distributed memory task-based parallelism systems is still heavily researched to determine the most usable, efficient and scalable approach. Instead of waiting for the future holy grail of distributed task parallelism, I designed Taskloaf while visiting Oak Ridge National Lab in Fall 2015. Taskloaf is a minimal but reasonably efficient and scalable task parallelism library. A primary goal with the library was to keep it small and easy to maintain. The codebase has less than 2k lines of code so that a skilled C++ programmer can learn the inner workings of the entire library in a day. The interface is based around [futures](https://en.wikipedia.org/wiki/Futures_and_promises), a time-tested parallelism primitive. I use Taskloaf to parallelize my boundary element software.
