# Is it better to install a Python module from repository or from source?

	author: Steve Theodore
	written: 2017-07-20
	views: 231
	upvotes: 1
	quora url: /Is-it-better-to-install-a-Python-module-from-repository-or-from-source/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


For me the choice depends on whether you’re delivering to other people or not.

In my line of work - supporting video game artists using Python tools written for Maya — I can’t depend on my users to manage their own Python ecosystems. Not only do most artist’s eyes glaze over when I say things like ‘virtualenv’, it’s very important for the whole team to be on the same version of our tools.

For this reason, I have to ‘vendor’ my output product: I maintain a curated environment in one place and I distribute all my dependencies in a monolithic package (a single zip file) to make sure that everybody gets a complete, working ecosystem. Since I need some version control on that environment, I can’t pip-install into it; I use repos instead so I can always reproduce the state of the whole thing deterministically.

Alongside that, however, I also have a generic system python environment which I maintain using pip. That’s the one for me and my one-off tools and personal tasks. If I want to play with something new, I just virtualenv it and work in a sandbox.

So for me the binary split is on the difference between being a developer and being an end user. When I’m doing it for myself, I go with pip; when I’m going to be sharing the results I switch to repos and curation.

