# What compiled language should I go to from a python programmer?

	author: Steve Theodore
	written: 2015-12-13
	views: 607
	upvotes: 0
	quora url: /What-compiled-language-should-I-go-to-from-a-python-programmer/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Assuming you've already considered mainstream options like Java and C#, you might try [Nim, ](http://nim-lang.org/)a compiled language with a significant whitespace syntax but compile-time safety checks and some interesting ideas.

    var a: array[0..1, char]
    let i = 5
    try: 
     a[i] = 'N'
    except IndexError: 
     echo "invalid index"

There's also [delight](https://github.com/pplantinga/delight) which is a pre-processor that allows you to write [ D ](http://dlang.org/)with a python-like syntax; D itself has some nice modern features and is a good tools and automation language.

Another option is [Boo: ](https://github.com/bamboo/boo)a very pythonic language that runs on the dot net CLR. Boo has lots of nice features and is similar to C# in terms of distribution (it's a tad slower at runtime but not by anything like the large C# -> Python delta). After a popular start about a decade ago development has slowed, but the language community is trying to rebuild the momentum. It supports python-style 'duck' typing as an option, though that has performance costs. As a side effect you can write Unity games in Boo.

