# What 3D file formats are the most popular in game industry?

	author: Steve Theodore
	written: 2015-11-23
	views: 5271
	upvotes: 5
	quora url: /What-3D-file-formats-are-the-most-popular-in-game-industry/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


FBX is the overwhelming favorite - it's writable (to some degree) from lots of different platforms. It's not really a great format, it tries to do too many things and the original design goal (round-tripping between different art packages without loss) is almost impossible. Nevertheless it's widespread and integrated into Max and Maya so it's the most common format by default. There is a text version but it's based on XML so it's super verbose.

OBJ is great for geometry - it's simple enough that you can write an exporter in an afternoon and it's human readable. Unfortunately no animations support.

[Alembic](https://alembic.readthedocs.org/en/latest/) is interestng but it's not really targeted at games.

