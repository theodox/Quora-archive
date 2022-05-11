# When modelling rooms with Maya, why might it be a good idea to use inches as a unit of measurement instead of centimeters?

	author: Steve Theodore
	written: 2015-01-08
	views: 274
	upvotes: 1
	quora url: /When-modelling-rooms-with-Maya-why-might-it-be-a-good-idea-to-use-inches-as-a-unit-of-measurement-instead-of-centimeters/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you're working with real-world data in inches, it's not a bad idea to use inches: if you've got a drawing that says "this lamp is 7 inches wide and 9 inches high" it's a pain to do the conversion in you head, particularly if the project is large. 

To a lesser degree, it's also not a bad idea to use inches if that's how you think. If you're used to imperial units, you don't need to give them up for Maya's sake.

If you're doing tools or scripts, it is easier to work in centimeters. Maya works in centimeters internally, regardless of what units are displayed in the UI. Some percentage of tools and functions - probably 10-15% - are effectively interpreted as centimeters no matter what your settings are; this causes a lot of confusion for people doing scripts or plugins. For most users however it's not a big problem.

If you're doing physical simulations you should probably stick with metric. The mass values and coefficients are all geared toward metric units, combining those with imperial units is asking for trouble.

If you do use inches or anything other than centimeters you can use the _optionVar_ command to set good default values for your camera clip planes, grid sizes and other UI settings that relate to the unit settings:

[MEL How-To #62](http://ewertb.soundlinker.com/mel/mel.062.php)

