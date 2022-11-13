# Why don't big game companies use Unity for their game development?

	author: Steve Theodore
	written: 2015-08-30
	views: 428591
	upvotes: 1084
	quora url: /Why-dont-big-game-companies-use-Unity-for-their-game-development/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


On the practical side, Unity's architecture has two critical problems for building big games.

On the tech side, Unity's core engine is C++ but the bulk of Unity games are written in C# or Unity's JavaScript-alike UnityScript. C# handles memory allocation and de-allocation for you, which is a boon for mere mortals who don't want to worry about mis-counting a pointer and blue-screening somebody's PC. However the automatic memory system (known as the [garbage collector](http://www.gamasutra.com/blogs/WendelinReich/20131109/203841/C_Memory_Management_for_Unity_Developers_part_1_of_3.php)) has a nasty habit of kicking in when it feels like it, introducing unpredictable pauses (occasionally measuring in seconds, rather than milliseconds). In an action genre like FPS, racing or sports that's an eternity. You can avoid the worst by careful planning and a conservative use of assets - but that's definitely a dis-incentive for teams planning big games in the sense of large, expensive assets.

Moreover C# is not as fast as the C++ used in other game engines like Unreal. Real numbers are hard to come by because they are very situational, but C++ is somewhere between 15% and 50% faster than C#. For many applications that doesn't make a difference: but for a bleeding edge title it's pretty significant.

On the production side, Unity requires that every developer locally recompile all of the assets and all of the game code. If you come back to the office after a week's vacation and grab the latest data for your game from source control, you may be waiting quite a long time for Unity to recompile the assets and the code. Unity's been [been working on that for a while](http://docs.unity3d.com/Manual/CacheServer.html) but the results are still not really acceptable for games with really big asset bases (if nothing else, when you've got a team of 150 working on your game and they all lose an hour a day to build times, you're effectively losing _one person-month of work every day!)_ Since Unity's architecture isn't really designed around centralized build farms or pre-cooked assets it's not a natural fit for big teams with lots of assets.

Also, Unity has only lately started playing nice with professional asset control systems like Perforce, which are the backbone of asset management in big game projects. Perforce support only came on line in 2013 and it's still a little wonky. The .meta files that Unity uses to track asset state over time are also notoriously difficult for collaborators. Plus Unity's preferred method of importing assets (keep your raw model files and textures inside the Unity project) is really unworkable for large projects where random junk like extra Photoshop layers, reference models, and test content show up all the time.

TLDR: Unity is a great engine, but it evolved out of a community focused on small teams and small projects. It's still finding its way when it comes to heavy-iron performance and big asset collections. It may catch up but it will take a while.

