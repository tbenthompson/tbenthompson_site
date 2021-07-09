+++
title="How to test scientific software: 50 suggestions"
date=2021-07-09
+++

I think testing and debugging is one of the harder aspects of scientific and numerical software. It's easy to get buried in giant pile of code and have no idea where to look for bugs. It's even harder when actually the bug isn't in the code but is in the concepts, math or data.

The fundamental problem with testing and debugging scientific software is that we don't know correct intermediate values or even the correct final output. [I wrote a previous post on similar topics](https://tbenthompson.com/post/automated_testing_for_science/) but I wanted to expand on the topic. So, here are various suggestions that probably would've helped me at some point. I'd like to expand quite a bit more on individual points here in the future. 

1. Don't trust your code. Seriously, never trust your code. 
3. Treasure correct code and use version control. Don't lose your treasure.
4. Use existing correct code to maximum value because it means you can check intermediate values that would otherwise be untestable. 
5. Hunt the internet for existing correct code. But don't trust it. 
7. Add one feature at a time.
8. Define "one feature" as narrowly as possible. 
9. Edges cases shouldn't be an after thought. Sometimes solving an edge case can be informative about the common case.
11. It's okay to spend a couple hours just thinking about to design a test problem that tests only one new feature. 
12. Any time you can, compare with an analytical solution.
13. The [method of manufactured solutions](https://asmedigitalcollection.asme.org/fluidsengineering/article-abstract/124/1/4/462791/Code-Verification-by-the-Method-of-Manufactured?redirectedFrom=fulltext) (MMS) is amazing.
14. Use MMS even if it requires implementing some extra features. It will be worth it. 
15. Check the order of accuracy/convergence rate!
16. Even on problems where the true solution is unknown, it's possible to check for convergence rate by comparing with a very high accuracy solution. 
17. Be a more careful programmer. Sometimes, It's okay to spend thirty minutes just thinking through each line of code.
18. Line-by-line step through debugging is incredibly helpful. 
19. Learn your debugging tools and IDE! 
20. Don't stay stuck for more than a couple hours. Try something different. 
21. When you notice that something looks wrong, try to encode the meaning of "wrong".
22. Be a faster programmer. Sometimes, just trying a bunch of things is the right approach.
23. Use smaller and simpler test problems so that you can iterate really fast.
24. Don't trust evaluation code. Look at the output. Bugs in evaluation code can make you waste a huge amount of time. 
25. Make lots of figures and videos. Visualizing a problem is often very effective for debugging.
39. Test derivatives with finite differences. 
46. Test symmetries and invariances. Many problems are rotationally symmetric. Or invariant with respect to rigid body motion. 
47. Test more algorithmic properties. Optimization algorithms often guarantee a decrease in objective at each step!
26. Log lots of info. It's okay to save a full matrix at each time step. 
27. Prototype! The first version of the code should not be well designed or fast. 
28. Write at least the first version in a language like Python or Julia where edit-(compile)-run cycles are on the order of a second. 
29. Doing the first phases of development in a Jupyter notebook (or similar) is really fast. Iteration time is extremely important.
30. Write a second version from scratch, maybe in a different language or style, and compare the results. You might catch some bugs. 
31. Fast tests are more useful than slow tests.
32. [Characterization](https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code) [tests](https://en.wikipedia.org/wiki/Characterization_test) (aka "golden master tests", aka "freeze tests") are useful for preventing unexpected changes. But they can't define correctness and they are brittle.
33. Robust tests are more useful than brittle tests. False alarms are a bummer.
34. Automated tests are more useful than manual tests. 
35. Continuous integration is normally worth the effort. 
36. Remove randomness in testing by setting a random seed. Even if true randomness is necessary for correctness. Consistency in testing is very important.
37. Use symbolic algebra tools to develop test cases. I frequently use [Sage](https://doc.sagemath.org/html/en/tutorial/index.html) and [sympy](https://docs.sympy.org/latest/tutorial/index.html).
38. Use multiprecision and arbitrary precision arithmetic to develop test cases. I've used [mpmath](https://mpmath.org/) and [MPFR](https://www.mpfr.org/).
40. Sign errors can often be solved with guess and check. Verify with the math later! I've found a lot of mild math errors or misunderstandings this way. 
41. Guess and check also works in some other areas. But, don't flail around in the dark for very long. 
41. Ablation testing: remove some component of your system and verify that the performance degrades as expected. 
44. Look for gaps or overlaps and other problems in your meshes. 
43. Check your normal vectors. Should they point inwards or outwards? 
42. Corners are scary. Start with something smooth like a circle or sphere.
46. The math and theory is often more important than you think. 
47. Violating function space and regularity requirements can bite you. See "corners".
48. Start with direct linear solvers. Iterative solvers introduce a whole new class of problems with preconditioning. 
49. Check the condition number of your matrices. 
50. Use standard tools and libraries where they are sufficient. 
51. Finally, remember not to trust your code. 



##### Footnotes and links
- I've also worked in machine learning and deep learning a bit. I think a similar list would apply in those areas, but I'd have to add and remove a few points. 
- [Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)
- [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
- [Sharing your code feels related](https://tbenthompson.com/post/share_your_code/)
- [Is it worthwhile to write unit tests for scientific research codes?](https://scicomp.stackexchange.com/questions/206/is-it-worthwhile-to-write-unit-tests-for-scientific-research-codes)
- [How to test scientific software?](https://stackoverflow.com/questions/3421469/how-to-test-scientific-software)
- [How to write integration tests for numeric simulation software?](https://scicomp.stackexchange.com/questions/14825/how-to-write-integration-tests-for-numeric-simulation-software)
- [Strategies for unit testing and test-driven development](https://scicomp.stackexchange.com/questions/8481/strategies-for-unit-testing-and-test-driven-development)
- [Why We Don't Teach Testing (Even Though We'd Like To)](https://software-carpentry.org/blog/2014/10/why-we-dont-teach-testing.html)
- [Spinning Up as a Deep RL Reseacher (A great high-level summary of how to do effective research in Reinforcement Learning)](https://spinningup.openai.com/en/latest/spinningup/spinningup.html)
