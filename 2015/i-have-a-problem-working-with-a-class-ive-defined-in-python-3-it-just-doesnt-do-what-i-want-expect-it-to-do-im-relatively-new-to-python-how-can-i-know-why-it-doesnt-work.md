# I have a problem working with a class I've defined in Python 3. It just doesn't do what I want/expect it to do. I'm relatively new to Python. How can I know why it doesn't work?

	author: Steve Theodore
	written: 2015-09-02
	views: 590
	upvotes: 1
	quora url: /I-have-a-problem-working-with-a-class-Ive-defined-in-Python-3-It-just-doesnt-do-what-I-want-expect-it-to-do-Im-relatively-new-to-Python-How-can-I-know-why-it-doesnt-work/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


R2.ifc is class member, so all instances of R2 share the same copy. Was that your intention? What happens if you remove line 4?

PS. You can embed code directly using code blocks. It'll be easier to get answers if people can paste your code into an interpreter



    class R2:
     def __init__(self, name, count):
     self.name = name
     self.ifc = [Address(i) for i in range(count)]
