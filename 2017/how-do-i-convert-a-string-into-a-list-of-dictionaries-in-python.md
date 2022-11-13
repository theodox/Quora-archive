# How do I convert a string into a list of dictionaries in Python?

	author: Steve Theodore
	written: 2017-02-12
	views: 4845
	upvotes: 4
	quora url: /How-do-I-convert-a-string-into-a-list-of-dictionaries-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


In the general case, `json.loads()` is what you want. The data supplied in the comments is messed up by the fact that its actually a string dump of python list, so it includes single quotes (‘) instead of json-friendly double-quotes and the unicode specifier `u` in front of them.

You could — in this case, because this is stringified Python — use `eval()` — but that’s a big security risk and a habit you should not pick up. For this piece of data

    import json
    source = '''[{u'deletions': 2, u'merge_commit_sha': u'd036848f0ab8d5e85c6a131504b4c024ce44c024'},
     {u'deletions': 3, u'merge_commit_sha': u'e666848f0ab8d5e85c6a131504b4c024c8f0ab8d'}, 
     {u'deletions': 4, u'merge_commit_sha': u'f987848f0ab8d5e85c6a131504b4c024ce4b68e0'}]'''
     
    source = source.replace("'", '"').replace('u"', '"')
    json.loads(source)
