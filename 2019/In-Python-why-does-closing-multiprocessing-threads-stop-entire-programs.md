# In Python, why does closing multiprocessing threads stop entire programs?

	author: Steve Theodore
	written: 2019-10-28
	views: 211
	upvotes: 4
	quora url: /In-Python-why-does-closing-multiprocessing-threads-stop-entire-programs/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


multiprocessing, as the name implies, works across processes: for lack of an easier description it’s really a way to make completely separate running python programs cooperate. The syntax and mental model are sort of like threads — but under the hood these are independent processes with their own lifespans. They are basically independent programs with a messaging and memory sharing api to facilitate coordination.

If you do kill one of the processes in a multiprocessing job there are several possible outcomes. Most often killing the “main” instance of python, the one that kicked off the job, will kill the subordinate processes— they behave like daemon threads and die when their creator does. However you can kill one of the subordinates and your program may or may not continue to run depending what kind of coding approach you took (a Pool vs a single process, whether or not you are using shared memory objects to communicate, and so on).

If you don’t need separate processes you can just use threads, or you can try both approaches with the multiprocessing.Dummy module which uses thread but shares the multiprocessing api.

