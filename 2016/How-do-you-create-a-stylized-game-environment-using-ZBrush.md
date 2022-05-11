# How do you create a stylized game environment using ZBrush?

	author: Steve Theodore
	written: 2016-01-27
	views: 887
	upvotes: 1
	quora url: /How-do-you-create-a-stylized-game-environment-using-ZBrush/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Zbrush is a great tool but generally environments are not its strong point.



Most genres of game require a lot of iteration in environment design: tweaking the distance between locations, controlling lines of sight, and accommodating the limits of AI or player movement. ZBrush excels at making individual objects (rocks and trees, for example, or man-made props) but it's not designed for arranging them : in most cases a zbrush file represents a single object or maybe an object assembled from a small library of reusable pieces. A game environment typically consists of dozens or hundreds of objects and it's important to have a UI that's designed for managing that task. Lastly, most games will require various kinds of extra information beyond the visible model -- from adding markup to tell the game where to play a particular effect or indicating that an object is breakable to providing a simplified convex hull for efficient physics. Zbrush has no real support for any of those.

So, zbrush will be part of a pipeline which includes visible models -- which it is very good at producing-- but also other tools for handling the layout, annotation, and lighting of the finished environment. The modeling part is only a fraction of the whole.

