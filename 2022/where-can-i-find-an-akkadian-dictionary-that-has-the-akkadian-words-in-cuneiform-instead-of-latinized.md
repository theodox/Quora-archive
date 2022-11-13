# Where can I find an Akkadian dictionary that has the Akkadian words in Cuneiform instead of Latinized?

	author: Steve Theodore
	written: 2022-05-30
	views: 1475
	upvotes: 76
	quora url: /Where-can-I-find-an-Akkadian-dictionary-that-has-the-Akkadian-words-in-Cuneiform-instead-of-Latinized/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You don’t really want a dictionary for that, you want a sign list.

Cuneiform is a messy writing system with many different ways to render the same word (for example, [there are many way to spell “Gilgamesh”](https://www.quora.com/Is-Gilgamesh-real-name-Bilgames/answer/Steve-Theodore?ch=10&oid=331744007&share=fecd7c4d&srid=zLvM&target_type=answer)) . So, people who study the language and its evolution tend to want some distance from the vagaries of cuneiform representation. Standard field practice is to first “[normalize](http://oracc.museum.upenn.edu/doc/help/languages/akkadian/obakkadian/index.html)” the cuneiform text and then use tackle the normalized-transliterated signs with a dictionary. This is not as easy as that makes it sound: the mix of logographic and syllabic writing, several millennia of changes in spelling, and the wierd gymnastics that cuneiform scribes did to impress one another mean that it’s very, very rare to be able to just look at a few signs and say “ah, got it.”

For the language side the 900-lb gorilla is the Chicago Assyrian Dictionary ([available online here, in the form of 900 lbs of pdfs](https://oi.uchicago.edu/research/publications/assyrian-dictionary-oriental-institute-university-chicago-cad)). It’s arranged alphabetically by transliteration because it’s much easier to navigate — and because entering cuneiform text into any electronic form is a pain in the butt (here, [cuneify ](http://oracc.museum.upenn.edu/saao/knpp/cuneiformrevealed/cuneify/)is your friend — but even your friend is a lot slower than typing Latin characters).

There are multiple competing sign lists; they generally agree about the sound and/or meaning of the signs but they use different ordering conventions (more detail than you probably want in the introductory chapter of [this](http://www.sumerisches-glossar.de/download/SignListNeoAssyrian.pdf)). Typically the number conventions are based on stroke order, somewhat like the ordering in a Chinese dictionary — though these conventions are hard to impose on older versions of cuneiform, which are more pictographic.

So, to do a translation the procedure will be something like this:

1. Find a sign list for the era you’re working with ([this is a good source](https://cdli.ox.ac.uk/wiki/sign_lists)). [This one](http://home.zcu.cz/~ksaskova/Sign_List.html) includes both old and the more common Neo-Assyrian forms. T

2. Figure out the stroke ordering that was used in the list — it will usually be somewhat visible if you scan the list but it’s going to take practice to know where to skip to when finding a sign if your list doesn’t tell you explicitly how it was arranged. This is the order used by the Borger (Mesopotamisches Zeichenlexikon, or MesZl ) sign list that you’ll find in the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_cuneiform_signs), which is pretty good.

![](https://qph.cf2.quoracdn.net/main-qimg-60f8792367f43713141db941b297ccc5-lq)

_Pro tip: if you’re working with a text that’s already in unicode Cuneiform, you can select it and just use ‘find’ in a sign list page like_ _[this](http://home.zcu.cz/~ksaskova/Sign_List.html)_ _or the wiki one._ 

3. Normalize the text, swapping in the transliterations for the original cuneiform

4. Use a dictionary to actually translate the normalized text into Akkadian

5. Then translate that into the language of your choice

Kind of shows you why Assyriology is not a crowded field.

