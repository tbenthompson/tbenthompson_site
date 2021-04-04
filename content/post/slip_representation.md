+++
title="Maybe we should stop using constant slip elements for fault modeling."
date=2021-03-31
draft=true
+++

## Slip discretization

Everything here was discussing the surface representation and not the slip function representation. But, slip function representation is important too! For example, using constant basis function slip elements causes many of these same problems. Two adjacent elements with different slip values will have a step function in slip at their junction. And that will produce a stress singularity. That's bad!

Furthermore, constant slip implies constant displacement along the element, which implies that the displacement derivative in the element parallel direction will be zero. And zero displacement derivative leads through to an inability to model surface parallel stresses. That's bad!

So, if you want to evaluate displacement *on* the fault, If you're evaluating displacements and stresses away from the fault by, for example, evaluating them on the free surface from a dislocation model, constant 
