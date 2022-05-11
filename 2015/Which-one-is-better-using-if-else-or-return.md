# Which one is better, using "if-else" or "return"?

	author: Steve Theodore
	written: 2015-08-11
	views: 7336
	upvotes: 6
	quora url: /Which-one-is-better-using-if-else-or-return/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


I general early-outs have the advantage of simplicity: if you head down a code path that early-outs via return you can gleefully ignore the code that's not relevant this run (for example, in a debugger). 

If-else -- particularly if you do what many people do and put the important, common case _first_  -- requires you to mentally cache the initial state of the if and then un-cache it many lines later. This is particularly bad if the code is deeply nested. I follow [The Art of Readable Code](http://amzn.to/1f6KzkX) on this one.

Compare how messy this is:



    if (value.ToUpper() == value)
    {
     string other_val = DoSomethingCaseSensitive(value);
     string tmp_result; 
     string final_result;
     if (DatabaseSaysOK(other_val));
     {
     tmp_result = SomeFunction(value, other_val);
     final_result = "result: {0}".Format(result);
     }
     else
     {
     string error = "Database rejected {0}".Format(value);
     Console.WriteLine(error);
     return 0;
     }
     Console.WriteLine(final_result);
     return 1;
    }
    else
    {
     // we have to read back a couple dozen lines to know how we got here!
     string no_caps = "{0} is not all caps".Format(value);
     Console.WriteLine(no_caps);
     return 0;
    }



...whereas this is less nested and places less tax on you to remember what's going on in widely scattered locations...



    if (value.ToUpper() != value) {
     string no_caps = "{0} is not all caps".Format(value);
     Console.WriteLine(no_caps);
     return 0;
    }
    string other_val = DoSomethingCaseSensitive(value);
    if ! (DatabaseSaysOK(other_val)) {
     string error = "Database rejected {0}".Format(value);
     Console.WriteLine(error);
     return 0;
    }
    // From here we're safe to just do the job...
    tmp_result = SomeFunction(value, other_val);
    final_result = "result: {0}".Format(result);
    Console.WriteLine(final_result);
    return 1;
