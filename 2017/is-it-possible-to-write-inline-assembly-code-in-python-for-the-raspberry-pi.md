# Is it possible to write inline assembly code in Python for the Raspberry Pi?

	author: Steve Theodore
	written: 2017-07-09
	views: 1235
	upvotes: 6
	quora url: /Is-it-possible-to-write-inline-assembly-code-in-Python-for-the-Raspberry-Pi/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You don’t need to write assembly to control the Pi’s GPIO board — the [RPi.gpio](https://pypi.python.org/pypi/RPi.GPIO) module (which I think comes pre-installed if you use the `noobs` distribution on your pi — includes control over the GPIO. If you think software perf and not system timings might be the issue you can always run C programs instead; you can use [Cython](https://github.com/cython/cython/wiki/EmbeddingCython) to compile python programs to C executables (or as fast extension modules you can run from regular python for flexibility).

Here’s a couple of links to pi + GPIO projects

[Raspberry Pi GPIO Tutorial: The Basics Explained - Pi My Life Up](https://pimylifeup.com/raspberry-pi-gpio/)

[Raspberry Pi GPIO Pins and Python | Make:](http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/)

[Gordons Projects](https://projects.drogon.net/raspberry-pi/gpio-examples/)

Because of the pi’s clock speed, the relative crudeness of GPIO, and the speed of Python, a pi isn’t usually going to be appropriate for very tight timings — if you’re thinking milliseconds rather than fraction of a seconds, you may find the out-of-box pi isn’t responsive enough. For high-speed kind of stuff might be better for a pure microcontroller like an Arduino (which typically is programmed in C or C++) . If you want to stick with Python in the microcontroller realm, consider the [WiPy](https://www.adafruit.com/product/3184): a microcontroller which runs Micropython as its OS (so, unlike a Pi, it doesn’t have to worry about OS interrupts messing with timings).

If you’re still feeling the itch to do it in assembly — and if you do, you’re way more hardcore than I’ll ever be — you might find this interesting:

[Raspberry Pi Assembly Language Raspbian [Third Edition]](http://www.brucesmith.info/raspberry-pi-assembly-language-raspbian/)

