# Generally speaking, will a single large texture shared by objects be more efficient than a texture per object?

	author: Steve Theodore
	written: 2017-06-03
	views: 317
	upvotes: 1
	quora url: /Generally-speaking-will-a-single-large-texture-shared-by-objects-be-more-efficient-than-a-texture-per-object/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There’s not a single right answer, a lot depends on your usage pattern and the larger context in which you’re operating.

The main reason you might want to combine textures is to avoid paying a tax on the resource usage for smaller textures. On some architectures — the old Xbox 360 comes to mind — memory alignment imposes a cost on smaller textures, so an equivalent amount of pixels divided up into smaller textures could actually use more memory.

On the other hand, bigger textures also have costs. Generally, bigger textures are less friendly to the GPU cache, and it’s going to be worse if the access pattern pulls pixels from all over the texture instead of in discrete chunks. It will also be worse if the accesses are at different mip levels. So too many big textures with bad access patterns can saturate your memory bandwidth and lead to stalls.

The other thing to consider is usage. If the big textures are shared by a lot of objects which always appear together its not too bad; a classic example of this is a lightmap atlas which is shared by lots of objects in the same physical area. On the other hand you con’t want to load a 2k texture just because one object needs 64 pixels from one part of it. That tax is particularly bad if you have low bandwidth between main memory and the GPU.

In general , on modern hardware I avoid combining textures into atlasses except for lightmaps. If the intended use doesn’t involve many, many return trips to the shared texture for a lot of objects in the same context, I stick with more, smaller textures. In addition to perf benefits, this allows you finer grained control when you have to start saving memory: it’s a lot nice to halve the resolution on a few of your assets than to have to halve the resolution of everything in that atlas in one go — that’s a big, clumsy hammer to start swinging at optimization time.

