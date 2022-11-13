# What are the pros and cons of making one's game open source?

	author: Steve Theodore
	written: 2015-02-14
	views: 2818
	upvotes: 31
	quora url: /What-are-the-pros-and-cons-of-making-ones-game-open-source/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Going to OS is removing a significant barrier to [cloners](http://www.gamesindustry.biz/articles/2012-05-31-how-to-protect-your-game-from-clones): it's far easier for the would be thief to repro your game if they've actually got your source code - reverse engineering the game is a non-trivial amount of work. Theoretically copyright should still protect the contents; however the combination of international jurisdictions and high enforcement costs makes it hard to rely on this. 

If you're going for a multiplayer with a server-based back end that you control, it's an interesting toss up. You may get good help and free bug fixes from friendly white-hat contributors, but you've also made the job of would-be hackers easier. As always the client is "in the hands of the enemy" in online games, but giving out source might allow for exploits that would be harder to spot by decompiling.

There's also issues with spoilers, easter eggs and things like hanging features. It's no big deal if the people looking at Mercurial see a half-implemented feature in the code base; they migh think "Oh, that will be cool when it's done" or even try to contribute to it. If you are browsing the open-source version of Last Of Us and see the the whole final scene laid out in code before the game is released.... when, that's a different story.

Realistically, the open-source movement works quite well for programmer-to-programmer mini-economies. I can give away work (I do : [theodox/mGui](https://github.com/theodox/mGui)
) knowing that what I lose in the (low) potential for profiting I get back in the form of other people's contributions to my project and other OS projects I can use. The losses are mostly theoretical (I'm not starting a company to sell my maya tools, the payoff would never be enough to justify the hassle) and the gains are real. 

In the case of a business where you sell software to end users, instead of essentially swapping services with other programmers the situation is much murkier. Piracy is already rampant in games (the 90% figure often cited may be too high -- but it's not wildly off) and giving away the source makes it easier and less dangerous: there's no need to worry if that cracked copy of FIFA is stealing my credit cards if I compiled it myself! If you go with a F2P model where all the money is made by micro-transactions and you own the servers, you will have to see if giving away your code makes it easier for your fans to help you or your hackers to hack you. As [Heartbleed](http://heartbleed.com/) showed, being open doesn't mean that only nice people will be scanning your code base, or guarantee that the nice ones will spot the holes first.

Overall, I don't think games and OS are a natural fit. Tools and pipeline work that are more generic and less specific to a given IP, absolutely. Individual modules that address specific things -- a better vertex buffer management system, a nice way to stream texture data, a cheap way to calculate navigation meshes -- these are all useful and will probably attract high value contributions from peers. But a whole game? I doubt it.

