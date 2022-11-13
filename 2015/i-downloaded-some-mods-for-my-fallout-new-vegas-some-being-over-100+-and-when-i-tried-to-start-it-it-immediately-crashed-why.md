# I downloaded some mods for my Fallout: New Vegas (some being over 100+) and when I tried to start it it immediately crashed. Why?

	author: Steve Theodore
	written: 2015-01-06
	views: 510
	upvotes: 3
	quora url: /I-downloaded-some-mods-for-my-Fallout-New-Vegas-some-being-over-100+-and-when-I-tried-to-start-it-it-immediately-crashed-Why/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Not a satisfying answer, but...

PC game development is a huge pain in the butt. It used to be worse, but the infinite combinations of hardware, drivers, operating system versions, languages, and God-knows-what-else-is-running-on-your-system make it pretty hard for even the most disciplined developers to support everybody. That's why consoles got popular: it's much harder to make a PC game work on a broad range of hardware than on a single, well-known platform.

Modders have it worse than pro developers: it's hard to work inside of somebody else's code base, and as a modder you rarely have testers and the programming time to figure out why having a particular mouse drive or sound card or Windows service pack crashes.

And, lots of mods end up competing for scarce resources (for example, the game may have a byte limit for a certain kind of resource: maybe you can have only 256 different sound files, or 128 physics materials, or something like that. Often modders will re-use some of those scarce assets -- replacing textures or models, for example. But the if the replacement overwrites another modders work instead of the files the original game came with the results can be very unpredictable. 

There's an infamous story about a very successful Skyrim mod which worked beautifully 98% of the time. However it crashed hard if it was installed alongside several popular porn mods. He eventually stopped supporting his mod because he was tired of getting angry emails from porn fans. 

So, modding is very much a YMMV (your mileage may vary) hobby. Even pro developers can't always support 100% of their customers, and with modders the situation is much worse. On the plus side, learning how to debug it all is a great education in how games and programming really work.

