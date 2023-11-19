+++
title="Extreme website and app blocking"
date=2023-11-19
+++


Computers are awesome. Also computers really suck… the time out of my day. The same goes for phones and tablets and anything that can access the internet. I've been addicted to way too many different internet activities: Reddit, TV, Instagram, Twitter, Hackernews, product reviews, travel blogs, tech blogs, the EA forum, etc, etc, etc. Even Wikipedia can be a huge time sink for me![^1] Maybe I have less self control or less willpower than others?[^2] Regardless, my internet time wasting got pretty bad over the years. Working from home during the pandemic finally set me off a cliff where I realized I _really_ needed to solve the problem.


<div style='background-color:#999999'><sub><a href="https://matt.might.net/articles/cripple-your-technology/">“Every advance in productivity afforded by technology has been quickly swallowed by a corresponding reduction in the barriers to procrastination.”</a></sub></div>

So, in late 2020, I started putting together a system of blocks that make my computer and phone helpful rather than destructive. I wasn’t successful immediately. I’ve made many little tweaks in that time and patched up gaps and cracks. But, the result is a system that solves most of my internet addiction problems without completely disabling my devices![^3] Over time, the urge to do addictive things online has also faded a lot, but I have no plans to loosen the controls.


## Blocking

![Flowchart of blocks](/images/blocks/image1.png "Blocks flowchart")


The flowchart above describes the algorithm for my blocks. The basic principles are:

1. My laptop is almost exclusively for work. Non-work stuff, even if it’s not addictive like a bank website, should be blocked. Having different devices for different purposes really helps to keep me doing what I want to be doing.[^4]
2. I use a “deep work” whitelist of acceptable apps and websites for times when I really want to get some coding or writing done. 
3. My phone and tablet[^5] can be used for anything else. But very addictive stuff is either completely blocked or is tightly time limited.
4. All my electronic devices should stop being useful or fun at night so that I am more likely to go to sleep. I don’t get sleepy at night until very very late.[^6] But, if I lie down for ten minutes, I will fall asleep. So if I want to go to bed on time, I need to reduce the attractiveness of staying awake.
5. I can violate these rules with permission from a few different people who share a password that unlocks these blocks. For example, if I want to watch a TV show with a friend, we’ll either use their laptop or they will use the password to unblock my tablet for an hour. I do not know the password!

In painstaking detail:
1. I use [Cold Turkey Blocker](https://getcoldturkey.com) for blocking websites and apps on my laptop.[^8] I have six block lists in Cold Turkey:
    1. “Permanent” - These are things that I should never use my computer for. Some obvious suspects are in there: TV shows, Instagram, Strava, Twitter, news websites. But also, there are also a lot of online shopping, blogs, and product review sites.[^9] This block is password protected with the password. 
    2. “Non-addictive” - websites that are not work but are also not addictive. Normally I shouldn’t be using my laptop for these tasks. But, if I need to, I can type 150 characters of random text to unlock this block. This is mostly financial and bill-paying related stuff like my bank, credit card websites, airline websites, Mint.
![alt_text](/images/blocks/image2.png "image_tooltip")
    3. “Whitelist” - This blocks every website and app _except_ for those on a list that I’ve built over the years. I will typically enable this in an irreversible way for 1-3 hours but sometimes for a whole day. When I first started, I couldn’t enable the whitelist for more than 20 minutes without having trouble getting work done. But, I’ve just noted down sites whenever I find something that I need access to and then I add the site after the current whitelist session is over. Being able to completely block almost all distraction potential for an hour gives me a lot of momentum even after that hour is over.
![alt_text](/images/blocks/image3.png "image_tooltip")
    4. “Email” - This is just for email websites and apps. Email can be very addictive! Especially when I’m expecting an important message. Knowing that I absolutely can’t access my email until later in the day is helpful for focusing on other tasks. After a morning email session, I block access to my email until the evening. (“Start and lock for 7 hours”)
    5. “All apps at night” - This blocks every last app on my computer from 9:15pm until 2am.[^10] Just like “Non-addictive”, if I need to, I can type 200 characters of random text to unlock this block. 
![alt_text](/images/blocks/image4.png "image_tooltip")
    6. “Whitelist at night” - even if I unlock “Everything at night”, the whitelist _also_ enables from 9:15 pm to 2am. This block is password protected. So, I can only use my laptop for work during that time. If there’s some work emergency, this means I can handle it. Also, I sometimes get very motivated in the night and want to work.[^11] I don’t object to that and don’t want to prevent myself from doing that. This double night-time block evolved out of an issue where I would want to work in the evening and would disable my night-time block. Then, I would work from say 10pm to midnight. But, after I was done working, I would take advantage of the unlocked laptop and stay up until 3am wasting time online by doing something like watching a TV show.
2. The phone and tablet blocks (synced together) are much simpler. I use the built-in Screen Time tools and allow myself:
    - 12 minutes a day on Twitter. I get a lot of value from Twitter but it has a lot of addictive potential. 
    - 10 minutes a day on Discord. 
    - 20 minutes a day summed across all apps or website in a big list of time-sinks like YouTube[^12], Reddit[^13], etc. There are 114 websites on this list right now.
    - One hour a day on Safari. This covers the “Do nothing**” in the flowchart. If a website isn’t blocked some other way, I’m still limited to at most an hour on that site. And normally much less time because I will have already used up some Safari time for other purposes. 
    - Complete blocks on Instagram, a few video games and all TV/Movie streaming services. 
    - Other web browsers are blocked so I can’t evade the Safari block.
    - Most apps are completely blocked after 9:45pm. The exception to this are apps that have no potential to keep me up late and are useful while traveling or out late: Messages, WhatsApp, Weather, Calendar, Uber, etc.
    - I should probably block the App Store but having access hasn’t caused me problems yet. 
3. I maintain and update these lists above by automatically tracking my time use. Lots of [other folks](https://www.benkuhn.net/zero/) have written about this. I use [Timing](https://timingapp.com/) for this on my laptop. On my phone, I use the built-in Screen Time app. Once a week, I look at the websites and apps I’ve used over the last week. If there’s anything that should be added to a block. If I realize I got distracted by a site, I’ll update the block lists immediately.
4. I also use [Daily](https://dailytimetracking.com). It pops up a window in the corner of my screen every ten minutes asking what I’m doing. I can respond with one key press whether I’m working (“w”) or not working (“n”). Since my laptop is intended for work, it’s useful to track when I’m using it for non-work purposes and try to adjust the system to push that kind of thing off to a different device. It’s also nice to know how much I’ve worked in that past week or month. “Oh yeah, that’s why I’m tired! Maybe I’ll go for a long run in the mountains tomorrow.” or “Gosh, I didn’t get much done this week. I wonder why?”
![alt_text](/images/blocks/image5.png "image_tooltip")

## Appendix

Implementation details that I left out above:
* If you open “App Limits” and try to add a time limit for Safari, you will sadly be unable to find the app! But there’s a workaround. Go back to the main Screen Time page and click “See All Activity”. Then, scroll down to the “Most used” list and select “Safari”. Click “Add Limit” and you’ll be able to set a limit. [Source](https://discussions.apple.com/thread/250088607)
* Make sure you select “Block at End of Limit” when setting up an App Limit. The default is to just yell at you but not actually block anything.
* I haven’t found a good way to block an app completely in Screen Time in a way that also allows using a password to temporarily unlock the block. Instead I just set a 1 minute App Limit. For most things, one minute is a short enough time to make the app useless. You can’t watch a TV show in one minute. 
* To set up my night time block in Screen Time, I set a schedule in “Downtime”, then I turned off “Block at Downtime” so that my phone is still usable. Finally, I select which apps are acceptable in “Always Allowed”.
* In Cold Turkey, I give an allowance of five minutes for the night time block. Without this, all my apps would suddenly close at 9:20pm. That’s normally not a big deal, but it is nice to be able to leave some browser or IDE tabs open overnight. Occasionally, killing all my apps is a big deal like when I’m running some code overnight and I didn't remember to launch the job inside tmux.

Technical problems that I’d love a solution for:
* Cold Turkey doesn’t allow a scheduled block to also be temporarily activated. So, I need to keep my night-time whitelist manually in sync with my day-time whitelist.
* Cold Turkey doesn’t have a way to temporarily turn off a block. So if I disable a block, I need to make sure to turn the block back on. In contrast, Screen Time allows choosing to disable a block for either 15 minutes, 1 hour or all day. It's nice that I can't accidentally leave a Screen Time block disabled.
* It’d be nice to be able to request access to an app/website remotely with Screen Time. If I need a Cold Turkey block on my laptop disabled remotely, I can do a screen share and let someone remotely type in the password without telling me the password. But, iOS has no mechanism for remotely controlling a phone like that. So, at the moment, if I’m traveling and need to unblock something, I just use my laptop. I've managed to get through quite a few trips without needing to disable anything!

<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     Reading about the history of some country that I’ve never read about before is an easy three hours.

[^2]:
     I also don’t read fiction anymore because I just won’t sleep until the book is over. Should I be embarrassed to admit that I read the entire ASOIAF (Game of Thrones) series in less than a week in 2010? I do still listen to fiction audiobooks, but even that can be a bit risky and I mostly reserve it for vacations or to listen to while I do some big home repair project.

[^3]:
     At one point, Liz went even further than me and completely blocked the internet on her personal laptop unless I explicitly enabled it. Her laptop was not connected to our wifi and only I had the wifi password. So, when she needed to use the internet on her laptop, I went into our router settings and activated a guest wifi network for her. The guest wifi was then active for three hours. Note that she did have a separate work laptop and these wifi blocks only applied to her personal laptop. 

[^4]:
     Actually working at the times that you plan to work is orthogonal to the question of how much you work.

[^5]:
     My “tablet” is effectively a second laptop because it has a fold-out keyboard and trackpad. This has been important for getting this system to work. Otherwise, I would drift back to using my laptop for non-work tasks that require a lot of typing. I think having a second laptop would be less effective because iPadOS is much easier to irreversibly lock down than a laptop. Also doing a lot of work tasks (coding!) is unpleasant on a tablet so this firms up the work vs not-work separation.

[^6]:
     I get sleepy at 3pm all the time…

[^8]:
     The Pro version currently costs $39 but it’s worth like 1000x more than that to me. None of the other blocker apps are at the level of Cold Turkey. If you use something else and like it more, let me know!

[^9]:

     I would’ve loved to share the contents of all my block lists here, but that would be akin to sharing my entire search history. It’s private! If you want the contents of the whitelist, I am more willing to share that because it’s only work-related websites. Feel free to email and ask.

[^10]:
     I chose 2am for the stop time so that I have some leeway to wake up early instead of unblocking. Suppose I need to get something done by 7am and it’s not done by 9:15 pm. I can either unblock a device or I can just wake up early. On the flip side, 2am is late enough that I won’t stay up in order to wait out the block. If I had chosen 11pm or 12am, that might’ve been an issue. 

[^11]:
     In grad school, I got most of my best work done between 10pm and 5am. How I “fixed” this deserves its own post. These days, I’m most productive in the morning. But, I still sometimes stay up late working when I don’t have anything important in the morning and I’m motivated.

[^12]:
     There are work-related talks on YouTube that I might want to watch but normally I can just substitute by reading the corresponding research paper. I'm not a big fan of watching talks anyway.

[^13]:
     Reddit is incredibly useful for getting opinions. I’m one of those people that appends “reddit” to the end of lots of Google searches.