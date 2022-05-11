# Should I wait for a while and do some basic things with Python without any framework before jumping into Django?

	author: Steve Theodore
	written: 2017-02-06
	views: 355
	upvotes: 3
	quora url: /Should-I-wait-for-a-while-and-do-some-basic-things-with-Python-without-any-framework-before-jumping-into-Django/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you’re confident about Python syntax, and you’ve already got some web expertise, then Django is not a particularly difficult API in general — that’s why it’s popular. So there’s a good case for just giving it a try.

That said, one thing that helps a lot with being effective in Django is some understanding of how the SQL database backend actually works — what SQL does and how. Even though Django hides a lot of that from you it’s good to know what’s _really_ going on behind those pretty Django models. So you might want to make sure you’ve got some experience with SQL tables and queries — which you can get using the builtin sqllite module in Python and any good [sqllite tutorial](http://zetcode.com/db/sqlitepythontutorial/). Django is more fun than real SQL but it’s good to know what Django is doing in the background.

Another way to get that background knowledge would be a project in [Flask](http://flask.pocoo.org/), which doesn’t hold your hand the way Django does. The little [microblog example](https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr) they include in their tutorial gives you a good look at the barest of bare-bones python web apps).

