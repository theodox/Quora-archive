# How does 3D calculation really work in modeling software and games?

	author: Steve Theodore
	written: 2018-01-20
	views: 690
	upvotes: 6
	quora url: /How-does-3D-calculation-really-work-in-modeling-software-and-games/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Most 3d math comes down to a handful of basic linear algebra concepts.

__Vectors__ 

Positions in space are represented as three numbers which represent the three cardinal dimensions of the 3–d world — left-right, in-out, and up-down (typically known as X, Y and Z).

You can also use 3-vectors to represent a _direction_  instead of a position. In a world where Z is up, a vector of 0,0,1 represents the direction ‘up’ and 0, 0, -1 would represent ‘down’. You can do basic math on vectors — for example, the spatial difference between two point represented as vectors is just the first vector minus the second. You can scale them up or down by multiplication, and you can get their length so you could, for example, know how far it is from one point to another by doing the subtraction and getting the length of the result.

Vectors have two neat extra operations as well:

The ___[vector dot product](https://theodox.github.io/2014/bagels_and_coffee.html)___ __ multiplies two vectors to make a single number. If both of those vectors are exactly 1 unit long, the dot product will be the cosine of the angle between the directions they represent. When a rendering system wants to figure out how much a particular surface is facing a direction, it uses the dot product.

The __[vector cross product](https://en.wikipedia.org/wiki/Cross_product)__ ____ takes two vectors and produces a new vector that points at right angles to the first two. This means you can figure out, for example, the facing of a surface as long as you have three points — get the vectors between the first and second and then the second and third points — the cross product of those vectors is the facing direction (usually we call it the ‘normal’ ) of the surface.

__Triangles__ 

With three XYZ positions, you can represent a triangle. Triangles have a lot of nice mathematical properties. By taking the cross product of two sides, you can get the surface direction (the ‘normal’). Using the dot product of the normal and the vector to some other point in space you can determine whether that point is above, below, or right on the surface of the triangle. 3-d models are usually stored internally as collections of 3-d points and then lists of triangles.

__Matrices__ 

Vectors arranged into lists of triangles can describe a model, but if you want to manipulate it you need methods of moving or rotating the points. Most often we do that with a [matrix](https://theodox.github.io/2014/dot_matrix.html), which is sort of like a generalization of vectors. A matrix usually looks something like this:

     0.707 	0.000 	-0.707	0.000 
    -0.331 	0.883	-0.331	0.000 
     0.625 0.468 0.625 0.000 
     240.0 180.0 240.0 1.000

The first three numbers .707, 0, -.707 represent the “X axis” of the matrix, that is, where the X direction of the world (usually 1, 0, 0) is pointing in this matrix. .707, 0, -.707 indicates that the X axis is rotated 45 degrees around the Z axis. The first three numbers of lines 2 and 3 are the Y and Z axes in the same way. The bottom left-hand three numbers are positions: they indicate that this matrix is offset to position 240, 180, 240.

When you multiply a vector against this matrix, you’re basically saying “here’s a point in space — if it were relative to that matrix, where would it tend up after the rotation, scale and position changes in the matrix”. You can also multiply multiple matrices together to make a new matrix: this represents a bunch of movements, rotations etc in series. The skeleton of an animated 3-d character is really just a series of matrices representing the places where the character can bend: first you move-rotate the shoulder, then the elbow, then the wrist, etc.

__3d to 2d__ 

Vectors, triangles and matrices are enough to describe a complete 3-d scene, but they are still in three dimensions. In order to get those 3-d points onto a screen you need to create a ‘camera’ that will convert those 3-d points. Luckily this is just another matrix, though one with a tweaked set of numbers. It’s job is to flatten the 3-d points onto a plane which will then be the final image — something like the way a camera focus light onto a receptor to turn 3-d reality into a 2-d picture.

![](https://qph.fs.quoracdn.net/main-qimg-5d49265ffa202c8f2b99d1a269fe8de5-c)

The projection matrix can represent a perspective or an orthographic view — the math is the same, the only difference is the numbers in the matrix.

__Shading__ 

Most of what people think of as ‘3-d rendering` is _[shading](https://en.wikipedia.org/wiki/Shading)_ _—_ once you’ve used your matrices to flatten your triangles onto a 2-d image plane you want to make them look as if they respond to light, or have distinctive surface texture. There are a million variations on this in detail, but they all rely on the same basic algebra under the hood. The [rendering equation](https://en.wikipedia.org/wiki/Rendering_equation) is the basis of all realistic computer graphics, and it’s really just another dot product: it’s usually written __N (dot) L__  where N is the surface normal and L is the vector to a light. We already saw that the dot of those two vectors is the cosine of the angle between them - as it happens, that’s also a pretty good approximation of the way visible light intensity falls off with angle for a non-shiny surface.

![](https://qph.fs.quoracdn.net/main-qimg-2d4fcd3ccf630cf5dbf669d990872050-c)

Shiny stuff (technically, ‘[specular reflection](https://en.wikipedia.org/wiki/Specular_reflection)’ is usually faked with a different equation that takes into account the angle between the surface and the viewer as well:

![](https://qph.fs.quoracdn.net/main-qimg-ae38cd88f80d9bd4f71cd51cc63cff04-c)

Nowadays there are many more elaborate tricks (for example, you might use a stored image to look up a range of lighting sources instead of calculating a mathematically perfect ray using the math above) but the basics all come back to the elementary tools of linear algebra.

Good reason to stick with math in high school!

Good basic course here with



And a more advanced version here:



