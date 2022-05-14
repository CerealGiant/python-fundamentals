#Dictionaries in Python -> {key : value}

#Dictionaries are unordered, data stored might not be in the same order as when the data was first added

#Creating a dict
a = {

"name": "john",
"marks": 90,
"subjects": ["eng","test"],
"friends":{
	"tom":"android"
}
}

#To access the data, we pass a key
print(a["subjects"])

#When iterating over a dict, we will be iterating over the keys
for key in a:
	print(key)

#Some impt dict methods:

#items which will create a tuple of name and value of each pair
for item in a.items():
	print(item)

#We can destructure the tuples using item,value
for item,value in a.items():
	print(item,"->",value)

#We can index a dict using [] which is unsafe

#Instead we use .get() which does not throw an error if the key does not exist returns None instead
#Clear method will empty the list.

#Also take note that keys in the dict can by any immutable data structure
#such as string,tuples
