# How would you create a simple spell checker program using Python?

	author: Steve Theodore
	written: 2016-10-24
	views: 3964
	upvotes: 8
	quora url: /How-would-you-create-a-simple-spell-checker-program-using-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There’s a wonderful example of a simple Python spell checker by Peter Norvig here: [http://norvig.com/spell-correct.html](http://norvig.com/spell-correct.html), and an github project I wrote which shamelessly steals his ideas here: [theodox/spelchek](https://github.com/theodox/spelchek).

The basic strategy is pretty simple: you look at the word and use a set of rules to generate potential variants. You’ve got a big dictionary which associates real words with scores that reflect how likely they are to be used in practice. For all the generated variants, check the list and get the highest scoring word — or give the user a list of words sorted by score if you’ve got something interactive.

The main fun trick is to write both the variant generations and the lookups as chains of generator expressions instead of functions that return lists: this makes it faster and less memory intensive.

The hard part is coming up with the scored dictionary. I wrote the code for my version in a couple of hours. Cobbling together word lists and scores from various free sources took a couple of days. Feel free to steal my dictionary if you’re writing your own version of the code!

