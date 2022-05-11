# How do I write something like this in a command line using Python, etc.? Is there any tool for this?

	author: Steve Theodore
	written: 2015-08-16
	views: 3550
	upvotes: 4
	quora url: /How-do-I-write-something-like-this-in-a-command-line-using-Python-etc-Is-there-any-tool-for-this/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you just need to display colored text in a python interpreter, you can simply print using the right [terminal escape codes (ANSI/VT100)](http://wiki.bash-hackers.org/scripting/terminalcodes) for your terminal. For example in the OSX terminal you can type something like this:



    print "\033[38;5;2mHello World\033[0m" 



Which should give you something like 



![](https://qph.fs.quoracdn.net/main-qimg-a7a6a91d6cfda85afeb80c4018e393d0)


The actual colors you see, unfortunately, depend on the settings in your terminal app: most terminals support '16 colors' but _which_  16 colors is generally set by the user. Some systems allow you to set colors explicitly in your escape codes and will try to match the colors you've asked for as closely as possible from their limited palette, but in most cases you only provide indexes.

For some more background on using escape codes in python, try [this blog post](http://techartsurvival.blogspot.com/2015/04/blockquote-background-f9f9f9-border_12.html); although it's intended for people using Maya with a terminal emulator most of it will be the same for any general-purpose python running in a colored terminal window on Linux or OSX (or in ConEmu or Terminal2 on windows).

The actual set of codes which works varies from on terminal to another. Color is supported by almost all terminals; other features (graphics blocks, bell sounds, clears and animation for example) are less likely to be universally available.

