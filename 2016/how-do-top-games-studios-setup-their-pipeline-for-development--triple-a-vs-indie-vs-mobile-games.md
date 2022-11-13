# How do top games studios setup their pipeline for development? — triple A vs indie vs mobile games.

	author: Steve Theodore
	written: 2016-01-18
	views: 7915
	upvotes: 13
	quora url: /How-do-top-games-studios-setup-their-pipeline-for-development-—-triple-A-vs-indie-vs-mobile-games/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


I'm answering on a very general level rather than hitting the specifics, because I think it's a good idea to stop and consider what pipelines are really about, which is getting content into a game. You can PM me or follow up in comments if you want to go deeper.



In most cases a AAA pipeline is much, much more complex than and indie one. In AAA art production costs are one of the biggest drivers of budgets, so big studios generally recognize that it's worth a lot of investment to streamline and simplify their process. If you have a staff of 100 content people on your project and you can save each of them 5 minutes per day, you've basically hired an extra artist or designer -- and of course that equation works in reverse too: wasting 5 minutes a day per artists on that hundred person team is like losing someone. It adds up pretty fast when you consider how complex and cumbersome a lot of what artists actually do for games can be.

So, a big studio will usually have a dedicated team of technical artists and programmers who figure out how the content will be built and imported into the game and then provide tools to the art team to make that as easy as possible. Their job is to anticipate what kinds of data will need to get from a content person to the game, find a clean and simple way to send that data, and make sure that the game can use it effectively. For example in my office we've got a fairly customized Maya environment which does data validation and enforce standards: among other things, we pop up a dialog to stop you from exporting a model using non-metric units since the game thinks '1 unit' means '1 meter' and its' easy to create bugs with oddly-sized objects. We also enforce standards for things like number of UV channels or vertex colors that an artist can easily mess up without realizing it. We try to speed things up for the artists giving them a google-style search box to find things in the game since our asset base will eventually to 50,000 pieces: hunting around inside of folders is a big waste of time. We also provide standardized character rigs, enforce naming conventions and do a whole lot of other work to try to keep clerical and data-integrity jobs in the background and let the artists focus on art: nobody is happy in a team that depends on artists' typing skills.

For some problems you can pack a lot of data using conventional art tools. Max and Maya and Photoshop are good at what they do, and often provide out-of-the-box solutions for things like displaying LODs, compressing animations, or even designing shaders. In other cases -- typically with 'design' content like placing game entities in the game world -- you'll need a custom editing application which is designed around the kind of data you have to manage: Max and Maya are great at managing a complex character or a fancy model, but painful to use as spreadsheets or world editors. So a lot of pipeline design on the big end is figuring out which tools go with which job -- building as little as you can but as much as you need.

In an indie project on the other hand "pipeline" usually ends up meaning "whatever we can do to get stuff into the game". With a small team, and often with 1:1 communication between the programmer who implements a feature and the artist who provides the art for it there's much less need -- or more correctly, much less_perception_  of need for all the tools and processes that big teams expect. A small project can wing it -- and often, due to the budget and time constraints their under, they have no choice. A lot of the data is bespoke, and the format is evolving, which makes it particularly hard to evolve a good toolkit. Since so many indies are small and don't have a long track record there is also a lot of wheel-reinvention.

Luckily for the indie scene 3d party engines like Unity and UE do a decent job at tackling the worst pipeline hassles: getting models and textures into the game in a hardware-friendly format is not a very interesting or creating task, but it's not something that can safely be ignored. Luckily standard formats like FBX (which I personally loathe, but which I have to admit does it's job) and DDS or even PNG take a lot of the mystery out of getting art from Max, Maya or Photoshop into the game. It's wisest not to use Unity's built-in "we'll just read your Max/Maya files directly" because most artists need to keep some stuff in their files that doesn't belong in the game: scale reference, alternate versions, or construction history are all useful and Unity won't do a great job of differentiating between those and actual art content.

I'm a technical artist by trade so I am biased, but I think a lot of indie teams would benefit by stealing a few pages from the AAA playbook when it comes to process and data flow. Just because it doesn't bust the budget does not mean wasting artist time on cumbersome, un--artistic tasks like properly naming assets or hand-editing verbose configuration files is a good use of artists' creativity and talent. 

Shameless plug: I'm a part author on [Production Pipeline Fundamentals for Film and Games](http://www.amazon.com/gp/product/0415812291/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0415812291&linkCode=as2&tag=tecsurgui-20&linkId=7BJDW6CY7BKZL5L4)

![](https://qph.fs.quoracdn.net/main-qimg-3b1d88f075b3731c49654408efd4c009-c)

which is a pretty good overview (if I say so myself) of the major strategic considerations and gotchas in pipeline design.

