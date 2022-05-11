# I’m an experienced engineer looking at building a simple MMORTS. What are the best practices for building the persistent game world logic?

	author: Steve Theodore
	written: 2016-10-24
	views: 444
	upvotes: 3
	quora url: /I’m-an-experienced-engineer-looking-at-building-a-simple-MMORTS-What-are-the-best-practices-for-building-the-persistent-game-world-logic/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The biggest thing to consider is server architecture.

Unless this is purely a hobby project you need to think ahead to a world where you’ve scaled beyond the ability of a single physical server to host your games. Depending on the nature of your gameplay that could be in the thousands of simultaneous players — or it could be in the dozens : if, for example, you’re thinking about an action RPG with fast-moving vehicles and physically simulated objects in the world you’ll have to be worry about correct physics replication and higher-fidelity positional updates which will mean much tighter latency windows and more servers for the same number of players.

As you can imagine this has a pretty tight connection with the bandwidth requirements for your game: there’s some lowest number of updates you need for the gameplay you want. The smaller that number, the fewer servers you need. So designing features that are not chatty is a really good idea. This has a lot to do with the perennial popularity of cooldown mechanics in MMO games :)

You’ll also need to design for imperfect connectivity. Not only do you have to worry about the game experience of players who have bad connections, you have to ensure that a player with a bad connection doesn’t drag down the experience of everybody else in the same area. As you develop your game you’ll want to include tests that simulate a range of latencies and dropout rates for many clients to spot problems with your core loop design, particularly places where gameplay is overly tied to a having a fast, lossless connection. Fast, lossless connections aren’t even guaranteed at a LAN party, much less over the open internet. This is particularly tough in an RTS genre where the number of client side actions is very high compared to, say, an FRPG.

An interesting subset of connectivity issues is handling transactions. MMO games have along history of exploits that derive from incomplete transactions between players — if A disconnects just after B has sold him the Magic Sword of Swording but before his payment of Mithril has registered on the server, A may get a free sword; or he may even get a free copy of B’s sword without the B losing his. If you leave a loophole like that in your marketplaces there is a 100% certainty that players will find it and exploit it to enrich themselves or enrage others.

Another big one to consider is how your server architecture shards out the world. You’ll need to figure out how to balance out the computers’ needs for low-latency and load balancing with the needs of players to find and play with their friends: nothing is more dispiriting for an MMO player than discovering that they have created a new character on a different server from all the people they want to play with.

Finally you need to design on the assumption that all client-side data is already compromised. No matter what you do , players will be able to take apart your client and see how the network traffic is structured. That’s why pretty much all games in this space provide radars: it’s often easier to concede the fact that the players will hack the client. The only way to keep secrets from the players is to keep them from the clients as well — so you can’t, say, update all unit positions on the client and rely on the client’s rendering to hide things from players. This also means that all resolution of interactions has to stay on the server: you can never delegate a question like “did X hit Y” or “how much damage did that attack do” to a particular client; the host must do it.

Server-side ownership of the rules means that you also need to be aware of the problem of paradoxes. Every client has an imperfect view of the pure, platonic truth on the server. It’s quite easy for them players to see things in their reality which are out of line with the servers’; on my client, I had you head in my crosshairs when I popped the trigger, but on the server you’d never actually gone around the corner — I just missed a server packet and my client placed your image there on my screen as a prediction. There are lots of ways things can go wrong and you’ll need to find design solutions that minimize them although in the end they will never be completely eliminated.

Oh, and since the server is the truth you want to validate that all of your interactions are as close to perfectly deterministic as possible. Its hard enough to keep dragging all the clients back into sync in order to account for packet loss and latency; if different architectures are giving you different floating point numbers for the same inputs thanks to machine-level quirks, its even harder — and numerically intense systems like physics are much more vulnerable to that sort of problem. If you can replay the game perfectly from a timestamped list of client messages you’ll have a vastly better time.

Related to that, of course, is that you need to have good authentication and encryption for your connections to prevent bad actors from impersonating other players. But that’s an instance of general networking nowadays.

Here’s a great talk from a real vet on the gnarly innards of a successful MMO server.



This is from the same guy: [Writing Server and Network Code for Your Online Game](http://www.gdcvault.com/play/1015379/Writing-Server-and-Network-Code) (this might be paywalled for you - but Pat Wyatt is The Man in this space as far as I’m concerned).

These are more about physical and gameplay interactions, particularly as regard latency and determinism.

[http://gafferongames.com/networking-for-game-programmers/what-every-programmer-needs-to-know-about-game-networking/](http://gafferongames.com/networking-for-game-programmers/what-every-programmer-needs-to-know-about-game-networking/)

[Developing Your Own Replay System](http://www.gamasutra.com/view/feature/2029/developing_your_own_replay_system.php)

[How to design a replay system](http://gamedev.stackexchange.com/questions/6080/how-to-design-a-replay-system)

