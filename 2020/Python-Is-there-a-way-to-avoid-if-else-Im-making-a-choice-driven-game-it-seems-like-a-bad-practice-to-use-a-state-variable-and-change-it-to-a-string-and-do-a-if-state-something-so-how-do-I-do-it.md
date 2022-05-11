# (Python) Is there a way to avoid if/else? I'm making a choice driven game, it seems like a bad practice to use a "state" variable and change it to a string, and do a "if state == 'something'", so how do I do it?

	author: Steve Theodore
	written: 2020-03-28
	views: 307
	upvotes: 5
	quora url: /Python-Is-there-a-way-to-avoid-if-else-Im-making-a-choice-driven-game-it-seems-like-a-bad-practice-to-use-a-state-variable-and-change-it-to-a-string-and-do-a-if-state-something-so-how-do-I-do-it/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you’re just trying to avoid long chains of if/elif conditionals a very common python idiom is to use a dictionary where other languages would a switch/case construct.

Say you have a “room” in your game and the player can leave to the north, south, or east or use some stairs. You can clean up that logic with a dictionary lookup like this:

    player_choice = raw_input(“where do you go?”)
    next_room = {
     “east”: 27,
     “south”: 132,
     “north”: 33,
     “stairs”: 14
    }.get(player_choice, this room)
    
    go_to_room(next_room)

Here the dictionary returns the number of another “room” in the game, or the number of the current room if the user entered something unusable. There’s a more complete example of this approach [in this coderview post](https://codereview.stackexchange.com/questions/36101/better-way-to-code-this-game/36112#36112).

In a practical example of a choose-your-own-adventure game you’ll really need two levels of state — one of which represents inventory and one of which handles location / actions . However it’s easy enough to pass the current inventory into each ‘room’ as a function, modify it based on what happens, and pass the modfied one to the next function as an argument. [This post ](https://codereview.stackexchange.com/questions/36768/tiny-text-adventure/36829#36829)examines some of the ways you could handle inventory and combat in a similar style

