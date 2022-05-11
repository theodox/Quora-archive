# Why is it so important to close files that have been opened in Python?

	author: Steve Theodore
	written: 2017-02-03
	views: 2049
	upvotes: 4
	quora url: /Why-is-it-so-important-to-close-files-that-have-been-opened-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It’s not really specific to python — depending on the kind of access you’re doing when you crash, you may end up with a file or a network socket that is unusable by other processes if you died with it open.

Try something like this from a python interpreter:

    filehandle = open(“path/to/a/file”, “wt”)
    filehandle.write(99/0)

that will crash and the file you pointed at will not be deletable until you close your python interpreter.

![](https://qph.fs.quoracdn.net/main-qimg-11f0fe08cd9319ec4763bb8f4d46b148)

The typical pattern for dealing with this is to use the `with` context manager, which will guarantee a closure in the event of something going wrong.

    with open(“path/to/a/file”, “wt”) as filehandle:
     filehandle.write(99/0)

That will still crash - but the file will be deletable because the `with` statement will close it out for you

