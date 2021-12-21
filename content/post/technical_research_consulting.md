
+++
title="We need technical research consultants."
date=2021-12-15
+++

##### Prelude: Research scientists and research consultants. 

<sub>This is a proposal for a new type of research organization that would provide technical support, particularly on things like lab equipment or computational methods or software: technical competencies that take a long time to develop and are mostly independent of the particular lab environment.</sub> 

<sub>There's a spectrum of hands-on technical researchers. On the one hand, research scientists are full-time technically talented team members that execute on research plans. They have deep knowledge of the research in the lab and can help maintain continuity and keep execution speed high. On the other end of the specrum, research consultants are briefly involved in many different projects. Research consultants are valuable less for their deep knowledge of a particular research agenda and more for a particular skill that they have developed to a high degree. Ultimately, I think we need many more research scientists than research consultants. But right now, we have too few of both.</sub>

<sub>I wrote this in September and I've shared the idea with a lot of people but I figured I should post it more publicly. I'm less excited about the proposal than I was then. I think there's something here but this particular idea may not be quite right. I would be very excited about being involved in an effort similar to this. If you're interested in similar ideas and want to chat, I'd love to hear from you.</sub>

## Overview

I’ve been providing part time software, computational and mathematical help to earth scientists for the last two years. In that time, I’ve repeatedly found projects that I could accelerate by months in just a few days of my time. That makes me think that *a huge opportunity to accelerate scientific progress is to provide the technical expertise that scientists need to get their research done.*

But, why aren’t scientists getting this support already? The basic reason is that **there are not enough senior individual contributors (ICs) in science**. The tech industry has found a winning formula by defining both IC and manager career tracks allowing companies to hire and retain top technical talent. By comparison, retaining top technical talent in a hands-on role is frequently impossible in academic science. Two processes conspire to limit access to top technical hands-on talent:
* *Scientists are forced into management.* Hands-on technical skills peak during the postdoc and first few years of a faculty position, but often rapidly deteriorate because most faculty members spend their time managing their team, finding funding and handling university responsibilities. The standard career path follows from graduate student to postdoc to faculty. By the time a scientist’s hands-on skill set has reached a high level, they either become a manager (faculty) or leave academia for an industry position. 
* *Postdocs and early career faculty are normally too busy and provide assistance only reactively.* As a postdoc, a scientist must be laser focused on finding a faculty position. As an early career faculty member, they must be equally focused on tenure. At each stage, a scientist is sufficiently focused on their own career progress that they do not have time to provide substantive advice to other projects. This is especially true when that assistance needs to be given proactively since the receiver does not have a sufficient map of the technical domain to know who they need to contact.

In response, I would like to **establish a technical research consultancy focused on proactively identifying and assisting projects** that are stuck, slow or abandoned due to solvable technical issues. Initially the team will be focused on applications of computational science, software engineering and machine learning to physical and life sciences with a particular emphasis on projects that have clear impact. We will provide a couple weeks to a couple months of assistance per project depending on the needs. The goal will be to set projects, researchers and especially graduate students off on the right track and help build the technical foundation of the project and the skills of the partner.

The range of technical skills required for doing cutting edge research is ever-increasing and the traditional academic model of encapsulating all of those skills in a single researcher is failing. Instead, there is a pressing need to build new institutional models that provide technical skills as a service to principal investigators and their teams. 

See the rest of this document for more details.

### Concrete examples of the type of work that a technical research consultant (TRC) might do:

I’ve been operating part time in a role like this for the last six months and I’ve had several experiences where I was able to accelerate projects massively just by spending a few days helping out. There’s a lot of low hanging fruit: 
* I set up some tools to help a researcher doing tsunami simulation account for surface bathymetry/topography in his models which led to substantial changes in the predictions. This took me about three days and was something the researcher thought was not possible using the method they had based their simulations on.
* I sped up a computational geometry algorithm that was the bottleneck in doing plate tectonics and earthquake science research. Previously, the algorithm took over an hour and was a critical bottleneck in experimenting and iterating quickly. Now it takes 15 seconds and the group has been able to move much more quickly. This took me about three days and the group had been using the poorly optimized version since 2006. 
* I helped a researcher whose statistical estimation algorithm was not converging and identified where the popular open source package they were using had an algorithmic error. They had been stuck on the problem for months and had almost given up on the method. This took me about four hours between discussing the issue with them and then pair-programming looking into the code.


### What types of work will a TRC do?

A technical research consultant will focus on rapid high impact work plus continuous learning and networking:
* Connect with researchers to *identify projects that need technical assistance*. A major part of the role will be to have a good relationship with many research groups in order to have an overview of where the TRC could best contribute. 
* Quickly *provide projects with a technical foundation* to get off the ground.
    * Provide assistance with methodology, algorithms, software, design. 
    * Write summaries of the work done and assistance provided. 
    * When possible to do so without negatively impacting the client researcher/team, publish these summaries in an organization publication.
* *Publicly explain deep technical concepts in clear terms* when the concept comes up in a work setting and no high quality explanation already exists. Many cutting edge concepts are explained exclusively in articles written for a narrow audience and full of technical jargon. Bringing those concepts into the light of day is a natural extension of this educational consulting model. 
* *Bridge the gap between methods researchers and applications* of those methods in the physical and biological sciences. Often methods researchers have little incentive to seek out applications for their work. As a result, applications are often using tools that are over a decade behind the state of the art. Providing this bridge will help accelerate adoption of the state of the art.
* *Publicly share targeted code snippets and small software packages* where appropriate while avoiding getting bogged down in large speculative software projects. 
* *Continuous learning to stay on the skill frontier.*


### How long will a TRC project last?

Ideally short on the scale of a few days up to a couple months. The goal is to engage with a client research team, learn extensively about the problem that they are working on, and then provide help in the best way possible. Imagine a similar role to a private sector software contractor or management consultancy but translated into a technical research dimension. The goal is to provide a firm foundation for the client research team to perform their research, but not to execute or complete an entire project. 


### Three stages of a TRC organization:
1. **Network:** The three components of the network are the TRCs themselves, the scientists working on impactful but stuck projects and the potential funders. Building this network will be the initial task. This task allows for some space to build the key playbook for a TRC:
    * Learn strategies for finding which projects both need technical assistance and have high impact.
    * Building experience myself as a TRC to form the basis of a future core team. 
    * Producing documents with advice on how to be a TRC.
    * Identifying a core team of potential technical research consultants who are interested in joining full time. 
2. **Trial period:** Find funding for a small team of TRCs for a year. A tight-knit team will connect with client researchers to find opportunities to accelerate projects. 
3. **Fellowship:** TRCs will be hired into a two year postdoc-like position. Success will result in the offer of a repeatable five year fellowship. 


### Will it be hard to find capable and interested TRCs?

TRCs need to have skills in several dimensions. Obviously, they need to have **at least one rare and valuable technical skill.** But, they also need to have **good project management skills, writing skills, and client communication skills.** Finding this combination of talents will not be easy. In addition, we will be unable to pay competitive rates with industry research science or engineer roles where such an individual could easily be paid \$500k in total compensation. 

That said, there is a large supply of technical talent that would like to follow an individual contributor career path in science. I’ve personally talked to a slew of people who wish they could continue as a scientist without becoming a faculty member. Many of these people leave academia for industry or settle for a different career path than they would prefer. A smaller number work at national labs or other large laboratories where research scientist positions are more common. A select few find research scientist positions in academia.

The pool of candidates for a TRC position will consist mostly of mid-career academic and industry technical workers who have built an in-demand technical skill set: current postdocs, early career faculty, industry engineers and researchers. Many things drive people towards academic research: intrinsic motivation towards societal impact, discovery, autonomy. Technical research consulting will have a similar spectrum of these same attractive characteristics. 


### Where might we find funding?

Private philanthropy is the main target at the moment.

I don't think technical research consulting is a sustainable model when the "client" researchers themselves are expected to pay for the services. Only the largest research labs have the flexible funds to pay. This fact is fundamentally why there is a market failure here: I think there's a lot of demand for short-term technical help and there's a (small-medium?) supply of people who would be capable and interested in doing that work. But, the friction of university and grant funding mean that these people aren't able to work together. Often, grant funding is slated for very specific purposes and can’t be re-allocated. 

On the other hand, there seems to be a lot of energy in the private philanthropy sphere for "improving science and scientific institutions". The growth of Progress Studies over the last few years is one of many demonstration of this. This TRC project fits right in with this trend and will hopefully be attractive to private funders. 


### How much funding would be required for a trial period?

The main expense would be team member salaries and benefits. I’m uncertain about what rate to pay. Great team members will be in a situation where they can get paid very well in the private sector. I’m guessing that the right salary number is somewhere between \$100k and \$150k. I would expect an additional \$40k in health insurance, administrative overhead, travel costs and equipment per team member. With \$1 million per year, we could support five to seven team members depending on the salary number. I would take a smaller salary. The exact details don't seem particular important to pin down here.

### What would the organizational structure look like?

I see two potential models. One is a typical executive-driven organization and the other is a partnership. 

In the executive-driven model, the hierarchy would be very light. While the team is small, I would like everyone to have the core TRC job as their main purpose with a few team members having additional responsibilities
* A technical leader. This person would be responsible for team management including ensuring that everyone’s work is aligned with the core mission of enabling cutting edge science. 
* A business leader. This person would be responsible for continued funding and relations with funders. 

In the partnership model, the structure would be similar to a law firm with partners that individually lead their own subteam. Initially, I could imagine three “senior” partners with another junior team member each.


### When?

An ideal model would involve a soft start. Over the next year, we will build the network and possibly obtain a small amount of funding for one or two TRCs either part or full-time. Then, starting in early 2023, we would have funding for a one year trial period of five to seven team members. 

### What fields are you likely to work in most frequently? Are there fields where technical research consulting would be less useful? Can we learn from those fields? 

In most of the physical sciences, life sciences and engineering there is a faculty-as-manager culture with few senior individual contributors. The faculty manage their labs and delegate the hands-on work to graduate students and postdocs. 

By contrast, mathematics doesn’t need an additional individual contributor career track because math PIs are in “the lab” every day: they keep writing proofs for their entire careers. Similarly, a surgeon will develop new procedures by doing the procedures themselves. Other fields like economics have a culture where faculty are more likely to stay up to date with their technical skillset and continue doing hands-on research. Statistics, econometrics and biostatistics also have a culture of encouraging faculty to provide consulting assistance to researchers that need help with issues like experiment design or hypothesis testing. 

It would be interesting to further investigate the historical and systemic reasons why fields have developed to have such different patterns and cultures. 


### Will authorship for the TRC be expected?

It will depend on the project. Researchers will be less interested in our help if it means adding an author to their paper. If the contribution is small, I would prefer to leave the TRC contribution in the acknowledgements in order to reduce the cost of our involvement. In case of a larger involvement, anything but authorship would be dishonest. In cases where a TRC is left out of the authorship, we would likely publish a report in our organizational publication detailing our involvement with the project in order to document the value we provide and help future projects in a similar position. Ideally, we would combine that report with educational materials that would help future teams in a similar situation. 


### Why does this need an organization, rather than just giving grants to independent scientists directly?

There are a few major advantages of an organization:
1. People work best in a team with a shared mission! The frequent isolation of academic research is one of its major weaknesses. No one should be working alone for many weeks or months at a time. 
2. The power of referral. When I find a project that clearly needs help but that I don’t have the skills to provide the help needed, I would like to be able to easily refer that team to a colleague.
3. Having an organization with a shared mission and stable funding will open the career path to a much wider range of potential team members. The uncertainty of being an independent scientist removes most of the talent pool. 
4. Career mentorship will be critical. Working in an uncertain and new career path can be demoralizing and lead to burn out. This is much easier to ameliorate together, as a team. 


### What are the restrictions on the TRCs?  Are you funding them to do whatever they want, or just to collaborate?  Are they allowed to switch fields, or are you hiring them for a specific area?

I would like to give team members a lot of autonomy in what they work on, but with a clear expectation that they demonstrate impact and focus on short-term engagements. 


### Would you only work with academic or nonprofit scientists?

Initially, I think it would be good to keep a clear focus on the main goal which is to solve some of the bottlenecks in academic science by providing access to technically talented individual contributors. At some point this focus might be reconsidered. It might be useful to work with private sector businesses in order to provide additional funding to the organization. 

<sub>Thanks to Milan Cvitkovich, Tomo Sato, Elizabeth Santorella, Brendan Meade, Lyke Thompson and probably a couple others for useful comments on this!</sub>
