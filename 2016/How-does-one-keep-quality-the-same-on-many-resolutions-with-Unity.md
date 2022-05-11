# How does one keep quality the same on many resolutions with Unity?

	author: Steve Theodore
	written: 2016-11-23
	views: 1162
	upvotes: 4
	quora url: /How-does-one-keep-quality-the-same-on-many-resolutions-with-Unity/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you’re really, really worried about image quality, you’ll probably need to provide separate assets for each target platform. It’s annoying but it works.

Scaling images up never looks very good: you’re trying to fake information you don’t have. Scaling images down works better, so in a pinch you should author bitmaps for the largest resolution and let the hardware scale them down rather than up. However hardware downscaling usually does not look that good either - at least, it’s rarely competitive with what you’d get from doing the same thing in Photoshop.

The best results will always come from importing your vectors to exactly the pixel resolution you want. The next-best would be to downsize an original image in Photoshop, which uses more sophisticated filtering and will look better than the same downsize done on the graphics card. (hint: “Bicubic sharper” and the “unsharp mask” filter are your friends!).

Unfortunately, Unity does not provide a simple one-shot method for saying ‘use this bitmap on PC and that on IOS’ or the equivalent: you can customize compression and color depth settings per output platform but Unity prefers to thing there’s only one asset and the platform-specific customizations are just settings changes. It’s not however very hard to write scripts which pick the appropriate asset based on [#ifdefs](https://docs.unity3d.com/Manual/PlatformDependentCompilation.html) and apply it at startup time.

Also on the downside, multiple custom assets will make your built games bigger. There used to be a plugin for picking platform-specific assets but it’s out of the Unity Marketplace nowadays — there may be a replacement in there somewhere however.

More detail, in a programmery way, [here](http://www.badlogicgames.com/wordpress/?p=1403).

