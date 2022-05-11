# How do I position UVs properly to get seamless textures?

	author: Steve Theodore
	written: 2016-07-06
	views: 454
	upvotes: 0
	quora url: /How-do-I-position-UVs-properly-to-get-seamless-textures/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Strictly speaking the answer will always depend on the geometry. Some physical shapes cannot be UV mapped seamlessly, at least not without a lot of stretching: the classic example is a sphere which can only be mapped with either seams or stretches (or more usually both).

In the example picture you can avoid seams by making sure that you use the same texture projection for both sets of faces — in the case, selecting both sets of faces before applying a planar projection will do the trick, although it will change the UVs on the whole object.

If for some reason you can’t change the projection on the house as a whole, you’ll need to re-create the projection of the large wall section and re-apply it to the smaller pieces. If you still have the construction history on the big piece, you can copy the settings from the projection old projection node to a new one. You can also use the Transfer Attributes tool to ‘copy’ the projection from wall to the smaller pieces _if_  the pieces are separate meshes:



If the mesh had shared vertices at the corners of the windows you would not have this problem: you’d have UV you could snap the disjoint pieces to. Ordinarily it’s not a good idea to build the mesh with vertices which look like they are joined but which are not actually connected to the neighboring geometry — this kind of problem is the reason why.

As a practical matter, I’d just select the whole wall (big and small pieces) and apply a new projection - that’s the least complicated way to fix the issue here.

