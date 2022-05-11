# Which programming language to create for Maya and Photoshop?

	author: Steve Theodore
	written: 2016-12-29
	views: 2780
	upvotes: 5
	quora url: /Which-programming-language-to-create-for-Maya-and-Photoshop/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


For Maya, Python is the best choice — unless, by chance, you’re already a fairly serious C++ programmer. Even then there are a lot of Maya support jobs that are far easier to handle in Python. I only go to C++ for the heavy-duty, performance intensive problems, less than 10% of the work. A great community for Maya programming is [Tech Artists.Org](http://tech-artists.org/)

For Photoshop… really you’re stuck with Javascript, and not a nice modern Javascript either but a little Javascript shim jammed onto a very creaky, old-fashioned C API. You can do _most_  of the same thing using COM (so, you can do it with any language that has a COM bridge — I’ve seen it done in C# and Python, but it can be done from anything that talks to COM with varying degrees of pain. Unfortunately not all of Photoshop is easily accessible via COM, so you’ll probably end up having to do at least some of the work in Javascript. The Photoshop scripting system is an embarrassment which Adobe shows no sign of rectifying, and it might be impossible to fix since it’s clear that the data model and tools are not well separated from the visible UI (hiding tool panels, for example, can speed up your scripts a lot) . It’s better than nothing — but if you’re trying anything serious it can be extremely frustrating.

[http://wwwimages.adobe.com/content/dam/Adobe/en/devnet/photoshop/pdfs/photoshop_cs5_scripting_guide.pdf](http://wwwimages.adobe.com/content/dam/Adobe/en/devnet/photoshop/pdfs/photoshop_cs5_scripting_guide.pdf)

[TRANBERRY.COM • Adobe Photoshop Scripting](http://www.tranberry.com/photoshop/photoshop_scripting/)

[Introduction To Photoshop Scripting – Smashing Magazine](https://www.smashingmagazine.com/2013/07/introduction-to-photoshop-scripting/)

