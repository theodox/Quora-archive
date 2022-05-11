# Why are clipping bugs still so common in video games?

	author: Steve Theodore
	written: 2016-01-27
	views: 47049
	upvotes: 1212
	quora url: /Why-are-clipping-bugs-still-so-common-in-video-games/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Collision checking in game physics is pretty computationally expensive. The expense of the checks scales pretty much linearly with the complexity of the geometry: checking to see if a point is inside or outside of a cube is (more or less) six times as expensive as seeing if it lies above or below a single plane. So almost always the physics representation of the object is much simpler and cruder than the visual representation: Here's an example of some of the different ways you might represent the collision of an odd shape:

![](https://qph.fs.quoracdn.net/main-qimg-45527f84bdb902c4eecca5738b8500ee)

The sphere is very cheap: you just check the distance from a point to the center of the sphere. The cube involves 6 checks. The simple hull (3rd from the left) involves a few dozen. The accurate hull probably involves at least 60. All of that is sucking up CPU time you might want elsewhere.

And of course, if you wanted to check a strand of hair realistically, you'd also have to subdivide it into lots of short linear segments and check them all individually as well. Again, that's all CPU cycles you could be spending on more responsive vehicle controls or smarter AI.

Lastly: in the case of characters, particularly, it's pretty common to skip the self-intersection checks altogether. Instead you rely on the animators to supply poses and animations which don't produce bad visual results. However the animators are often working on a generic model with different equipment — or even different proportions! — than you might see at a particular time. They do their best, but frequently they don't know what combination of hair, equipment, and clothing will actually be used in any particular moment in the game. We generally accept a little bit of slop — some clipping, some mismatch between the gesture and the implied weight of their outfit, and maybe some artifacts that happen when different animations are blended together.

