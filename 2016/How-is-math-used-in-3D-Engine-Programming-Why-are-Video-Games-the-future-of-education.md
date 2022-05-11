# How is math used in 3D Engine Programming? Why are Video Games the future of education?

	author: Steve Theodore
	written: 2016-05-08
	views: 73
	upvotes: 1
	quora url: /How-is-math-used-in-3D-Engine-Programming-Why-are-Video-Games-the-future-of-education/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The most common application for math in a 3D game engine is for rendering. It uses fairly straightforward linear algebra and a bit of trigonometry. Vectors, dot products, and matrix multiplication are the bulk of what's necessary to render a 3d image on screen. Along with a little bit of trig to handle things like correctly representing perspective, that handles most of what's needed to display the game world. 

Other aspects of an engine are mix of 'programmer math' -- basic calculations like 'how much health does this character have after being hit by dragon breath' -- and more sophisticated techniques. 

The most math-intensive job outside of graphics is realtime physics simulation. The interesting and tricky part is often finding good, stable approximations -- unlike lab physics, a game engine has to process the world in a tiny slice of time and physics calculations depend on a time interval to arrive at the correct results. Thus, if you take too long to calculate the result of a physics interaction correctly your result is wrong: you may have take 1/30th of a second to calculate the portion of a trajectory that should represent 1/60th of a second -- which the player might see in the form of bullet that passes through walls or a character who drops out of the world through the floor. Since physics in particular is trying to simulate continuous phenomena but has to work on discrete time slices, physics-related programming usually draws on calculus.

There are also more exotic jobs which require higher order math skills. For example, while it's not too demanding to render a single frame of a 3d world with nice shading and highlights, many tricks involving signal processing are necessary if you want to avoid the appearance of pixelization, 'jaggies' or high-frequency flickers when the camera or the subjects move.

__[Mathematics for 3D Game Programming and Computer Graphics](http://amzn.to/24BTmAh)__ ____ by Eric Lengyel is a pretty good introduction to the range of math that's involved in generic games tasks. [Advances in Real-Time Rendering in 3D Graphics and Games](http://advances.realtimerendering.com/) is the website which collects papers on game graphics programming and gives good examples of some of the more elaborate techniques.



As for the second part of the question -- while I feel instinctively that games have enormous educational potential, I've been consistently disappointed by most of the efforts I've seen to make educational games. Adding some sound effects or animations to conventional drill-and-kill exercises does not seem to me like a very effective use of the medium.

