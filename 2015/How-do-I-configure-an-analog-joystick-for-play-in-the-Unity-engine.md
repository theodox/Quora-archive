# How do I configure an analog joystick for play in the Unity engine?

	author: Steve Theodore
	written: 2015-05-23
	views: 780
	upvotes: 0
	quora url: /How-do-I-configure-an-analog-joystick-for-play-in-the-Unity-engine/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The input manager provides a mapping between the joystick or other controllers and named axis values. It's where you want to adjust things like sensitivity and deadzones as well as assigning names to stick directions or buttons. You don't need to make a component for the input manager, it's always available in any script you right.

In other scripts you'll use Input.GetAxis() to react to the data that comes out of the input manager:

