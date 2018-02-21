+++
title="Automated testing for scientists and data analysts"
date=2018-02-07
+++

A lot of scientists and data analysts don't use automatic test suites for verifying their code. 
And I think that's because it's really hard.
Almost all the introductions to automated testing that I've seen come from a more typical software engineering perspective. They assume you already know exactly what the output of your code should be.
And the trouble with science is that that's rarely the case. 
I mean, if you knew the results ahead of time, you wouldn't be doing science! 

It's hard to square this situation with the consistent loud noises coming from the software development world (in my case, also from inside my head!) saying "It might be broken! Write tests! Write tests! Write tests!". "But, I can't!" 


I've been dealing with this battle for a few years now and feel like I've figured out some coping strategies.
The simplest solution is to just give up.
And for some types of science, I think that's the right thing to do.
Essentially, whether or not to test is a question of how important it is that the results are correct.
In that sense, I don't think automated testing makes sense for exploratory analysis.
But, for a reusable algorithm or production/final analysis, tests are invaluable.
My work flow mostly involves Python and C++. So, in my case, the question of whether something should be tested often goes hand in hand with whether I'm working in a Jupyter notebook or with a proper package. 

So, let's back up and ask: why should we have automated tests?

## Automated testing

Automated testing is valuable for ensuring that software does what is is supposed to do. Automated testing:

* reduces fear when making implementation or design changes (this is huge, in my opinion!) One perspective on when to write tests is to write tests whenever you feel afraid of making a change and to keep writing tests until your not afraid anymore.
* enables rapid refactoring without fear of breaking the code base
* gives instant feedback
* helps improve software accuracy, correctness
* provides a form of precise documentation

[A couple good discussions of why we should unit test.](https://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort)

I've also enjoyed the book "Working Effectively with Legacy Code" by Michael Feathers, because it focuses on adding tests to previously untested and maybe poorly designed "legacy" code (which he defines as any code without tests!).
[A summary of the book.](https://softwareengineering.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code)

But, returning to the original problem, automated testing can be very difficult in science and analytics because the true answer is not known. Sometimes low level functions can be assigned a "correct" result. But, for higher level constructs (e.g. an entire time series forecast or the solution of a complex PDE), it's normally much harder to determine what is right and wrong.  It requires careful input from the statistician/scientist/analyst to determine if something looks right or wrong and whether there's anything fishy going on.

So, given that we want to have automated tests, but the inherent nature of the problem makes most testing difficult, what do we do? I still struggle with this issue and am learning all the time, but I've found three types of approaches particularly useful: 

## Special cases

This first approach is the most common, the simplest, and often the most valuable. 
Suppose I'm writing a [general algorithm for numerically solving elastic partial differential equations for an arbitrary geometry and set of boundary conditions](https://github.com/tbenthompson/tectosaur). 
It might be really hard to say whether the answer I'm getting is correct for 
any given problem. But some specific problems have already been solved analytically. 
For example, a spherically symmetric problem is easily solved by hand and any number of textbooks 
have exact solutions. Or, similarly, the motion of the Earth due to an planar earthquake in an infinite flat Earth has [a well known solution](http://www.bosai.go.jp/study/application/dc3d/DC3Dhtml_E.html).

In some cases, there are very general approaches for building special cases. For example, anyone writing numerical methods for solving PDEs should absolutely learn about the [method of manufactured solutions](http://www.personal.psu.edu/jhm/ME540/lectures/VandV/MMS_summary.pdf), which lets you come up with as many arbitrary test problems as you need. 

Unfortunately, even if there are useful special cases, often the resulting tests only validate the program as a whole. What if that program involves thousands of lines of code? I'd prefer to be able to test smaller portions of the code base on their own.

## Property testing

I think property testing is the most useful approach when the answer isn't known. Instead of check the final answer, we check a *property* of some final or intermediate part of the calculation. For example:

* Newton's method for root finding should take exactly one step to solve any linear system of equations. So, a simple property test might be to generate 100 random linear systems and check that all of them are solved in one step. The difference from a special case is that we have a simple algorithm for generating many special cases.
* In the case of a finite element or boundary element model, the solution should converge with increasing mesh density.
* Running an idempotent function 100 times should leave the system in the same state as running it once.
* With an infinite penalty, ridge and lasso regressions return all zeros. With a penalty of zero, ridge and lasso regressions return the same answer as unregularized least squares.

I've always written property tests by hand, but there are some libraries that attempt to automate part of the process. They're probably more useful if you are writing code that might receive inputs from the "outside" and thus must check behavior in funky edge cases (zero length lists, NaNs, Infinity, etc). 
Many property testing libraries are descended from the original QuickCheck Haskell library.
I've heard good things about [Hypothesis](https://github.com/HypothesisWorks/hypothesis-python).

## Golden master testing

Property testing is great, because it links the test back to some fundamental 
property of the code/math. The trouble is that it still requires knowing *something* 
about what the code should do. What if you really have no clue what the output 
should be, or encoding the properties is too difficult to do in a repeat-able 
automated test and requires human input? But you still want to make sure that your refactoring and future development don't break the current implementation. 

That's where golden master testing shines. Also known as characterization testing. The idea here is very simple. Choose some input (if that includes randomness, set the random seed manually!). Then, run your function and save the output to a file. Later, to test that the behavior of the function has not changed, run it again on the same input and check that the output matches the previous output exactly. 

[Wikipedia](https://en.wikipedia.org/wiki/Characterization_test) has a good discussion of the advantages and disadvantages of this type of testing. The main two points:

* it enables testing even if you have no idea what the correct result is. Common in science and analytics. Also, common in legacy systems...
* it only prevents unwanted side effects of software changes, it doesn't actually check that the answer is correct.

## Testing through Monte Carlo simulation: A special kind of property test (guest section by Liz Santorella)

Many statistical algorithms are designed with the following setup in mind: 
Assume that data is drawn from some known distribution $D$ with unknown parameters $\theta$.
We don't know $\theta$, but the algorithm $A$ returns $\hat{\theta} \approx \theta$,
with the estimate becoming precise as the data grows large.
<!---
For example,
say we have a series of observations $y_1, y_2, \dots, y_N$ and we assume they are drawn independently from
the Normal$(\mu, \sigma)$ distribution. We don't know $\mu$ or $\sigma$. Applying the algorithm $A$ to the
data should give the unknown parameters, approximately: $A(y_1, y_2, \dots, y_N) \approx (\mu, \sigma)$.
-->

In such a setup, we can make up some parameters, create fake data drawn according
to a distribution with those parameters, and check that, when data is large, the algorithm
returns parameter estimates very close to the parameters you put in.

The appeal of this method is that it allows you to know what the right answer for your
entire procedure is (you made up the data, after all). The downside is that your algorithm
may only work accurately when your data is very large, so the test can take a long time to
run. It can also be hard to tell what counts as a correct answer: If you put in the parameter
$\mu=1$ and recover $\hat{\mu}=1.002$, is the discrepancy becuase your Monte Carlo data is too 
small or because your code is wrong?

In practice, I often combine Monte Carlo simulation testing with Golden Master testing.
I run Monte Carlo simulations for several parameter values, including some interesting
edge cases. Then once I'm satisfied that the code works, I run it on a very small example,
save both the inputs and the outputs, and make those inputs and outputs into a Golden Master test.
I don't automate the Monte Carlo test itself -- it takes too long to run, and its guarantees
are only probabilistic.

<!---
## Making sure it runs
Sometimes, you don't have time to figure out how to check that your code produces the correct output,
but you can still check that it runs without raising errors. Although this can easily be done in a unit testing
framework, I like to make sure my code runs by creating a Jupyter notebook
that calls almost every line of code that I think is important. I explain why the code behaves
the way it does in the notebook, which then makes pretty good documentation.
-->
