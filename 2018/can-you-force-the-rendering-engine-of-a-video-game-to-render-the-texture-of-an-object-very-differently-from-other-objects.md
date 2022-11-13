# Can you force the rendering engine of a video game to render the texture of an object very differently from other objects?

	author: Steve Theodore
	written: 2018-04-02
	views: 917
	upvotes: 6
	quora url: /Can-you-force-the-rendering-engine-of-a-video-game-to-render-the-texture-of-an-object-very-differently-from-other-objects/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Yes. This is the whole job of shaders, which are micro-programs inside the rendering engine that control the final appearance of rendered objects. Most shaders are efforts to create a pseudo-realistic result, modeling the behavior of light and various kinds of materials. However, shaders can do pretty much anything else too: cartoon-style flat shading, matrix -style text crawl effects, or just plain psychedelia. Textures are just one one of the many factors that a shader can use to create visual results, although they are one of the most common.

The best introduction to the huge range of what shaders can do is the website [Shadertoy](https://www.shadertoy.com/), which showcases the incredible variety of effects that are possible. Unfortunately Quora won’t run their samples inline inside and answer, but here are a few images to give you an idea of how varied the results can be (click on the links below to see the shaders running live in 3d):

![](https://qph.fs.quoracdn.net/main-qimg-cea262855b4cc5aa99c09c2d44b79e27)

by [Flyguy](https://www.shadertoy.com/view/4lsSzX)

![](https://qph.fs.quoracdn.net/main-qimg-c31f07241b8850d085afd61430203ae4)

by [mrx](https://www.shadertoy.com/view/MlfGR4)

![](https://qph.fs.quoracdn.net/main-qimg-e767337c8a434dea251b96f3fdfa4068)

by [xt95](https://www.shadertoy.com/view/MdX3zr)

![](https://qph.fs.quoracdn.net/main-qimg-6a1245bcfc86ddc7e353c55266d5571b)

by [fizzler](https://www.shadertoy.com/view/lt2fD3)

![](https://qph.fs.quoracdn.net/main-qimg-8362e937f3bf26df33808a6f2f0cb107)

by [Candycat](https://www.shadertoy.com/view/MscSzf)

