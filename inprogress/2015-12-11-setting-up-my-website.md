---
layout: post
title: Setting up my website
---

I have a website now. Since technical stuff is fun, I thought I'd share the way I set it up.

The site is a set of statically served HTML pages. [Jekyll](https://jekyllrb.com/) makes this really easy. You can set up a few template pages and then wrote posts and pages in Markdown. Running Jekyll takes your templates and pages and concerts them into static HTML.  The pages can then be dropped into any web accessible folder and accessed remotely. This is nice, but a few additional steps makes everything obscenely easy:

* [GitHub Pages](https://pages.github.com/) renders the pages from a git repository. You just place the templates and posts in a git repository with the name username.github.io. Then, Jekyll is automatically run after each push and the live page is updated.
* The [Hyde template](https://github.com/poole/hyde) provided a nice starting point for my page. I just forked the repository, renamed it "tbenthompson.github.io" and then made my changes.

You can take a look at all this [here](https://github.com/tbenthompson/tbenthompson.github.io)
