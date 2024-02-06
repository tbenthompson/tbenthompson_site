+++
title="Fluent dreaming for language models (AI interpretability method)"
date=2024-02-06
+++

My coworkers at Confirm Labs and I recently posted a paper on fluent dreaming for language models! [arXiv link.](https://arxiv.org/abs/2402.01702) 
We have a [companion page here demonstrating the code](https://confirmlabs.org/posts/dreamy.html). We also have [a demo Colab notebook here](https://colab.research.google.com/drive/1B0dM7du91BUkT7tSICXjKL7lrBAEdSa-?usp=sharing).

Dreaming, aka "feature visualization," is a interpretability approach popularized by DeepDream that involves optimizing the input of a neural network to maximize an internal feature like a neuron's activation. We adapt dreaming to language models.

Past dreaming work almost exclusively works with vision models because the inputs are continuous and easily optimized. Language model inputs are discrete and hard to optimize. To solve this issue, we adapted techniques from the adversarial attacks literature (GCG, [Zou et al 2023](https://arxiv.org/abs/2307.15043)). Our algorithm, Evolutionary Prompt Optimization (EPO), optimizes over a Pareto frontier of activation and fluency:

![](/images/dreaming_pareto.png "Points and prompt text on the Pareto frontier for a single dreaming run.")

In the paper, we compare dreaming with max-activating dataset examples, demonstrating that dreaming achieves higher activations and similar perplexities to the training set. Dreaming is especially exciting because some mildly out-of-distribution prompts can reveal details of a circuit. For example, Pythia-12B layer 10, neuron 5 responds very strongly to "f. example", "f.ex." and "i.e" but responds even more strongly to "example f.ie.", a phrase the model has probably never seen in training.

![Figure: Comparing activation and cross-entropy between dreaming outputs and the top 64 max-activating dataset examples from 500 million tokens of the Pile. Lower cross-entropy prompts are more fluent. The black line is schematically separating regions of the plot that are empirically inside and outside the training distribution.](/images/dreaming_scatterplot.png "Scatterplot of activations and cross-entropy from dreaming and max-activating dataset examples.")

Like max-activating dataset examples, language model dreams will be hard to interpret in the face of polysemanticity. We would be excited about applying dreaming to more monosemantic feature sets resulting from dictionary learning/sparse autoencoders.

We also think algorithms like EPO will also be useful for fluent algorithmic redteaming. We are working on that now!