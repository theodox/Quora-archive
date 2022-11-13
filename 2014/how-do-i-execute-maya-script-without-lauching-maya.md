# How do I execute Maya script without lauching Maya?

	author: Steve Theodore
	written: 2014-12-19
	views: 9974
	upvotes: 2
	quora url: /How-do-I-execute-Maya-script-without-lauching-Maya/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You can do it from standalone as well - you'll need to make sure that the standalone sets up any plugins or other paths that you need correctly (although ordinarily starting a standalone will run the same userSetup. py or userSetup.mel that youd get in the GUI version of maya.)

It also helps if you run your standalone using the Mayapy.exe that comes with Maya - it's a regular python interpreter but it is preconfigured with access to the paths you need for Maya to run. Running standalone in another python interpreter might not leave you set up with the right system paths.

If you start MayaPy with these flags, you'll have an interactive session that you can use to test out your ideas:

mayapy.exe -i -c "import maya.standalone; maya.standalone.initialize()"

Once you have a script that works, you can run it with

mayapy.exe "your_script_here.py"

Just make sure the script imports standalone and calls standalone.initialize() at the top

This stackoverflow post goes into more detail:
[use external python script to open maya and run another script inside maya](http://stackoverflow.com/questions/27437733/use-external-python-script-to-open-maya-and-run-another-script-inside-maya)

And this blog posts includes some example code for starting up standalones with different environments:
[Multiple MayaPy Management Mania](http://techartsurvival.blogspot.com/2014/05/what-happens-at-startup.html)

