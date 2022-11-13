# Why does no one add built in graphics support to C++ given it's age and widespread use in game development?

	author: Steve Theodore
	written: 2017-09-07
	views: 376
	upvotes: 5
	quora url: /Why-does-no-one-add-built-in-graphics-support-to-C++-given-its-age-and-widespread-use-in-game-development/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Built in graphics is not appropriate for first-class language feature: it’s too dependent on hardware, and thus also on drivers. You don’t want to add something to the core language that won’t run without lots of prerequisites. — and what would all of that stuff do when compiled for, say, an ARM phone versus a PC with a dual-SLI graphics card vs a rack-mount server with no display at all? It’s easier and simpler and more flexible to leave graphics where they are, as APIs that can be linked into C++ programs when needed.

There are dedicated high level languages like HLSL and GLSL for graphics. Because they target different hardware, they have compilers and toolchains dedicated to turning human readable instructions like

     OUT.Color = diffuse*diffuseMaterial + specular*specularMaterial;

into all of the register movement that actually happens on the GPU. But those tools are big and sophisticated — and not that closely related to the things that make a good C++ compiler. Adding them to C++ directly would make the language ecosystem even messier than it already is.

