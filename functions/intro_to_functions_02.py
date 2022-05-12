#Functions (Return, Local, Glocal)

#Return statement
def add(a,b):
	return a+b

a = add(5,2)
print(a)

#Try,Except,Finally in function
#In this case, the finally block will always run regardless of whether the statement in the try block 
#succeeds or not
def div(a,b):
	try:
		return a/b
	except:
		print("Error!")
	finally:
		print("Wrapping up")
		return 50

x = div(10,2) #x holds the value that is returned in the finally block
print(x)

#Local and Global Variables
y = 10 #Here y is a global variable
def hello(): 
	#If you define the same y within this function, this will be treated as a local variable
	#within this function
	#However trying assignment with the global variable like this
	#y+=5
	#this will result in an error saying that local variable y has been referenced before assignmenet
	#to fix this, explicitly state that you are using the global variable
	global y
	y+=5
	print(y)

hello()

#Python also supports inner function
def outer():
	x = 5
	def inner():
		#x+="a" this will result in an error
		#to fix this,
		nonlocal x #by doing so you make python look for x in the enclosing function
		x+=5
		print(x)
	inner()
	print(x)
outer()

