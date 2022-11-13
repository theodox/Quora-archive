# How do I paint textures on a 3D STL model?

	author: Steve Theodore
	written: 2017-10-31
	views: 1648
	upvotes: 4
	quora url: /How-do-I-paint-textures-on-a-3D-STL-model/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


I like [3d-Coat](https://3dcoat.com/home/) for high-poly mesh painting; it’s primarily a sculpting program but it has painting tools and good tools for dealing with UVs. And, since it’s a high-poly friendly program it also has tools to simplify or retopologize the mesh. If the STL is a scan you may find that cleaning up will make both painting it and working with it in other contexts much easier.

[ZBrush ](http://pixologic.com/)can do pretty much all of the same things, though it’s more precisely focused on the needs of sculpting rather than painting.

Both programs will import STL, but STL files vary widely in quality and adherence to standards. [MeshLab](http://www.meshlab.net/) is a great free tool for fixing up and re-exporting dicey high-density data. If your mesh has vertex colors already (like some scans do) meshlab can manipulate those, but it doesn’t have “painting” tools per se.

