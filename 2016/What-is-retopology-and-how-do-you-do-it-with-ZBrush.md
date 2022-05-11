# What is retopology, and how do you do it with ZBrush?

	author: Steve Theodore
	written: 2016-01-26
	views: 15335
	upvotes: 15
	quora url: /What-is-retopology-and-how-do-you-do-it-with-ZBrush/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Retopologizing is re-building an existing mesh with (more or less) the same volume and shape but with a different mesh layout. Especially when working in a sculpting program like Zbrush, the underlying 'grain' of the mesh matters a lot for the quality of the result: you want the edges in the mesh to flow as much as possible with the contours of the mesh. You also want to control the density of the subdivisions so you have more edges where you need detail or special animation deformations, and fewer edges in simpler areas. Retopology is also a good way to simplify and clean up noisy data, such as 3d scans. 

Good topology is also very important for animation, since it will strongly affect the way a model can animate: poorly placed vertices and edges will make life much harder for animators and riggers.

![](https://qph.fs.quoracdn.net/main-qimg-c5a7e22dabb461ecf55bc4a9fa114555-c)

 _The edge flow in a clean model reflects the visual flow of contours in a mesh_ 

![](https://qph.fs.quoracdn.net/main-qimg-16567f74cf3e59b82be6123eebbdd7b4)

_A messy original mesh with badly flowing edge loops (left) and the same mesh with good topology (right). Note how much many fewer faceting artifacts you see, despite the much lower density on the right._ 

Most sculptors find that they iteratively re-build the mesh as they sculpt -- they'll work for a while, look for problems, and then re-flow the topology around a problem area as they hit problems or add more details. Until quite recently this was a pretty big pain in the butt, since you're basically put re-modeling the mesh on the fly. However modern tools have made it much less of a problem. 

The most popular workflow these days is probably to use [ZRemesher ](http://docs.pixologic.com/user-guide/3d-modeling/topology/zremesher/)ZRemesher allows you to essentially draw the mesh flow you want and project it onto your existing mesh. It's not going to fix all your problems for you but it's a huge, huge leap forward from where things were 5 years ago. Good video intro here:





Another great, under-utilized tool for retopo is [3DCoat, ](http://3dcoat.com/home/)which is similar to ZBrush but voxel rather than Mesh based. It does a good job of intuiting decent toplogy for you:





