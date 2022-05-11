# Do game developers use inheritance and OOP fairly heavily compared to most non-game developers?

	author: Steve Theodore
	written: 2017-03-27
	views: 1768
	upvotes: 10
	quora url: /Do-game-developers-use-inheritance-and-OOP-fairly-heavily-compared-to-most-non-game-developers/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


A lot of games make super heavy use of OOP techniques. The Unreal engine has an absolute bestiary of classes, subclasses and sub-sub-sub-classes — I’ve never counted them but I’d be surprised if the total doesn’t run to the low thousands at least. Almost everything you interact with in Unreal derives at several removes from [UObject](https://docs.unrealengine.com/latest/INT/API/Runtime/CoreUObject/UObject/index.html).

That said (and to balance out the good info in the other answers), it should be noted that a lot of game developers are leery of too much OOP — particularly in performance sensitive parts of a game. OOP — especially naive OOP where the mental convenience of the programmer matters more than the needs of the computing hardware — can result in inefficient layouts of data in memory and bad access patterns. High performance games need to be super careful about making data as coherent as possible in the CPU’s cache. For that reason a lot of developers (particularly those on console hardware) balance out traditional OOP with [Data-Oriented Design](http://www.dataorienteddesign.com/dodmain/node3.html).

For an entertaining, if maybe a bit overblown, look at why data oriented design is an important antidote to some common OOP problems check out Mike Acton’s talk on DOD vs OOP



Brian Will’s critique is not game specific and I don’t buy it completely, but it’s thought provoking.



