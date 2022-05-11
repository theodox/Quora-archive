# How do I model this portion in SketchUp?

	author: Steve Theodore
	written: 2015-11-10
	views: 770
	upvotes: 5
	quora url: /How-do-I-model-this-portion-in-SketchUp/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


That looks a little heavy for Sketchup, which is really great for architectural forms but isn't a great free-form modeller. 

If you can get your hands on a student copy of [3ds Max](http://www.autodesk.com/education/free-software/3ds-max) or [Maya](http://www.autodesk.com/education/free-software/maya) those will be able to handle these kinds of details better; [Blender](http://www.blender.org/) is free and could handle it as well, though the UI is a bit less refined.

 Trying to recreate the exact winding in the model will be very time consuming and hard to work with, If this was my project I'd use lofts or extrusions to create a few overlapping ribbons representing each of the major windings of the rope. If you generate those surface with NURBS curves and loft along them, the surfaces will have texture coordinates along their length so you can apply texture maps (either photographic or maybe generated a program like Zbrush so you have coordinated color, transparency and normal maps). A couple of layers of these textured ribbons will give a pretty good approximation of the dense windings in the photo. You can top it off with a few strands of completely extruded rope to do the dangling bits and provide more 3-d relief.

Here's an extremely crude example of a lofted NURBS surface, cloned and distorted a couple of times, with a generic rope-y texture -- it would work a lot better with a bump map. I did this on a laptop with a trackpad so it is only a very rough example of that you could do with some real work. With a handful of fully extruded ropes over this you can create a pretty decent illusion of complexity without managing a very heavy model. 



![](https://qph.fs.quoracdn.net/main-qimg-90cf1aef432614e3acead5caf8fa5d64)

