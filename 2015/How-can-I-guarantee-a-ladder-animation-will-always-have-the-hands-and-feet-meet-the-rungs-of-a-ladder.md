# How can I guarantee a ladder animation will always have the hands and feet meet the rungs of a ladder?

	author: Steve Theodore
	written: 2015-09-25
	views: 1056
	upvotes: 6
	quora url: /How-can-I-guarantee-a-ladder-animation-will-always-have-the-hands-and-feet-meet-the-rungs-of-a-ladder/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The cheap solution is simply to dictate the position of the ladder and the spacing of the rungs so that the distance between rungs exactly matches the distance travelled in each half-cycle of the climb animation. This does not require much fancy tech as long as the animation system drives the players motion from animation data directly (which it probably should be doing anyway).

In a big production with lots of content it is basically inevitable that some ladders (or some animations) will deviate from any agreed on standard: there are lots of ways things can get out of sync. So, in larger games it's common to use inverse kinematic to apply small scale fixes to the positions of hands and feet to make sure they match the actual ladders when the scale is off or if the rungs are unevenly positioned. This makes it possible to re-use the same animation with a wider range of content, but it doesn't magically make the players climb any random collection of rungs realistically -- it just prevents the hands and feet from hovering in mid-air if the relationship between the animation and the model content is off by a bit.

For climbing, particularly, it's possible to do an entirely procedural animation, combining IK for hands and feet with an algorithm to position the player and account for the different distribution of weight between the player's points of contact. This will adapt to any set of hand and foot holds, but it takes a lot of work to make it look as fluid and have as much character as a hand-crafted animation.

