+++
title="DRAFT! Automated testing for scientists and data analysts"
date=2018-02-07
+++

A lot of scientists and data analysts don't use automatic test suites for verifying their code. 
And, I think that's because it's really hard.
Almost all the introductions to automated testing that I've seen come from a more typical software engineering perspective. They assume you already know exactly what the output of your code should be.
And the trouble with science is that that's rarely the case. 
I mean, if you know the results ahead of time, we wouldn't be doing science! 

It's hard to square this situation with the consistent loud noises coming from the software development world (in my case, from inside my head!) saying "Write tests! Write tests! Write tests!". "But, I can't!"

I've been dealing with this battle for a few years now and feel like I've figured out some coping strategies.
The simplest solution is to just give up.
And for some types of science, I think that's the right thing to do.
Essentially, whether or not to test is a question of how important it is that the results are correct.
In that sense, I don't think automated testing makes sense for exploratory analysis.
But, for a reusable algorithm or production/final analysis, tests are invaluable.
I mostly work with Python, so the question of whether something should be tested often goes hand in hand with whether I'm working in a Jupyter notebook or with scripts/modules/a proper package. 

So, let's back up and ask: why should we have automated tests?

## Automated testing

Automated testing is valuable for ensuring that software does what is is supposed to do. Automated testing:

* reduces fear when making implementation or design changes (this is huge, in my opinion!) One perspective on when to write tests is to write tests whenever you feel afraid of making a change and to keep writing tests until your not afraid anymore.
* enables rapid refactoring without fear of breaking the code base
* gives instant feedback
* helps improve software accuracy, correctness
* provides a form of precise documentation

[A couple good discussions of why we should unit test.](https://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort)

I've also enjoyed the book by Michael Feathers, "Working Effectively with Legacy Code", because it focuses on adding tests to previously untested and maybe poorly designed "legacy" code (he defines legacy code as any code without tests!).
[A summary of the book](https://softwareengineering.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code)

But, returning to the original problem, automated testing can be very difficult in science and analytics because the true answer is not known. Sometimes low level functions can be assigned a "correct" result. But, for higher level constructs (e.g. an entire time series forecast or the solution of a complex PDE), it's normally much harder to determine what is right and wrong.  It requires careful input from the statistician/scientist/analyst to determine if something looks right or wrong and whether there's anything fishy going on.

So, given that we want to have automated tests, but the inherent nature of the problem makes most testing difficult, what do we do? I still struggle with this issue and am learning all the time, but I've found three types of approaches are particularly useful: 

## Special cases

This first approach is the most common, the simplest, and often the most valuable. Suppose I'm writing a [general algorithm for solving elastic partial differential equations for an arbitrary geometry and set of boundary conditions](https://github.com/tbenthompson/tectosaur). It might be really hard to say whether the answer I'm getting is correct for any given problem. But, some specific problems have already been solved exactly. For example, a spherically symmetric problem is easily solved by hand and any number of textbooks have exact solutions. Or, similarly, the motion of the Earth due to an planar earthquake in an infinite flat Earth has [a well known solution](abc).

Going a different direction, developing statistical algorithms --> simulation? Good lead in to property testing in the next section.

## Property testing

I think property testing is the most useful approach when the answer isn't known. 

Property testing is another approach to testing when the correct answer is not known. Instead of check the final answer, we check a *property* of some final or intermediate part of the calculation. For example:

* Or, blended more wit a special case, Newton's method for root finding should take exactly one step to solve any linear system of equations. So, a simple property test might be to generate 100 random linear systems and check that all of them are solved. This is a sort of 
* In the case of a finite element model, checking for solution convergence with decreasing mesh size. 
* The solution of a PDE should obey the original PDE

I've always written property tests by hand, but there are some libraries that attempt to automate part of the process. They're probably more useful if you are writing code that might receive inputs from the "outside" and thus must check behavior in funky edge cases (zero length lists, NaNs, Infinity, etc). 
Many property testing libraries are descended from the original QuickCheck Haskell library.
I've heard https://github.com/HypothesisWorks/hypothesis-python

## Golden master testing

Property testing is great, because it links the test back to some fundamental property of the code/math. The trouble is that it still requires knowing *something* about what the code should do. What if you really have no clue what the output should be, or encoding the properties is too difficult to do in a repeat-able automated test and requires human input? But you still want to make sure that your refactoring and future development don't break the current implementation. 

That's where golden master testing shines. Also known as characterization testing. The idea here is very simple. Choose some input (if that includes randomness, set the random seed manually!). Then, run your function and save the output. Later, to test that the behavior of the function has not changed, run it again on the same input and check that the output matches exactly. 

[Wikipedia](https://en.wikipedia.org/wiki/Characterization_test) has a good discussion of the advantages and disadvantages of this type of testing. The main two points:

* enables testing even if you have no idea what the correct result is. Common in science and analytics. Also, common in legacy systems...
* only prevents unwanted side effects of software changes, it doesn't actually check that the answer is correct.

## Golden master testing with py.test (NOT SURE IF I SHOULD INCLUDE THIS)
The py.test tool is handy for running a batch of tests in python. It's a very general tool for running all the tests in a project. The pattern normally follow is: Add a `tests` directory the root of the project. Name any test files in that directory `test_xyz.py` and then any tests within that file `def test_abc():`. py.test will find all of these automatically and run them. I try to keep the run time of the main test suite short enough that I can just run `py.test` every time I make a change and it takes less than a second to confirm that I didn't break anything.

For more happiness, add a `pytest.ini` file to the root of your project:

```
[pytest]
addopts = -s --tb=short
```

The `-s` causes any text printed by your tests or code to appear on the screen. By default, py.test suppresses printing/logging to standard out.
The `--tb=short` leads to shorter, more concise tracebacks in the case of test failures.
