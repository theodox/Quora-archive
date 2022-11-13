# What skill are involved in Procedural Modeling of Building?

	author: Steve Theodore
	written: 2015-11-21
	views: 931
	upvotes: 5
	quora url: /What-skill-are-involved-in-Procedural-Modeling-of-Building/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There are several different skill sets involved in this kind of project (which is why you rarely see a big finished example coming from a single individual).

On the technical side you need:

__A good understanding of how 3d geometry is constructed.__  You need to understand enough about how primitive shapes (cubes, cylinders and so on ) can be combined to create complex architectural forms. If you're doing realistic modern buildings instead of sci-fi or fantasy this almost always means you'll need to understand [Constructive solid geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry)



![](https://qph.fs.quoracdn.net/main-qimg-23066c444ff3d7648c4d0030544de174-c)

 
This will generally be somewhat easier in Houdini, but it's possible in both packages.

You'll also need to understand __how textures are applied to the models__ , which (especially for realistic shapes) can be complicated. Many procedural city modeler just project photographs onto the models -- which works pretty well for blocky shapes on city-sized models -- and others attempt to generate [UV mapping](https://en.wikipedia.org/wiki/UV_mapping) that will follow surface contours. This allows for more complex effects (such as a decoration that correctly follows the shape of an arch) but is much more complex. Procedural textures can make it easier to avoid all the problems of generating good projections (both Maya and Houdini have good tools for combining different noise functions and hand-made textures, tools like [Substance Designer](https://www.allegorithmic.com/products/substance-designer) can also make this easier. The complexity of this part depends very much on what scale you're working on: doing a decent job on a rough city-sized model is easier than doing a really tight job on a single detailed building. 



![](https://qph.fs.quoracdn.net/main-qimg-136c8ad340526ffad6e9435476188b24-c)


_procedural textures are often a good complement to procedural models_ 

To put this all together, you need to know about __procedural generation__ : the art of creating the rule sets which guide the creation of a building from a set of instructions. The actual implementation is pretty complex but the idea is fairly simple: something like



Create a footprint for the building of some random size (between a reasonable minimum and maximum)

Assign a 'front' face and maybe a 'back' face (this might depend on location: a building in a suburban office park may not have 'back' but one in a city might have very different looks on the front and back.

Decide how many floors (this may relate to location, and also the footprint size, and other factors)

Generate a first floor. Usually this involves dividing the sides into a set of 'cells' which will represent windows and/or doors. (This may require special rules for a main entrance or street side windows)

Generate second and higher floors. This will be similar to the rules for the first floor but won't have a big entrance. Higher floors might have balconies (and these might happen on alternating floors or above a certain height and so on).

Add some kind of rules for rooftop items like elevator wells and HVAC


This is a big and complex topic -- it's easy to get something simple up and running ( [this Three.js example](http://learningthreejs.com/blog/2013/08/02/how-to-do-a-procedural-city-in-100lines/) is only 100 lines!) but getting an algorithm that realistically creates dozens or hundreds of buildings without oddball results is much harder. 
 Here's a decent collection links: [Procedural Content Generation Wiki](http://pcg.wikidot.com/category-pcg-algorithms). This one covers cities, rather than buildings: [gamesitb.com](http://gamesitb.com/SurveyProcedural.pdf).
Lastly -- but not least -- you need some decent __knowledge of art history and architecture.__  Not enough to teach a course - but enough to know when your algorithm is generating things which don't really mimic the styles and behaviors of real-world buildings. Many procedural-architecture programs fail this test.

I believe you can get a free trial version of [Esri CityEngine](http://www.esri.com/software/cityengine)., which will give you a good look at what a top-caliber procedural system looks like.

