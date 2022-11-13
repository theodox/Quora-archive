# Is particle system composed of many mesh?

	author: Steve Theodore
	written: 2016-01-31
	views: 254
	upvotes: 4
	quora url: /Is-particle-system-composed-of-many-mesh/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


A particle system, strictly speaking, is independent of the way it will be rendered. Particles are just an extremely simple unit of work for some kind of calculation. 

The particles can be rendered with conventional quads but they don't have to be. Maya and Houdini both have software particle renderers which don't use OGL or DX. And many games use instanced geometry particles for things which look better as meshes. 

Most of the time particles are used for phenomena which are amorphous or fluid. It's far easier to draw a lot of vague water droplet sprites than to model the ever changing form of a waterfall. A lot of the art in particle system design is finding the set of particle behaviors -- the motions, reactions and spawn patterns -- which match the situation best. 

