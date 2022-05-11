# How do you view the console/output window for Maya when running it on a Mac. It is useful to debug startup scripts?

	author: Steve Theodore
	written: 2019-02-01
	views: 404
	upvotes: 0
	quora url: /How-do-you-view-the-console-output-window-for-Maya-when-running-it-on-a-Mac-It-is-useful-to-debug-startup-scripts/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There’s no output window on the OSX version. If you launch Maya from a terminal window you will get the same printouts in your terminal that a windows user gets in the output window.

In any case, only very early stage debug info goes to the output window: you can’t get to it from MEL, at least I don’t believe you can, and to write to the output window or the OSX terminal you need to do something like:

    import sys
    script_listener = sys.stdout
    terminal = sys.__stdout__ #note underscore!
    script_listener.write (“hello listener\n”)
    terminal.write(“hello terminal\n”

sys.__stdout__ is the ‘real’ system stdout; Maya replaces it with a standin which redirects print() to the script listener.

If your users are not running Maya from a command line, just log your debugging using the standard Python logging module and either a file or the listener.

