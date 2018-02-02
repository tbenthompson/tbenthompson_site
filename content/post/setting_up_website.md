+++
title="Setting up my website"
date=2015-12-11
+++

I have a website now. Since technical stuff is fun, I thought I'd share the way I set it up.

The site is a set of statically served HTML pages. [Hugo](https://gohugo.io/) makes this really easy. Hugo is super fast and is written in Go. You can set up a few template pages and then write posts and pages in Markdown. Some layout is also done using Go templates. Running Hugo takes your templates and pages and concerts them into static HTML. The pages can then be dropped into any web accessible folder and accessed remotely. This is nice, but a few additional steps makes everything even easier:

* [GitHub Pages](https://pages.github.com/) serves the pages from a git repository. 
* The [Kiss template](https://themes.gohugo.io/kiss/) provided a nice starting theme. I modified it a bit aiming for a very simple layout and style.
* This [Hugo documentation on using it with GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/) has some good suggestions including a very helpful `deploy.sh` script that makes deploying changes super easy.

You can take a look at all this [here](https://github.com/tbenthompson/tbenthompson_site)
