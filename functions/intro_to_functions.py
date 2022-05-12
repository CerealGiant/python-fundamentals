#Functions are useful when you need to repeat certain code snippets
def hello_world(): 
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")


#hello_world()

#Functions can also accept parameters
def hello_world(i): #Taking i as the number of times to print 
	for k in range(i):
		print("hello world")

#hello_world(10)

#Parameters can be optional as well
def hello_world(name,i=3): #Taking i as the number of times to print 
	for k in range(i):
		print("hello world {}".format(name))
hello_world("penny",5)
