#Editing JSON files in python

with open("data.json","r") as file:
	print(file.read())
	#However, we cannot access indivdiual elements in a JSON file using the keys
	#print(file.read()["name"])

#Thus we need to parse the JSON file into a python dict or a python dict into a JSON file. To do this, python provides alib called json. 

import json

with open("data.json","r") as file:
	d = json.load(file) #Here in .load() we are taking a json file into a dict
	print(type(d))
	print(d)
	print(d["name"])


#Using .loads() where we take in a JSON String instead
with open("data.json","r") as file:
	d = file.read()
	print(type(d))
	data = json.loads(d)
	print(data["name"])



#Converting a python dict into a json file
d = {"name": "test", "marks":90}
string = json.dumps(d) #Converting a dict into a json string

#Creating a JSON file with an existing python dict
with open("data2.json","w") as file:
	json.dump(d,file)
