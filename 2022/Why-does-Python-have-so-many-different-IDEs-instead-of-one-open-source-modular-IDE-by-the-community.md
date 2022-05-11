# Why does Python have so many different IDEs instead of one open-source modular IDE by the community?

	author: Steve Theodore
	written: 2022-02-09
	views: 4465
	upvotes: 46
	quora url: /Why-does-Python-have-so-many-different-IDEs-instead-of-one-open-source-modular-IDE-by-the-community/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Probably the easiest answer is that Python got popular among *nix users who were used to working with console text editors like vim. IDLE was a concession to Windows users who were unlikely to have a decent console editor handy; Visual Studio was massive overkill for the ordinary Python scripter and modern lightweight GUI IDEs like VSCode and Sublime were still in the future.

Building an IDE is not actually a huge undertaking anymore — but it’s a crowded market. Linters, syntax highlighters, and other coding tools are common enough that there’s no strong reason to tie the language to a particular editor anymore.

All that, of course, is long in the past — nowadays the IDE market is pretty robust. You’ll note however that Jupyter, which is more of an integrated playground environment rather than an IDE proper — is the most popular. That has a lot to do with the fact that it addresses one of Python’s most popular niches (data science) and makes it easy for people to do what they want to do — munge data and see the results graphically. Old-school console editors like Vim and Emacs are now way at the back of the pack.

![](https://qph.fs.quoracdn.net/main-qimg-4515c3e76508ab858fe9f5b16927c42e-lq)

