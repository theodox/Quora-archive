# Which would be more efficient: Animating a single-mesh rigid object (like a gun) with bones, or breaking up each moving object and animate via pivot points?

	author: Steve Theodore
	written: 2017-12-06
	views: 350
	upvotes: 3
	quora url: /Which-would-be-more-efficient-Animating-a-single-mesh-rigid-object-like-a-gun-with-bones-or-breaking-up-each-moving-object-and-animate-via-pivot-points/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you don’t need the object to deform, it’s usually simpler just to model the moving parts as separate objects and animate them directly. A gun with a working trigger, slide and so on is a good example of a non-deforming object that doesn’t need bones.

If you decide you need the minor extra features of bones — such as rotation offset or joint orients — you can parent the meshes to bone objects. just make sure to lock the local transforms of the meshes if you do that so there’s no ambiguity about where the motion is coming from.

