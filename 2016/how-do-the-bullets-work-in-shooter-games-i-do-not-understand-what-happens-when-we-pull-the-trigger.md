# How do the bullets work in shooter games? I do not understand what happens when we pull the trigger.

	author: Steve Theodore
	written: 2016-06-01
	views: 3057
	upvotes: 33
	quora url: /How-do-the-bullets-work-in-shooter-games-I-do-not-understand-what-happens-when-we-pull-the-trigger/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There are three different ways you can do guns.

The most common is [Hitscan](https://en.wikipedia.org/wiki/Hitscan) : that’s an instantaneous check along a line, more like a laser beam than an actual projectile. Hitscans are cheap to do and accord with what the player sees, but they don’t account for spread, wind, or the effects of gravity.

For some kinds of weapons, such as a shotgun with a spread, you might do a cone test instead: rather than checking to see if a line from the gun intersects a target you use a cone to account for the wider angle of fire. This is also fairly easy to do, but it’s got the disadvantage of potentially hitting multiple targets so it’s a bit harder to code.

Actually simulating a projectile is more expensive in computing terms - particularly if the projectile is moving very fast. Since the game simulates physics one frame at a time, a fast moving projectile may go right through a thin barrier in between frames, causing unpredictable behaviors. That’s why you tend to see this only when dealing with slow-moving projectiles you can see: arrows, rockets and so on.

