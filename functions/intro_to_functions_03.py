#Function arguement python
#First you should give the required arguements,then packed positional args, then arugments with the default values,then followed by packed keyword args
def abc(a,b,c, d = 10,e = 20):
	pass

def show(a,b,c): #Here in the function signature, a,b and c are known as formal arguements
	print(a)
	print(b)
	print(c)

show("hello","world","python") #a = hello, b = world, here a, b and c are known as actual parameters
#However, we can choose what value we want to pass to the parameter
show(b="hello",c="world",a="python") #These are called keyworded arguments 

#we can also have default args
def show(b,c,d=10):
	print(b)
	print(c)
	print(d)

show(10,20,d=30)

#in python, we have *args which packs all the optional positional args in a tuple. Such a *args is used in the print function to take any number of args to print
def show(a,b,c,*args):
	print(a)
	print(b)
	print(c)
	print(args)

#This means that the show function takes in a minimum of 3 args(a,b,c) 
show(10,20,30,"packed","arguments")

#python also supports packed args
def show(a,b,c,*args,d=10,e=20,**kwargs):
	print(a)
	print(b)
	print(c)
	print(args)
	print(d)
	print(e)
	print(kwargs)

show(40,50,60,d=15,name = "hello") #kwargs packs any keyworded arg not in the functional signature and packs it as a dictionary

