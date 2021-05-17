+++
title="Why it's okay to share your code"
date=2021-05-17
+++

TL;DR: If you write a paper that involves complex code, share your code freely online. Don't make it pretty. Don't make it easy to use. Refuse to support the code. Just share it! 

People have talked a lot already about why it's a good idea to share code with your research. I want to address a specific component of this. The desire to share good, well-maintained code often becomes a barrier to sharing any code at all. So, here, I'd just like to say that we love you, and we love your code too no matter what it looks like.

Disclaimer: This mostly comes from my experience at the computational methods and Earth science communities.

## No, you can’t see my work.

I frequently ask people for the code they used to write a paper. The answer is often a deflection or just "No." It's depressing because seeing code is so incredibly useful. With a complex algorithm, I'm more likely to jump straight to the code if I can rather than trying to read the paper description carefully. The code is the truth. The writing is just the broad strokes. For technical work, there's often dozens of tiny technical decisions that are never important enough to make it into the final published paper. But, at the same time, those little choices are what make or break an implementation. If I'm debugging why my implementation doesn't work, I'm going to go read your code. I don't need to be able to run it for this to be valuable. It doesn't even need to be readable. If I care enough, I'll spend hours just sifting through line by line.

Published papers are just a filter on the truth behind your research. In very literal fields like mathematics, the filter is very thin. The proofs and theorems are the truth and can be written literally in paper form. On the far other end, in some fields, the filter is thick. There's no way to share the truth, the lab experiment. The experiment is over. But we can and should share the raw-est results possible and a precise procedure for repeating the experiment. Computational methods and modeling papers are much more on the math side of the spectrum. The truth is straightforwardly sharable in the form of code. But, we don't do it!

So, let’s discuss a couple of the common reasons why people don't share their code!

## Embarrassed about the quality and usability.

These folks aren't even sure the code they share will run at all or produce the results they presented in their paper. They had a good idea and slammed together something that demonstrated that their idea works well enough to publish a paper.

For these people, I think we need to encourage a culture of acceptance. It’s okay to produce ugly and unusable code. I’ve done it. You’ve done it. We don’t all have the skills to make nice software. It’s even rarer to find those skills in someone who has spent year practicing some other skillset (like doing good research!). We don’t always have the time to write something reusable and we shouldn’t be expected to. When the bar for publishable work is too high, the result is fewer publications and a longer publication cycle and that’s bad for everyone involved! Apparently the bar for publishing code is so high that we often don’t even do it at all. So I’d like to try going to the opposite extreme and explicitly setting the bar so low that we publish all the code all the time. 

## Worried about the maintenance burden.

These folks think they will have to maintain the code or support users. For these people, I have a simple message. There is no maintenance burden! You can and should say no. In fact, you’re already quite good at saying no when I email you asking for your code. So, just do it the other way around. Share your code freely and then say no when people ask for help. Unless you want to help. That’s always an option. But don’t feel obligated. The code is the truth and if someone care enough, they can dig through and figure out what they need to on their own.

## All the other reasons that I won't address here

There are a lot of other reasons someone would decline to share their code:

* Career incentives. They think their secret sauce code is their ticket to a job/tenure/grants/etc. Bummer!
* The code doesn't exist. Data analysis was done using an interactive system and the original source is gone. Scary!
* Proprietary code. But then why is the paper not proprietary? Bummer!
* The code only runs on (insert supercomputer here). See above. Being able to just read the code is very valuable.

I'm not going to dive into these here, but it's worth thinking about to train people and redesign incentive systems so that these aren't issues.

## Some useful links:

* [Randall LeVeque made a more extensive and better argument than me!](https://faculty.washington.edu/rjl/pubs/topten/topten.pdf)
* [Papers with Code](https://www.paperswithcode.com/) is a great project linking papers and their code repositories. It's focused on the machine learning world. It would be great to have something similar in other areas.
* [This set of guidelines](https://github.com/paperswithcode/releasing-research-code) for releasing machine learning research code.
* [ReScience C](http://rescience.github.io/) is an open-access journal dedicated to reproduction of computational papers. 

*Thanks to Greg Wagner, Liz Santorella for helping out. If you want to chat please [get in touch](mailto:t.ben.thompson@gmail.com)!*


