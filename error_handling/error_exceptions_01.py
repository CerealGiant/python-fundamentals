#Difference between error and exception:
#An error is something wrong with the code -> computer does not understand how to compute that code
#An exception are errors that happen during the execution of the code


#Error example: This is an error because this is an invalid syntax and code does not execute at all
#fore i in range(10):
	#print("hello world!")


#Exeception example
#print(10/0) -> This will not work since 10/0 gives an infinite answer but syntax is correct and only throws an error during execution/runtime.

#Handling Exceptions
#We can use try-except to handle execptions in python
#We handle exceptions because once an exception is encountered, the program will exit right there.

def div(a,b):
	try:
		print(a/b)
	except:
		print("Error")

div(10,0)
