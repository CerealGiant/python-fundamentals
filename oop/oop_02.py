#Python OOP 2


#Lifecycle of an object
#It gets created, deleted and some other activites such as being printed,add and subtract and other such events
#As such, python has created a corresponding dunder/magic method for that event.
# One such dunder is __init__(self) (Called whenever the object is created)
# Another such dunder is __del__(self) (Called whenever the object is deliberertly removed from memory)
# Another dunder is called __add__(self,other) (Called whenever we try to add one object with another)
# Another dunder is called __string__(self) (Helps convert the current object into a string -> str(a) )



#Dunders or Magic Functions

class Car:
	def __init__(self,model,mileage):
		self.model = model
		self.mileage = mileage

	def __str__(self):
		return("{} {}".format(self.model,self.mileage))

	def __repr__(self): #Used when we call print on the car class
		return "{}".format(self.model)

	def __eq__(self, other): #when equivalent operator is used
		return self.mileage == other.mileage

	def __add__(self,other):
		return self.mileage + other.mileage

c1 = Car('a',2)
c2 = Car('b',2)


print(c1+c2)
print(c1 == c2)

#Trying to implement cout in python
class Out:
	def __lshift__(self,other):
		print(other)
		return self
	def __rshift__(self,other):
		print(id(a))
		text = input()
		print("Inside Func: ",other)
		other = text
		print("Inside Func: ",other)
		return self

cout = Out()

#cout << "hello" << "this is working?"
a = "test4"
cout >> a
print(id(a))
print("TEST: ",a)
cout << a


