# What is a pixel shader?

	author: Steve Theodore
	written: 2017-06-06
	views: 689
	upvotes: 1
	quora url: /What-is-a-pixel-shader/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Shaders are specialized programs used by graphics hardware to produce images. They’re usually subdivided into smaller programs which handle different aspects of the hardware rendering process.

![](https://qph.fs.quoracdn.net/main-qimg-44d4637046b06a35b91b11a4feece6e0)

There are several different varieties but the most common ones are __pixel__  and __vertex__  shaders.

The vertex shader is responsible for applying any changes to input geometry. Usually that means projecting 3-d geometry onto the 2-d projection plane of the output image, but sometimes you might add some kind of procedural motion or deformation to the geometry here as well.

The pixel shader takes the output of the vertex shader and generates the pixels that will show up in the final image. Most of the time this is based on some variation of the [rendering equation](https://en.wikipedia.org/wiki/Rendering_equation), comparing the facing direction of the pixel with the directions of light sources and the properties of the surface, but could be anything from a random noise function to a complex simulation or raytracing.

The part of this that’s most different from ordinary programming is that both vertex and pixel shaders are _extremely_  parallelized. Each vertex shader will run on every vertex in the input data at the same time; each pixel shader will run on every pixel in the final image at the same time. That means it’s hard to do something to one pixel based on the state of another — all the pixels will be running at the same time independently of each other. Effects that need to be aware of context often have to run multiple pixels shaders one after another, storing the results into temporary images.

This gives you a decent, very basic overview of how it works:



