# Unity (Game Engine): 

	author: Steve Theodore
	written: 2015-01-04
	views: 708
	upvotes: 0
	quora url: /Unity-Game-Engine-Which-is-Right-Way-to-Add-Joystick-in-Unity3d-Adding-on-Scene-Directly-or-Initiating-it-From-Player-Scripts/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Unless you are reprocessing the input in some unusual way, it's most common to just use the [Input](http://docs.unity3d.com/ScriptReference/Input.html) class directly in different places. It's a service provided by the underlying (C++) game engine so you aren't creating new objects or otherwise costing performance hits by accessing it. 

If you have to do something special - say, you've got a complex way of remapping joystick input from the basic deadzone/scale methods in the[ Input Manager](http://docs.unity3d.com/Manual/class-InputManager.html), you might want to create a special manager object so that all of your scripts can access your remapped values the same way. This might also be good if you have a custom connection to a non-standard input device. 

However the Input/InputManager combination is the safe and reliable version, since it needs the least setup and is easy to configure.

