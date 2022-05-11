# How does adavanced iteration work in python?

	author: Steve Theodore
	written: 2015-01-30
	views: 272
	upvotes: 0
	quora url: /How-does-adavanced-iteration-work-in-python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


One thing that newcomers to python find confusing is that the classic C-Style loop form is actually very uncommon in python. That code is basically doing this:



    char[] vowels = new char[] {'a', 'e', 'i', 'o', 'u'};
    string powerful = "powerful";
    for (int i = 0; i < poweful.length; i++)
    {
     char c = powerful[i];
     if (vowels.index(c) > -1) sys.stdout.write(c);
    };



Besides better readability, this showcases some neat things Python does for you:


strings are basically lists of characters, so they can be iterated over as if they were lists


strings can also be searched as if they were lists: `if i in vowels` is asking "is this character in this list`

iterating does not require explicit loop creation. Indexed iterating is very uncommon in python, we almost always for `for something in some_container` instead of the traditional for loop form

