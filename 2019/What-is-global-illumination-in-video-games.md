# What is global illumination in video games?

	author: Steve Theodore
	written: 2019-02-16
	views: 1515
	upvotes: 16
	quora url: /What-is-global-illumination-in-video-games/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It’s an illusion.

In the real world, all illumination is handled by only one phenomenon — photons bouncing around or being absorbed (or sometimes, like inside your skin, doing both) . You can simulate these photon behaviors fairly well, mathematically — all of the various forms of ray-tracing or path-tracing do exactly that. Unfortunately, it’s very cumbersome to compute: even a fast ray tracer renders a single image in minutes (or, for complex scenes, hours). A video game needs to produce at least thirty complete images per second, and most games these days shoot for sixty if they can.

So, you need shortcuts. GI is the shortcut that handles indirect illumination or ‘bounce lighting’.

__Lighting basics__ 

The oldest shortcut is what we call _diffuse illumination._ Basically you don’t worry about all the bounces light could take* — you just check the angle between a surface and a light-source and do a simple bit of math and you’re done. This is the lighting you saw in games from the late 90s and the PS2 era.

The next shortcut is what we call _specular illumination_  — essentially, it’s ‘shininess.’ In the real world this is a variant of the kind of reflection you see in a mirror, but on a molecular level. You can fake it, however, checking the angle between the camera, the lightsource and the surface and then adding more or less contrast to the result. This creates moving “shiny” highlights — the sort of thing that started showing up in mainstream games around 15 years ago.

![](https://qph.fs.quoracdn.net/main-qimg-79a50cd609c4d235a40790e7dca01e6e)

_Diffuse (left) and specular (right)_ 

These two methods cover most of what you’re used to seeing in games today. There are shadows (which are a whole separate topic) and “physically based rendering” which is essentially a way to force you to have realistic combinations of specular and diffuse lighting — but basically this is the bedrock of game graphics.

__Light globally, light locally__ 

However both specular and diffuse lighting only cover a single light source and a single object at a time. The whole reason we use them in games is that they break the problem down into simple bits that can be run in isolation at high speed.

Unfortunately, the real world does not work like this.

In the real world, light is bouncing around everywhere. The photons that don’t reach our eyes as highlights don’t just disappear — they hit something else… and something else after that.

We experience that as indirect, or ‘ambient’ lighting that has no obvious single source. It’s not connected to an identifiable source — it’s _global_  illumination, and it affects pretty much everything we see.

Even on the surface of the moon, where there’s no bright sky to provide extra light, shadows are not completely black — in fact, graphics card manufacturer NVIDIA used moon photos to demonstrate the accuracy of their new realtime global illumination technique while poking fun at moon-landing conspiracy theorists:

![](https://qph.fs.quoracdn.net/main-qimg-80cdab4ef5043dbd5ab5706056b12ecd)



_Images: Nvidia corporation_ 

The common nickname for global illumination is ‘bounce lighting,’ which gives a good idea of the role GI plays in a rendered scene. It bleeds color between nearby objects, it softens the hard edges of illuminated areas, and contributes a lot to the visual unity and coherence of a scene.

![](https://qph.fs.quoracdn.net/main-qimg-ef540c2747463dfcceab94b18ad07c28-c)

_Image: Henrik Wann / Stanford_ 

There’s a whole lot more one could say about the subtleties of GI — and about how you make it happen at a reasonable framerate. Most contemporary games do not do realtime GI because it’s still at the outer edges of graphics tech. However, this is what it gives you:

![](https://qph.fs.quoracdn.net/main-qimg-3d928b936adddff215e525b806e2f1fa)

_[State of Decay 2](https://www.stateofdecay.com/age-gate/?r=%2F)_ _— where the interiors are lit only by the moving sun — uses realtime GI. Without it, this scene would be entirely dark except for the sunbeams hitting the floor._ 

The increasing power of GPUs and some new techniques (particularly [voxel-cone-tracing](https://research.nvidia.com/sites/default/files/pubs/2011-09_Interactive-Indirect-Illumination/GIVoxels-pg2011-authors.pdf), a cheat that lets GPUs do something very similar to what those slow old raytracers do) mean it will be pretty standard within a few years.

