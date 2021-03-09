+++
when="2015-2016"
title="Neural-net-accelerated viscoelastic calculations."
weight = 365
+++

<img src="/images/nn_grl.jpeg"/>

The viscous behavior of the deep Earth results in slow surface motion continuing for many years after an earthquake. However, computing the physics of this behavior can be extremely expensive involving multi-dimensional inverse Laplace transforms and slowly-convergent series. We developed a basic feedforward neural network that is able to replicate the results of the analytic computation while running ~500x faster. Since the analytic function being approximated is already known, this is a sort of strange application of neural networks in that they are very explicitly being used in their role as universal function approximators for a high-dimensional function. It works really well!
