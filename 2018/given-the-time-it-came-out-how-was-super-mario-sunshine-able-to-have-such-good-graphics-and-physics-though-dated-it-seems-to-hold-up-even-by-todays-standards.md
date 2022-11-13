# Given the time it came out, how was Super Mario Sunshine able to have such good graphics and physics? Though dated, it seems to hold up even by today's standards.

	author: Steve Theodore
	written: 2018-01-14
	views: 16099
	upvotes: 271
	quora url: /Given-the-time-it-came-out-how-was-Super-Mario-Sunshine-able-to-have-such-good-graphics-and-physics-Though-dated-it-seems-to-hold-up-even-by-todays-standards/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


This really doesn’t have much to do with technology. Nintendo has always been very good at the darkest of the dark arts of game design: __picking your battles.__ 

You can boil it down to basic ideas: First, _only do what you can do well;_ second, _make content that shows what you can do well._  These principles only involve technology as a limiting factor — the current tech level gives you a rough boundary for what is possible on a given platform, and the artistry involves finding the most interesting uses of that limited space.

“Mario physics” is a great example. Back in the day Mario games literally didn’t have a “physics engine” in the modern sense at all — _all_  the interactions in the game were managed by game code and not by a general purpose physics solver like [Havok](https://www.havok.com/physics/) ([this article](https://hypertextbook.com/facts/2007/mariogravity.shtml), by the way, is a nice effort to get the history of gravity in Mario games over the years — as you’ll notice, it’s nothing like the ‘real’ value of the gravitational constant!). By contrast no game designer gets to decide exactly what happens when your _World of Tanks_  tank takes a too-steep slope: it’s all up to a generic simulation engine that’s based around standard physic equations. The modern version still is not “real” — designers can and do change the numbers around for the feel they want — but they are tweaking the details of a framework that’s based on completely standardized math. It’s kind of like the difference between drawing on paper and working in photoshop with existing digital images.

Which brings us to graphics. Consider an even more extreme example: Super Mario 64. There was a game that made a lot of smart decisions for the limitations of the day. In 1996 “realistic” was a risky choice for a consumer platformer! This is [Goldeneye](https://en.wikipedia.org/wiki/GoldenEye_007_(1997_video_game)), one of the “best looking” 3d games of ‘96, on the N64:

![](https://qph.fs.quoracdn.net/main-qimg-f019d664c0a42a2245230899913e58ed-c)

Compare it to a shot in a modern espionage game, Metal Gear Solid V:

![](https://qph.fs.quoracdn.net/main-qimg-8443f30acc5751fa5d98b6f9d72709d4)

You can really see where the choice of subject matter imposes some hard, hard limits on what the artists get away with. On the other hand see how much continuity there is in these Marios over time:

![](https://qph.fs.quoracdn.net/main-qimg-115f1b3e882ccec4e883ebc265c832a6)

The tech delta is the same — but the 1996 Mario is still pretty approachable compared to that poor 300 poly Goldeneye dude, because he’s made of simple shapes and bright colors. Neither Mario reacts to light in a photorealistic way (check out the star and the moon — you could almost copy the star over into the 2017 game without it standing out too badly). Cartoony landscapes don’t demand impeccable shadows; cartoon textures can suggest rather than being relying on pixel density and proper sampling - though as an aside there are some levels in SM64 that give most contemporary viewers headaches on a proper emulator, because they have too much sharp pixelly detail on a crisp, noninterlaced modern screen).

In short: SM64 didn’t try to do more than the silicon of 1996 could accomplish; they set their own rules but they played by them with great consistency and panache. Not every genre or game is so lucky: literally nobody in 1996 could have delivered half of Metal Gear V or whatever other photorealistic modern title you care to name. A Nintendo 64 CPU had about 4.6 million transistors — an XboxOneX has 5 _billion_ : it’s literally a thousand times more computing power (and it’s got 20 years of graphics-specific optimizations built in, to boot). A Switch is considerably less powerful — but I’d be surprised if it wasn’t at least 200 times crunchier than the N64.

For _Sunshine_ , specifically, the thing that most people remember and are nostalgic for is the water. In 2002 the water was, literally, like nothing people had ever seen before: if you compare Sunshine’s water to, say, _Blood Wake_  on the Xbox at the same time it looks _astonishing_ . But here again it’s a case of picking battles: in those days the modern graphics pipeline (the “[Unified shader model”](https://en.wikipedia.org/wiki/Unified_shader_model) ) didn’t exist. The old hardware required very close-to-the-metal programming based on good knowledge of the system characteristics; you couldn’t just read the latest SIGGRAPH paper and go. Nintendo clearly banked seriously on the water graphics for Sunshine, because there was no off-the-shelf solution to start from — but, as platform owners, they had all the people who know the best paths to take. It’s probably no accident that this focus just happened to mitigate one of the Gamecube’s biggest liabilities relative to the Xbox and the PS2: texture bandwidth. Big portions of the screen were going to get graphic pizazz from the refraction and reflection effects which were pure math instead of needing to pull lot of pixels from memory fast. Not coincidentally you’ll notice how many of the textures are big and soft and painterly— that means you can pull fewer pixels without looking chunky and pixellated. The other cool effect — washing away the sludge with your FLUDD hose — was also very unique at the time and it was ultimately just a math friendly, texel-light vertex shader.

Like I said - picking battles. Twenty years from now, people will look at some our best efforts today and be amazed that we even tried (think of the whole _Mass Effect Andromeda_  facial animation fiasco, for example, or basically anything virtual reality). On the other hand they’ll probably be playing _Super Mario Hyper Multiverse VR_  and thinking “Mario — what a classic!”

![](https://qph.fs.quoracdn.net/main-qimg-88955bc82133f82792b9f9743f41012d)

_this too will never get old, for different reasons._ 

