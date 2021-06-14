+++
title="Maybe we should stop using planar triangles for fault modeling"
date=2021-03-31
+++

Let's consider a model problem where the goal is to calculate the stress on a fault due to some slip on that fault. We also include a topographic free surface. How should we model this surface? 

Should we use planar triangles to model a curved fault? What happens at the junction between two triangles? If we do the natural fault thing and require the slip to be tangential to the suface, the slip vector has a step function at the junction between the two triangles. This must be true because the two triangles have different normal vectors and tangent vectors. On the other hand, if we force slip to be continuous across triangles, we have to allow non-tangential slip because at an edge where two triangles meet the slip vector has to be identical but the tangent vectors are different. 

That means that we're stuck between a rock and a hard place and have to choose: 
* non-tangential, but continuous slip
* tangential, but discontinuous slip. 

So, planar triangles probably aren't a sustainable or "correct" way to represent a fault surface unless that surface is perfectly planar or we're zoomed in far enough that the underlying microscale behavior is relevant. Fundamentally the problem is that our fault surface representation is $C^0$, meaning that the function itself is continuous but the derivatives are not. This problem propagates through the whole model up in other ways too. Suppose you choose to have discontinuous, but tangential, slip. Then, there will be stress singularities at every element junction! 

Should we use a smoother fault surface representation? Probably. A $C^1$ fault representation where the normal vector is continuous between adjacent elements solves the problem described in the previous paragraph. 

Let's back up and consider how to mesh our model earthquake problem from the perspective of *truth*, *accuracy* and *robustness*:

**Truth**: The underlying true surface of the Earth is fractal and has sharp corners at basically any zoom level. The fault surfaces are probably similarly fractal and non-smooth.

**Accuracy**: There is accurate satellite data on the location of the Earth's surface down to about a a few meters resolution. And for faults, depending on where in the world, the uncertainty in fault location is on the order of 10-10000m. So, only a few digits of accuracy could possibly be relevant in these models since there's already a high level of error introduced by the mere location uncertainty in the faults, much less all the other uncertainties that I haven't discussed here. The main goal, at least at this point in the evolution of the earthquake science field, is in terms of qualitative behavior and questions on the scale of 1-50% or even about the sign of an effect (positive or negative).

**Robustness**: This is where smoothness gets really important. From my experience, having smooth boundaries makes so much about integral equation methods simpler. Especially for these faulting/crack problems where hypersingular terms are common.

## A different approach

My tentative approach that I've been exploring is:

* Use at least a $C^1$ mesh. Even smoother surfaces should work fine too. An easy way to get a $C^1$ surface is to use cubic splines. Smooth surfaces make the numerics and code much easier because they remove several types of singularities. This is especially relevant because of the hypersingular integrals from faults that result in stress singularities I described above. 
* Methods for smooth surfaces tend to be developed by people looking for high-order accuracy. To reduce all forms of error, it makes sense to have accurate representations of both the surfaces involved and the functions defined on that surface. In addition, low order surface discretizations introduce singularities. For example, a boundary element method which is based on $C^0$ elements will have singularities in stress at each element intersection because there's an artificially introduced corner. I don't think the high-order accuracy is particularly important for quasi-static earthquake problems, but in my experience so far these high-order methods tend to work quite well even when the order $p$ is fairly small.
* Modifying non-smooth surfaces to be smooth makes a negligible difference in the model results, especially compared to the other uncertainties. And on the scale of a few meters left or right, there is no real reason to think that input geometries are perfectly correct. I think there's some potential for this point to be wrong in some circumstances. For example, if the small scale roughness is extremely important to the problem, or the purpose of the model is to study a sharp corner in a fault. But, in most situations, using smooth surfaces will be both acceptable and easier. If a corner truly is important, I can do some refinement so that the resulting singularity is sufficiently well resolved.

*Thanks to Andreas Klöckner, Brendan Meade and Andrew Bradley for discussions that led to this post. If you want to chat about these kind of topics, please [get in touch](mailto:t.ben.thompson@gmail.com)!*
