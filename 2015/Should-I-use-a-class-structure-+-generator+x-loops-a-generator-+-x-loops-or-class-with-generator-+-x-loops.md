# Should I use a class structure + generator+x-loops, a generator + x-loops, or class with generator + x-loops?

	author: Steve Theodore
	written: 2015-01-01
	views: 98
	upvotes: 1
	quora url: /Should-I-use-a-class-structure-+-generator+x-loops-a-generator-+-x-loops-or-class-with-generator-+-x-loops/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Based on the comments, there are two ways you could do this. Classes will work better if the random generation is stateful, and first-class functions will be simpler if it is stateless.

If your randomizing routines need to have some persistent state, you probably want to tackle this by creating a variety of classes, each of which shares a common method to produce the actual results. You could then use the some other logic to create a list of these classes and call their methods in turn. 

Here's a really simple example, using 3 different classes that use the same interface to generate temperature lists, but have 3 different methods of generating the random numbers.



    import random
    
    
    class RandomTemp(object):
     """ naaive random number from 0 to 100"""
    
     def __init__(self, size=10):
     self.size = size
    
     def generate(self):
     for r in xrange(self.size):
     yield self.next()
    
     def next(self):
     return random.random() * 100
    
    
    class CenterWeighted(RandomTemp):
     """ simple weighted distribution, biased toward 50 """
    
     def next(self):
     r1 = random.random() * 25
     r2 = random.random() * 25
     r3 = random.random() * 25
     r4 = random.random() * 25
     return r1 + r2 + r3 + r4
    
    
    class Statistical(RandomTemp):
     """ use a selection from historical samples"""
    
     SAMPLE_DATA = [48, 25, 82, 37, 20, 43, 82, 7, 75, 83, 85, 97, 95, 30, 30, 22, 78, 30, 84, 52, 36, 83, 53, 1, 22, 96, 8, 63, 15, 12]
    
     def __init__(self, size=10):
     self.size = size
     self.pointer = int(random.random() * len(self.SAMPLE_DATA))
    
     def next(self):
     r = self.pointer
     while r == self.pointer:
     r = int(random.random() * len(self.SAMPLE_DATA))
     self.pointer = r
     return self.SAMPLE_DATA[self.pointer]
    
    
    batch = [Statistical(20), CenterWeighted(20), RandomTemp(20)]
    results = []
    for sampler in batch:
     results.append([i for i in sampler.generate()]) 



By making the number generators into classes, you can use both stateful algorithms -- such as the 'Statistical' one which uses saved numbers -- and stateless ones like the simple call to random.random().

If you're sure you don't need state, you don't need to use classes. You could just provide a list of methods which did the generation, and call the methods directly:



    def pure_random(size, min, max):
     for r in xrange(size):
     yield random.random() * (max - min) + min
    
    
    def gaussian_random(size, min, max):
     for r in xrange(size):
     yield ((random.gauss(0, 1) * .5) + .5) * (max - min) + min
    
    
    def pareto(size, min, max):
     for r in xrange(size):
     yield random.paretovariate(1) * .1 * (max - min) + min
    
    
    algorithms = [pure_random, gaussian_random, pareto]
    results = []
    for algo in algorithms:
     results.append([i for i in algo(20, 0, 100)])



In this second example, all the functions take the same signature so its easy to loop through them passing stansardized arguments and collect the results.

The other dimension here is whether or not to use generators (the _yield_  statement) or returns. I usually opt for generators automatically, since generators will allow you to process items one at a time without keeping an entire list of values in memory. In both of my examples it's not an issue, since I'm creating a final list which contains all of the temperatures anyway; but for really big data sets it's advantageous to process lazily. 

Generators are also great if you want to hide the complexity of series generation from other code. Say, for example, you needed to generate time-varying samples so that you got realistic seasonal variations: a generator could easily handle the seasonal variance behind the scenes, so that the temperatures just came out in a reasonable order and other code didn't know or care what had to happen to make the order come out correctly.

PS re-reading the comment I realize this sample code is not grouping the temperatures into 10-degree increments. Without a clearer ideas of the use case I don't want to try to implement that, but the it's another good application for a generator: you could keep the existing code to have a variety of randomization strategies, and then pass the results into a separate generator that did the batching. If you use generators instead of conventional returns throughout, you will be able to randomize and batch the whole series without the need to keep two big data sets in memory at once.

