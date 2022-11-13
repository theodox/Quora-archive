# Video Games: 

	author: Steve Theodore
	written: 2015-02-09
	views: 1216
	upvotes: 9
	quora url: /Video-Games-How-hard-is-it-to-create-human-like-NPCs-AIs/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


as [Daniel Super](https://www.quora.com/profile/Daniel-Super) points out, it's extremely hard from a computational point of view. Just doing simple path planning for a few hundred agents is a real stretch on modern hardware if you want to run at 60 FPS -- at 16.666 milliseconds per frame it's hard to just pick behaviors and find paths. 

Getting beyond that is far harder. A "realistic" AI would have many of the same frustrating, opaque qualities as a real human: if you called it and it didn't respond, would that be a bug -- or was the AI just trying to remember where it left it's keys? 

And most importantly, how could you _communicate the difference to the player_ in a natural way?

You could certainly have the NPC say, "oh, sorry, I was just wondering where my keys were" once: but if it showed up five or six times in a play session the player would go bonkers and the naturalism of the behavior would be shot. To really sell the human-like nature of the characters you would need tons of animation and voice data (we can't really synthesize believable versions of either, at least not on the fly) and a very sophisticated model of the motivations of the character. And the audience is super critical: we're all programmed to be expert judges of human behavior, since it's a critical survival skill. Really subtle flaws can unmake lovingly hand-crafted character models and animations very easily (the [uncanny valley](http://www.arts.rpi.edu/~ruiz/EGDFall08/postmortemreadings/Theodore%20Uncanny%20Valley.pdf) effect) ; it will be a long time before procedurally generated behaviors are anywhere near as good as those.

In any case, the 'realism' of the AI is inextricable from the animation, the voice acting and the graphic presentation, all of which are extremely resource-intensive. So, considering we have a such hard time getting the little sunsabitches to just walk through doors reliably, I'd have to say the answer is "pretty damn hard".

