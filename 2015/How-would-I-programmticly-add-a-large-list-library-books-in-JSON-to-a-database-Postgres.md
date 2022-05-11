# How would I programmticly add a large list library books (in JSON), to a database (Postgres)?

	author: Steve Theodore
	written: 2015-09-12
	views: 163
	upvotes: 2
	quora url: /How-would-I-programmticly-add-a-large-list-library-books-in-JSON-to-a-database-Postgres/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You _could_ use [Postgres' support for JSON columns](http://www.postgresql.org/docs/9.3/static/functions-json.html). In this strategy you just dump all of the JSON data into a JSON column in Postrgres and then run queries directly using the extended operators and functions in the link above. I have not first hand experience with it but there is a Django extension that should allow you to issue Postgres queries: [djangonauts/django-pgjson](https://github.com/djangonauts/django-pgjson). That extension supports the same kind of JSON operations as Postgres, but wrapped in the Django object model -- so it would presumably integrate well with a pre-existing Django application.

The wisdom of doing it that way probably depends on the quality/reliability of the data and the nature of the application. Using Postgres like a [NoSQL](https://en.wikipedia.org/wiki/NoSQL) database is do-able, but it doesn't make sense if performance or data integrity are the key problems. A nice, tidy, old-fashions SQL DB is almost always faster than an unstructured, document based DB and can contain much more aggressive checks for data integrity. If this is a simple project with a short shelf-life -- and if you trust the data to be pretty consistent -- the Postgres/Django/JSON route is very little extra work.

