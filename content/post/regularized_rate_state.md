+++
title="Regularizing rate and state friction for numerical simulation"
date=2018-03-19
+++

The standard form for rate and state friction produces undefined results for $V = 0$. Some algebra and calculus and microphysics lead to the commonly used regularized form that is still valid at $V=0$. This is based on the presentation in Rice and Ben-Zion 1996 and Lapusta et. al 2000. There's nothing novel here, but the details of this sort of thing are often glossed over in the literature. So, while working it out for myself, I figured I'd write it up!

Let's start with the common, empirically-derived rate and state friction with the aging law for state evolution.

\begin{equation}
\tau = \sigma_n (f_0 + a \log(V/V_0) + b \log(V_0\theta/D_c))
\label{rsorig}
\end{equation}

\begin{equation}
\dot{\theta} = 1 - V\theta / D_c
\label{agingorig}
\end{equation}

First, I'll transform to use a somewhat different state variable. $\theta$ is hard to intuitively understand, while $\Psi$ is much more intuitive -- it's just the current absolute offset of the friction coefficient.

\begin{equation}
\Psi = f_0 + b \log(V_0\theta/D_c)
\label{transform}
\end{equation}

or, for the inverse transformation:

\begin{equation}
\theta = \frac{D_c}{V_0}\exp(\frac{\Psi - f_0}{b})
\label{invtransform}
\end{equation}

With this transformation, $\ref{rsorig}$ becomes:

\begin{equation}
\tau = \sigma_n (\Psi + a \log(V/V_0))
\label{rstransform}
\end{equation}

For me, this is nicer in that I can understand the new "state" parameter, $\Psi$, as the current strength of friction when $V = V_0$.

Now, I'll get the aging law in terms of $\Psi$.  Differentiating \ref{transform}:

\begin{equation}
\dot{\Psi} = b \dot{\theta}/\theta
\end{equation}

and plugging in for $\dot{\theta}$ from \ref{agingorig}:

\begin{equation}
\dot{\Psi} = b/\theta - bV / D_c
\end{equation}

Finally, plug in for $\theta$ from \ref{invtransform}, I get the aging law in terms of $\Psi$.

\begin{equation}
\dot{\Psi} = \frac{bV_0}{D_c}(\exp(\frac{f_0 - \Psi}{b}) - \frac{V}{V_0})
\label{aging01}
\end{equation}

With that done, the second step is to actually do the regularization at $V=0$. Solving $\ref{rstransform}$ for $V$:

\begin{equation}
V = V_0 \exp(\frac{\tau}{a\sigma_n})\exp(-\frac{\Psi}{a})
\end{equation}

The trouble here is that the $\exp(\frac{\tau}{a\sigma_n})$ term can never be 0 and as a result $V=0$ is impossible. Quoting Lapusta et. al 2000:

>A drawback of the logarithmic form (28a) is that the stress is not defined for V = 0. The logarithmic form was derived from purely empirical considerations to match experimental observations (Dieterich, 1979, 1981; Ruina, 1983). However, it has a theoretical basis, in that such a form would result if the direct velocity effect is due to stress biasing of the activation energy in an Arrhenius rate process at contact junctions, at least in the range for which forward microscopic jumps, in the direction of shear stress, are overwhelmingly more frequent than backward jumps.

So, the $\exp(\frac{\tau}{a\sigma_n})$ term represents the frequency of forward microscopic jumps. What about backward microscopic jumps? They happen too, especially near $V=0$. That suggests adding another term like $-\exp(\frac{-\tau}{a\sigma_n})$ to represent backward microscopic jumps:

\begin{equation}
V = V_0 (\exp(\frac{\tau}{a\sigma_n}) - \exp(\frac{-\tau}{a\sigma_n}))\exp(-\frac{\Psi}{a}) = 2 V_0 \sinh(\frac{\tau}{a\sigma_n})\exp(-\frac{\Psi}{a})
\end{equation}

Solving for $\tau$ and I get the regularized rate-state friction system:

\begin{equation}
\tau = \sigma_n a \sinh^{-1}(\frac{V}{2V_0}\exp(\Psi/a))
\label{rsreg}
\end{equation}

\begin{equation}
\dot{\Psi} = \frac{bV_0}{D_c}(\exp(\frac{f_0 - \Psi}{b}) - \frac{V}{V_0})
\label{aging01-2}
\end{equation}

In my numerical quasidynamic models, I am using equations \ref{rsreg} and \ref{aging01-2}, rather than the more traditional \ref{rsorig} and \ref{agingorig}. Most other rate and state friction implementations (both fully dynamic and quasidynamic) that I have read about also use the regularized forms.
