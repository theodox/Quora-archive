# What appropriate renderer libraries for learning computer graphics?

	author: Steve Theodore
	written: 2016-02-14
	views: 158
	upvotes: 0
	quora url: /What-appropriate-renderer-libraries-for-learning-computer-graphics/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The twin standards are DirectX (using [HLSL](https://msdn.microsoft.com/en-us/library/windows/desktop/bb509561(v=vs.85).aspx) or something close to it) and OpenGL using [GLSL](http://nehe.gamedev.net/article/glsl_an_introduction/25007/). They are very similar for most purposes; if you're on Windows it will be slightly easier to go with DirectX and if you're on Linux or Mac the OGL is easier. Both of these are designed as optimizable specialty languages for driving graphics hardware, so they aren't quite the same as traditional programming languages. The third runner up is [Cg,](https://en.wikipedia.org/wiki/Cg_(programming_language)) which is pretty much orphaned nowadays but is also extremely similar to the previous two. They're all basically flavors of C with extensions for handling the vector-heavy 3d math of graphics hardware.

If you'd rather stick with a more linear programming style you might want to investigate [Renderman](https://renderman.pixar.com/resources/current/RenderMan/home.html) which isn't as closely tied to the peculiarities of graphics cards. Software rendering in general is more flexible and more powerful than the hardware variety -- for example, its how usually how you would do global illumination or raytracing -- but it's slower because it doesn't use special acceleration hardware (there used to be special RenderMan boards back in the 90's but AFAIK there aren't any specific ones today: the rise of massively parallel chipsets created a new genre).




To get started, you can just write an app including any of the above APIs and start coding. However there's a bunch of extra work which you'll need to do -- like reading textures and managing app lifecycle -- that its not part of the rendering system. If you want to skip all that you might also consider the [Unity Game Engine](https://unity3d.com/) as a test bed; it includes a very CG-like shading language with the positive addition of providing all the application shell you'll need so you can focus on the shader math and not on writing a windowed application to display your stuff. 

[mental mill ](https://forum.nvidia-arc.com/showthread.php?12284-mental-mill-1-2-release-and-download)-- if it's still supported, I'm not sure -- is another environment where you can focus on shader work and not have to write your own framework.

[Processing](https://processing.org/) is another good environment for playing around with all aspects of 3d coding and -- I think! -- allows you to do rendering work without being too tied to the hardware.

 Last but not least you can try [three.js](http://threejs.org/), a Javascript library for working with WebGL, a subset of OpenGL -- it has the big advantage of being interactive and not needing a full app shell. If Javascript bothers you there's also [VPython](http://vpython.org/) which does an analogous job in Python.

 

