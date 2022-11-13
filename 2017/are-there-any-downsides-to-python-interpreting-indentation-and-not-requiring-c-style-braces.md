# Are there any downsides to Python interpreting indentation and not requiring C-style braces?

	author: Steve Theodore
	written: 2017-05-12
	views: 1086
	upvotes: 9
	quora url: /Are-there-any-downsides-to-Python-interpreting-indentation-and-not-requiring-C-style-braces/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


As I think you can see from the other answers, this issue is long on emotion and shorter empirical evidence.

Any token system that tries to represent the nesting of scopes in what’s ultimately a one-dimensional stream of characters is going to annoy some people. Indentation vs braces is an aesthetic choice first: I know that this bit of Lisp is completely legit. But it still gives me the cooties:

    (defun make-edge-list ()
     (apply #'append (loop repeat *edge-num*
     collect (edge-pair (random-node) (random-node)))))

And — let’s be honest here — most curly bracket advocates feel the same way about that sample… _even though it’s formally hitting all of the things they say they like, and doing it more consistently than C-style braces._ People strongly privilege the familiar in their evaluation of the look and feel of code on screen.

I think it’s easier to just be upfront about the role of personal aesthetics which (a) saves you a lot of jawboning and (b) lets you put a pricetag on choices which are subjective.

This video includes a very eloquent discussion of the role of aesthetics in development. But it’s also got a great technical core which demonstrates some of the ways in which code formatting actually is a canary-in-the-coalmine for code which is just plain objectively bad.



