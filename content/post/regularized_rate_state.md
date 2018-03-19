+++
title="Regularizing rate and state friction for numerical simulation."
date=2018-03-19
+++

The standard form for rate and state friction produced undefined results for $V = 0$. Some algebra and calculus and microphysics lead to the commonly used regularized form that is still valid at $V=0$. This is based on the presentation in Rice and Ben-Zion 1996 and Lapusta et. al 2000. There's nothing novel here, but the details of this sort of thing are often glossed over in the literature. So, while working it out for myself, I figured I'd write it up!

Let's start with the common, empirically-derived rate and state friction with the aging law for state evolution.

$\tau = \sigma_n (f_0 + a \log(V/V_0) + b \log(V_0\theta/D_c)) \label{1}\tag{1}$

$\dot{\theta} = 1 - V\theta / D_c \label{2}\tag{2}$

First, I'll transform to use a somewhat different state variable. $\theta$ is hard to intuitively understand, while $\Psi$ is much more intuitive -- it's just the current absolute offset of the friction coefficient.  

$\Psi = f_0 + b \log(V_0\theta/D_c) \tag{3}$

or, for the inverse transformation:

$\theta = \frac{D_c}{V_0}\exp(\frac{\Psi - f_0}{b}) \label{4}\tag{4}$

Differentiating to get an evolution law:

$\dot{\Psi} = b \dot{\theta}/\theta \tag{5}$

and plugging in for $\dot{\theta}$ from \ref{2}:

$\dot{\Psi} = b/\theta - bV / D_c \tag{5}$

Finally, plug in for $\theta$ from \ref{4}, I get the aging law in terms of $\Psi$.

$\dot{\Psi} = \frac{bV_0}{D_c}(\exp(\frac{f_0 - \Psi}{b}) - \frac{V}{V_0}) \label{6}\tag{6}$

With that done, the second step is to actually do the regularization at $V=0$. Solving $\ref{1}$ for $V$:

$V = V_0 \exp(\frac{\tau}{a\sigma_n})\exp(-\frac{\Psi}{a}) \tag{7}$

The trouble here is that the $\exp(\frac{\tau}{a\sigma_n})$ term can never be 0 and as a result $V=0$ is impossible. Quoting Lapusta et. al 2000:

>A drawback of the logarithmic form (28a) is that the stress is not defined for V = 0. The logarithmic form was derived from purely empirical considerations to match experimental observations (Dieterich, 1979, 1981; Ruina, 1983). However, it has a theoretical basis, in that such a form would result if the direct velocity effect is due to stress biasing of the activation energy in an Arrhenius rate process at contact junctions, at least in the range for which forward microscopic jumps, in the direction of shear stress, are overwhelmingly more frequent than backward jumps.

So, the $\exp(\frac{\tau}{a\sigma_n})$ term represents the frequency of forward microscopic jumps. What about backward microscopic jumps? They happen too, especially near $V=0$. That suggests adding another term like $-\exp(\frac{-\tau}{a\sigma_n})$ to represent backward microscopic jumps:

$V = V_0 (\exp(\frac{\tau}{a\sigma_n}) - \exp(\frac{-\tau}{a\sigma_n}))\exp(-\frac{\Psi}{a}) \tag{8} = 2 V_0 \sinh(\frac{\tau}{a\sigma_n})\exp(-\frac{\Psi}{a})$

Solving for $\tau$ and we get the regularized rate-state friction equation:

$\tau = \sigma_n a \sinh^{-1}(\frac{V}{2V_0}\exp(\Psi/a)) \label{9}\tag{9}$

In my numerical quasidynamic models, I am using equations \ref{6} and \ref{9}, rather than the more traditional \ref{1} and \ref{2}.
