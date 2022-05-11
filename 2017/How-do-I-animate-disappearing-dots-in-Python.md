# How do I animate disappearing dots in Python?

	author: Steve Theodore
	written: 2017-05-10
	views: 420
	upvotes: 2
	quora url: /How-do-I-animate-disappearing-dots-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The algorithm is really simple. You’ve got a list of some number of points, and you want to delete them over some lapse of times. That means you need to figure out how many microseconds should elapse between deletions:

    list_of_points = [p for p in generate_random_points(1000)]
    # how many microseconds between deletions?
    deletion_interval = (len(list_of_point) - points_you_want_to_keep) / fade_time * 1000000

Then you’ll repeatedly check your list of dots, and whenever enough time passes you’ll pop one off the list.

    def update_list(since_last_deletion, elapsed_time):
     total_time = since_last_deletion + elapsed_time
     if (total_time ) > deletion_interval:
     list_of_points.pop()
     return 0
     return total_time 
    
    def run():
     last_frame = datetime.dateime.now()
     since_last = 0
     while len(list_of_points) > 20:
     elapsed = datetime.datetime.now() - last_frame
     since_last = update_list(since_last, elapsed.microseconds)
     draw() # redraw the current state of the list

The tricky part is how you want to draw stuff. You could do it with a [Jupyter Notebook](https://ipython.org/notebook.html), or using [Kivy](https://kivy.org/#home), or using [PyQt, ](https://riverbankcomputing.com/software/pyqt/intro)or any of a lot of other graphics/application frameworks. My instinct would be to write the program in python, transpile it to Javascript using [Transcrypt](http://transcrypt.org/examples#react_demo), and draw the output in the browser, which has the fewest things to worry about distributing.

