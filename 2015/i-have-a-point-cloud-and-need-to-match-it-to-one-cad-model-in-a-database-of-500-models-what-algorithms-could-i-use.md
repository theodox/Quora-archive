# I have a point cloud and need to match it to one CAD model in a database of ~500 models. What algorithms could I use?

	author: Steve Theodore
	written: 2015-01-26
	views: 661
	upvotes: 2
	quora url: /I-have-a-point-cloud-and-need-to-match-it-to-one-CAD-model-in-a-database-of-500-models-What-algorithms-could-I-use/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You probably want to do a multi-pass search, since bulk comparisons are going to be very slow. At each pass, you want to find a way to create a hash for all of the geometric objects and check the hashes (rather than doing millions of vert-to-vert comparisons). 

Bounding boxes would make an obvious first pass, you can quantize the bounding box values to some given tolerance to account for float epsilons, etc. You should probably translate all the bounding boxes so they share common minima (ie, the least corner of the bounding boxes should all be (0,0,0). 

However, if you don't know that your point cloud is aligned with the models, however, you cant' use bounding boxes -- see the next step.

In a second pass, if you have more than one hit you'll need to create new hashes. If your point cloud comes from CAD data -- ie, if it should match vertex -for-vertex, you only need to hash that. If your data is scanned - ie, you have a 3d scan and a collection of cad models -- you should probably compare convex hulls. Use something like QHull to generate convex hulls from the point cloud and all the pieces in your search. You can do a fast rejection by discarding samples with wildly differing convex hull vertex counts (again, you might want quantize the convex hull samples to hide small errors).

If you still have multiple candidates, use the longest point to point differences in the convex hulls to generate a major and a minor axis so you can rotate the models into alignment (long axis to long, second axis to second, and cross vector of those to cross) . Use the differences in volume between convex hulls as a metric for similarity. 

If that doesn't get you close enough, things get trickier. If you're doing point cloud to cad model comparisons, you might try voxelizing the point cloud and the cad data and comparing those (using the rotations from previous operation)

