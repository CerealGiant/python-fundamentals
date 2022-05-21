#Inheritance in Python

#Common mistake in Python OOP

class Dog:
	kind = "canine"
	def __init__(self,name):
		self.name = name
	

#Lets define 2 objects

a = Dog("tom")
b = Dog("john")
b.kind = "something" #Chaning b's kind here only changes the kind of b, not for a. a is still a canine
print(a.kind)
print(b.kind)

class Dog:
	tricks =[]
	def __init__(self,name):
		self.name = name
	def add_tricks(self,trick):
		self.tricks.append(trick)

#Lets define 2 dogs here


a = Dog("tom")
b = Dog("test")
b.add_tricks("barking")
print(b.tricks)
print("A:",a.tricks) #Notice how a also contains the element added for b


#Why does this happen? This happens because whenever an object is created, first python copies the object's attributes (meaning its variables and methods) before calling the init method.

#Hence, both a and b share the same list and hence both point to the same list in memory. Given that a list is a mutablestructure, we can add/change elements in the list. Given that both objects point to the same list, they will be updating the same list in memory and hence a change by one object to the list can still be seen by other objects.

#To prevent this, we can init the tricks list inside the init method, which means that after all the methods are copied over then we actually create the list.
