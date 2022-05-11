# Are CPU cores important for 3D animations such as Autodesk Maya?

	author: Steve Theodore
	written: 2016-10-19
	views: 3385
	upvotes: 2
	quora url: /Are-CPU-cores-important-for-3D-animations-such-as-Autodesk-Maya/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Less than they should be — Maya is quite imperfectly multicore. Most — not all — rendering will benefit from more cores but modeling and animation in Maya do not get nearly as much oomph as you’d hope from extra cpus. The late, lamented SoftImage|XSI was very good about this. Maya’s been working on it for a while but it’s not there yet.

Lots of gory tech details here: [http://download.autodesk.com/us/company/files/2016/UsingParallelMaya.pdf](http://download.autodesk.com/us/company/files/2016/UsingParallelMaya.pdf)

