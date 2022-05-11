# What are the standard pipelines to create a mesh model of an object from its multi-view sequence?

	author: Steve Theodore
	written: 2015-03-21
	views: 198
	upvotes: 2
	quora url: /What-are-the-standard-pipelines-to-create-a-mesh-model-of-an-object-from-its-multi-view-sequence/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Most mesh reconstructions techniques involve some arbitrary cleanup and noise removal as well, these are frequently proprietary. The "right" output differs for different applications -- a model that's suitable for use in VFX production might not be equally good for mechanical reconstruction, for example.

You might try to voxelize the point cloud by quantizing the sample points into a fixed resolution 3-d grid and using a marching cubes algorithm to resurface the mesh; this would have some desirable properties (in particular, it would work well with a mesh based decimation algorithm and you could also determine watertightness very easily. However it would be lossy.

There are a bunch of techniques in the docs at [Point Cloud Library (PCL)](http://pointclouds.org/documentation/tutorials/voxel_grid.php)

