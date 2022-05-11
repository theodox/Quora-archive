# Real Time Rendering: 

	author: Steve Theodore
	written: 2015-08-30
	views: 958
	upvotes: 8
	quora url: /Real-Time-Rendering-Wouldnt-a-triangular-polygon-be-more-efficient-than-a-quad-polygon-for-displaying-things-like-grass/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


This is one of those super tweaky things which relates to the nature of the hardware. It's a good example of how our usual intuitions really break down in the bizarro world of GPU hardware, which is designed for massive parallel operations instead of the linear ones we know so well from ordinary computing.

A quad isn't really twice as expensive as a triangle: it's usually only 33% more. The usual way you'd send the quad to the GPU is as an a set of 4 vertices and 4 indices; the second triangle involves only one extra index because the hardware knows to look for this arrangement:



![](https://qph.fs.quoracdn.net/main-qimg-ed2a4e22aacc69c83c9b46f41b951cd6)

_(not a square, but you get the idea)_ 

The main reason that quads are better, though, is _overdraw._  Some hardware -- particularly graphics chips like the PowerVR set commonly found in older mobile devices -- is limited by the ability of the rasterizer to push pixels to the screen. Unfortunately this includes the 'empty' pixels around, say, a transparent sprite. On that kind of hardware it makes sense to use a more detailed set of triangles to approximate the rendered shape more closely, using more vertices and fewer transparent pixels: otherwise you have to rasterize a very big triangle with lots of waste space to get the same image on screen. For most sprites the overdraw costs more than outweigh the trivial cost of that extra vertex / index pair. 

The other issue is batching. In most cases the data going from the game to the GPU (or between the different stages of the shader pipeline) is batched up into bundles of a fixed size. In most cases there's really no difference in memory or performance cost between sending a single item and a whole batch (although adding an extra batch because you add one trivial item is a common, and very frustrating problem: on the PS3, for example, skinning 73 vertices used to cost 2X as much as skinning 72 for this reason!) Quads in particular are so far below the typical batch sizes that there's a good chance that there's literally no difference at all between sending a triangle and sending a quad.

