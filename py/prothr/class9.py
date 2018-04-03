#-*- coding: utf-8  -*-
import json
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

json_str='{"age": 20,"score": 88,"name" :"BOb"}'
print(json.loads(json_str,object_hook=dict2student))