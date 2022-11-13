# What is fps of human eye vision?

	author: Steve Theodore
	written: 2016-01-11
	views: 9848
	upvotes: 16
	quora url: /What-is-fps-of-human-eye-vision/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Eyes aren't digital so they don't have a 'refresh rate'. However most humans can't easily distinguish individual frames at 30 hz.

If you're really attentive you can probably train yourself to see as much as 48 hz, the rate of those high frame rate movies -- back when I was animating all day every day I had a hard time watching film-framerate movies (24 hz) because I felt like I was seeing every damn frame and it gave me a headache. Nowadays I'm in the same bucket with everybody else: pages of python code scroll by a lot slower.

Gamers often think they can see as fast as 60hz ('solid at sixty', as the old tagline goes). However this is rarely an an instance of the actual rendering framerate: more often they are reacting to the latency of the control - > visual feedback loop which is perceptibly better if the entire game is running at 60hz. However if you decouple the render loop from the game and allowed the former to run at 60 and the game to run at 30 or less the experience is generally more like the 30hz game despite the better visuals. Most console games shoot for 30, with some highly competitive titles (particularly shooters and racing games) aiming for 60 at the cost of visual density of quality. PC games often clock much higher nominal frame rates while idling but when the action starts anything besides a glorified arcade game will probably be rate-limited by the physics simulation framerate instead of graphics: that '150 FPS in Crytek' stuff in the boards is mostly about graphics card machismo.

Old style interlaced CRT TVs ran a hair under 60 hz (in NTSC - PAL is slightly different) but they only updated every other scan line in a given frame for an 'average' framerate of just under 30 -- which was chosen precisely because it's where most people's eyes top out.

Interestingly, virtual reality tends to be more frame-rate dependent. Most people are prone to seasickness if you can’t give them a steady 45hz to each eye (which, for rendering purposes, is about the same as 90hz on a conventional screen). That’s why very games usually have simpler visuals — they need to keep the frame rates higher.

As for a 'good game development book' -- well, that's a pretty big field nowadays. Can you updated the question to narrow it down a bit?

