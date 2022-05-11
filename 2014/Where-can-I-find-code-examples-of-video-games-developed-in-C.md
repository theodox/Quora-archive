# Where can I find code examples of video games developed in C#?

	author: Steve Theodore
	written: 2014-12-31
	views: 942
	upvotes: 1
	quora url: /Where-can-I-find-code-examples-of-video-games-developed-in-C/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Unity3d is the reigning C# game dev champ. [Microsoft XNA](http://en.wikipedia.org/wiki/Microsoft_XNA) never really took off although I think it is still supported by its own community. 

Before diving in to C# game dev make sure you understand C#'s managed memory system and the tradeoffs that makes between reliability and performance. Some types of games are tough to pull off in C# because managed memory is prone to pauses as unused memory is reclaimed; working around this requires some careful design decisions. The series of articles here: [Gamasutra: Wendelin Reich's Blog](http://www.gamasutra.com/blogs/WendelinReich/20131109/203841/C_Memory_Management_for_Unity_Developers_part_1_of_3.php) is a good place to start even if you don't use Unity

