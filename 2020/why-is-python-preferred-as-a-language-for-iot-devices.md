# Why is Python preferred as a language for IoT devices?

	author: Steve Theodore
	written: 2020-03-22
	views: 1025
	upvotes: 9
	quora url: /Why-is-Python-preferred-as-a-language-for-IoT-devices/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


IOT applications statistically skew towards C or C++ for both practical and historic reasons. On the practical side the tight memory footprint makes explicit memory management attractive — and in the marketplace the popularity of inexpensive Arduino kits based around C or C++ means that a lot of hobbyists got their start on microprocessors using those languages. Vanilla Python, with its relatively heavy interpreter and managed memory, is a tough sell on tiny devices.

However, the C/C++ route also comes with a lot of hurdles for new developers, especially folks who are primarily interested in completing hobby projects of prototyping connected devices rather than learning how to ride herd on a finicky compiler. That’s where __[MicroPython](https://micropython.org/)__ ____ (and its sibling __[CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)__ ) come in.

They both provide a very slimmed down, streamlined version of Python that does work will within the constraints of cheap microprocessors. These Python variants are still not as close to the metal as C or C++, so they are not quite as performant — at least, not as performant as well written C-style code. However MicroPython and its variants demand a lot less from the programmer and will be good enough for most applications, particularly in the hobby and prototype spaces. Only a fairly skilled traditional programmer will do significantly better in terms of memory and performance, but a novice is quite likely to do worse, or simply to get discouraged and go home. Hence, the MicroPython & co. are very popular with IOT developers who don’t have pre-existing knowledge of C-style languages. MicroPython occupies a nice sweet spot between the complexity of C-style memory management and the limitations of block-based programming-lite tools such as [Microsoft MakeCode Arcade](https://arcade.makecode.com/).

And let’s face it, it’s pretty cool to have a freaking [ruler ](https://www.adafruit.com/product/4319)or a [name tag](https://www.adafruit.com/product/4200) that’s programmable.

![](https://qph.fs.quoracdn.net/main-qimg-16857b7bbb096550da10afca94f89785)

_An Adafruit Pybadge running MicroPython_ 

