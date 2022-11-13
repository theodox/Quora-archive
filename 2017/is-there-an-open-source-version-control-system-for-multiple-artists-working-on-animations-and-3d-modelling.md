# Is there an open source version control system for multiple artists working on animations and 3D modelling?

	author: Steve Theodore
	written: 2017-12-03
	views: 1265
	upvotes: 0
	quora url: /Is-there-an-open-source-version-control-system-for-multiple-artists-working-on-animations-and-3D-modelling/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You might be able to get by with [Git Large File Storage](https://git-lfs.github.com/), which allows git to deal with large(ish) binary files. However distributed solutions like git and svn are designed by and for programmers — their virtues are really important for people working with text files but big binaries (models, animations, textures and movies) benefit very little from the typical DVCS.

[TACTIC Open Source ](http://www.southpawtech.com/tactic-open-source/)is an open-source production management system that might work; it’s Hollywood style so it’s naming convention heavy (filename_001.ma sort of thing) rather than relying on updating files in place.

