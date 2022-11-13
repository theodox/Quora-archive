# What exactly are dual-quaternions and how are they used?

	author: Steve Theodore
	written: 2015-11-22
	views: 1293
	upvotes: 7
	quora url: /What-exactly-are-dual-quaternions-and-how-are-they-used/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Since this one was tagged 'game development' I'm going to assume you're interested in the common application: [character skinning](https://www.cg.tuwien.ac.at/courses/Animation/skinning.pdf). 

A [quaternion](https://en.wikipedia.org/wiki/Quaternion) is a set of 4 numbers which is usually used to represent a 3-d rotation. It has some useful properties compared to the more common XYZ [Euler angles](https://en.wikipedia.org/wiki/Euler_angles) and it's less math heavy than a [3 D rotation matrix](http://inside.mines.edu/fs_home/gmurray/ArbitraryAxisRotation/). It's tricky to visualize a quaternion but you can more more or less treat three of the numbers as vector and the fourth as rotation around that axis:



![](https://qph.fs.quoracdn.net/main-qimg-d1b98113e70a8e0f4b92d32c2179a914)



Most 3-D games use what's known as _linear skinning._ When a character flexes a joint the mesh vertices move with the bones of the character's animation skeleton. A vertex in a flexible area like an elbow or knee calculates where it would be if it moved with the each bone that affects it, and then linearly interpolates between them:


![](https://qph.fs.quoracdn.net/main-qimg-017379304c6b4d76fd60168fbb2ddf77)

_Bones (center) and vertices (left and right lines). As the bone rotates, weighted verts are interpolated between the 'bone1' (orange) and 'bone2' (blue) positions._ 

Linear skinning unfortunately tends to collapse around joints with twists or large bend angles, like the right-hand sample above or this:



![](https://qph.fs.quoracdn.net/main-qimg-b713cb52072bc97611510476dba092d4)


The icky artifacts are caused by the fact that the interpolation between possible vertex positions is linear -- this causes shapes like shoulders and elbows to lose volume and look bizarre.

[Dual quaternion skinning](http://Dual quaternion skinning) (DQS) is a technique that uses dual quaternions to provide more pleasing blended vertex positions in a skinned mesh. This effectively substitutes an interpolation of _rotation_  for the linear interpolation in traditional game skinning. It preserves volumes and resists twists much better than linear skinning:



![](https://qph.fs.quoracdn.net/main-qimg-be7bc6e2c5f1af7381ddf1b2c9063fbe-c)

_Linear skinning (a) collapses the elbow; DQS (b) preserves volume pretty well._ 

This video covers this in more detail:







DQS isn't perfect -- it's still just a mathematical transformation, not a muscle system -- but it's a good compromise between cost and power. The only realistic alternative for most games is to add more bones, which gobbles up both CPU and memory.

Maya 2011 + includes dual quaternion skinning out of the box; I'm not sure about other packages. Only a handful of game engines support it (CryEngine is probably the best known example) but it's a fairly standard technique nowadays. 

The link above it the original SIGGRAPH paper and explains the math in more detail. [This link](http://This link) covers it from a code perspective.

