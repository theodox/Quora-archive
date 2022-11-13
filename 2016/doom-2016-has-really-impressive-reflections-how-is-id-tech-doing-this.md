# Doom (2016) has really impressive reflections. How is ID Tech doing this?

	author: Steve Theodore
	written: 2016-05-19
	views: 3267
	upvotes: 28
	quora url: /Doom-2016-has-really-impressive-reflections-How-is-ID-Tech-doing-this/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It’s probably [Deferred Screen Space Reflections](https://jackmccallum.wordpress.com/2014/06/07/deferred-screen-space-realtime-reflections/).

A modern renderer generally creates an image in several stages.

![](https://qph.fs.quoracdn.net/main-qimg-7dd6fdd2c3d2061c6ad7f312d8ec3775-c)

_This image from Killzone shows the basics:_ 

_The first ‘buffer’ or picture records the depth of each pixel — how far it is from the camera._ 

_The image at upper right is the orientation or “normal” of each pixel: the XYZ facing of the pixels is encoded into red, green and blue_ 

_The image at the bottom left is the raw color of the objects (you’ll note that it’s not shaded)._ 

_Finally at the lower right there’s a buffer indicating how reflective different pixels are._ 

The renderer uses these buffers to figure out how to shade the image. The strength of the light source depends all 4 values: the amount of light on a pixel depends on distance (depth buffer), angle of incidence (normal buffer), surface roughness (shininess buffer) — then you multiply whatever light is left by the raw color to get a lit, shaded image. The key thing is that they final combination is done using the images — unlike older games the geometry is already ‘gone’ when the image is completed: it’s all being done by operations in the image processing hardware of the GPU, which makes it very fast.

Screen space reflections work in a similar way. For every reflective pixel, you can figure out where the reflected ray wants to go using the normal. You can trace along the line of the new vector using image-based techniques, which are very efficient and very GPU friendly. This technique has been around for a while (i think Crysis was the first AAA title to actually ship with it) but it’s only become widespread with the availability of XB1 - PS4 class hardware.

Screen space reflections are much less accurate than old-fashioned [ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)). In particular, the reflections only work if the reflected ray from the camera to a pixel ends up somewhere in the rendered frame: if the ray reflects _out_  of the frame, you’re out of luck: you won’t see anything behind, above, or below the camera, or any secondary reflections . In those case you fall back to an old fashioned [cube map](https://en.wikipedia.org/wiki/Cube_mapping), just like the bad old days of 2011.

A lot of the hard work comes in disguising the transition from the pretty screen-space reflections to more generic cube maps. The other bit that’s technically interesting is simulating roughness: a mirror pixel needs only a single pixel’s worth of data, but something semi-gloss is effectively averaging a lot of rays for a fuzzier look — doing that right without odd artifacts takes some special work in sampling patterns and so on.

