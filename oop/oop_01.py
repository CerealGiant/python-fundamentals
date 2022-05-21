#OOP in Python 01

#Class example in python

class test:
	pass

p = test() 
#Creating a new object, p is a test class object. Python is an OOP Langauage and treats everything an object ranging from int,class,float,function. Hence even the class is actually an object

#Every object in python has a flag on whether is the object callable or not = true or false
#Func objects, class objects are callable while int,float objects are not callable.
print(p) #When executing this you will notice "____main___" in front. Main is the name of the module that this class exists here. This module is called main because this is the entry point of the python script.

#Method demo in python
class Person:
	name = "john"
	def say_hi(self):
		print("hello, my name is",self.name)


p = Person()
p.say_hi() #even though this function requires a parameter called self, we called this method without any parameter.
	   #how? Since every method requires the context of the object, it automatically passes object p is passed as the first arg when the function is called

#Person.say_hi() #This is also acceptable in python


#Special Methods in python
#The __init__ method:

#As soon as the object is initialised, this method is called.

class Person:
	def __init__(self,name):
		self.name = name #Storing the name as an atrribute of the object	
	def say_hi(self):
		print("hello, my name is",self.name)

p = Person("test")
p.say_hi()
