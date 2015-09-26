import json

j_file = json.load(open('tt_blog.json.txt'))
categories = {}
for elem in j_file:
	if elem['category'] in categories.keys():
		categories[elem['category']].append(elem['body'])
	else:
		categories[elem['category']] = [elem['body']]
