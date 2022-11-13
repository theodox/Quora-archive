# Is it best to rig and animate a 3d character for export to Unity3d in an external app, or can the rigging and animation be done in Unity?

	author: Steve Theodore
	written: 2015-11-09
	views: 2055
	upvotes: 4
	quora url: /Is-it-best-to-rig-and-animate-a-3d-character-for-export-to-Unity3d-in-an-external-app-or-can-the-rigging-and-animation-be-done-in-Unity/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You really want to use an animation package for creating the content and Unity for playing it back and stitching it together. Unity is an essential part because the player's experience of the animations will be heavily influenced by how well and smoothly you transition between different animations as the game plays. However the fine detail work of weighting skins, creating animator controls, and above all keyframing whole characters should really be done in an animation centric tool (*cough* Maya *cough*). 

 There's 20 years of accumulated experience in character animation baked into the UI of animation packages that isn't really there in Unity -- adding it would take both the experience of a rigger and pretty serious programming chops.

