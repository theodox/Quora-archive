# What does game modeler do?

	author: Steve Theodore
	written: 2016-10-24
	views: 918
	upvotes: 4
	quora url: /What-does-game-modeler-do/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The basics are pretty simple: you make 3d models that can be included in the game. In that sense the job is more or less the same as the work done by a CAD modeller, or a modeller working on a film or VFX production. The devil is really in the details when it comes to game modeling. Game engines impose some pretty tight constraints on modeling techniques and tools which other brands of 3d modeler don’t need to worry about.

The most common one is simply simplicity: every vertex in a game model requires some memory and processing power to render; the more of those you need, the slower your game will render. A film or VFX model can be very lavish with modeled details, since the renders are usually going to run on big distributed render farms with thousands of cores. A game model, on the other hand, may need to be rendered sixty times a second on a single PC.

Typically game models also need to work with simpler shading and texturing models. In a film production you can make a complex procedural shader to make make sure that every brick in your brick wall is slightly different from all the others. In a game, you generally can’t afford the runtime processing to make those bricks procedurally at runtime; instead, you’ll need to give the game a texture image which includes a picture of the bricks you’ll be rendering. This is a bit more monotonous, and good game modelers have an arsenal of tricks to disguise this sort of problem.

Since textures are so important to the look of real-time models, game modelers have to be experts and efficient use of [UV space](https://en.wikipedia.org/wiki/UV_mapping). Wrapping a 2-d texture onto a complex shape is a lot like wrapping a toy in gift paper: it demands some compromises and careful planning. CAD modelers rarely need to worry about this; film and VFX modelers can computationally expensive methods for seamless texturing like [Ptex](http://ptex.us/overview.html). But for game modelers, clever use of the 2d-3d relationship is a big key to balancing efficiency and good looking content.

Game modelers also have to worry about gameplay. This could be as simple as making sure that a model hits the right memory budgets, or as complex as making sure that the game engine has a simplified convex hull to test for physics colllsions. Frequently the models will need to be annotated so that the game knows what things are supposed to be made out of : in addition to looking like metal, or wood or concrete a particular bit of the model will need to tell the game engine what substance it is made out of so physics interactions, sounds and effects all work as expcted: things get wacky when your huge metal Death Mech flies away when hit by a bullet because it has the physics properties of balsa wood.

Lastly there’s animation support. Many game models need to be animated, and unlike their film counterparts the math that connects the model to the animations is pretty simple. A modeler needs to work pretty closely with a character rigger and an animator to build geometry that will look good in all the poses that the character has to hit in-game. Otherwise you end up with collapsing elbows, shoulders that twist like candy wrappers, and characters that can’t walk because their proportions are unworkable.

Short answer: it’s a very tricky subset of 3d modeling. Just knowing how to run Max or Maya isn’t the same as being a game modeler.

