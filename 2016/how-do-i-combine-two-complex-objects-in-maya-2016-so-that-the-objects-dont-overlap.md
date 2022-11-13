# How do I combine two complex objects in MAYA 2016 so that the objects don't overlap?

	author: Steve Theodore
	written: 2016-11-13
	views: 1652
	upvotes: 1
	quora url: /How-do-I-combine-two-complex-objects-in-MAYA-2016-so-that-the-objects-dont-overlap/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You might be able to do this with boolean operations. Maya bools are less than perfect, especially with data this dense, but it should work if you do the operations one at a time and delete construction history after each one.

Another route would be to try [MeshLab](http://meshlab.sourceforge.net). It is not the worlds most user friendly software, but (a) it does a pretty good job with dense data and (b) it's free so the cost of experimenting is low.

