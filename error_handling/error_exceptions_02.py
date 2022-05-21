
#Python has many different classes of errors such as ZeroDivisionError
#We can pass the type of error as a parameter to except so that we can better handle exceptions


#Exception is the base class from which the rest of the errors are derived from

#Trying to divide 10 by 0 raises a ZeroDivisionError
#Other errors include trying to convert a string into an int is called ValueError
try:
	print(10/0) #Once error is hit, the rest of the try block does not run
except ZeroDivisionError:
	print("Test")
except ValueError:
	print("Value Error occured")
except:
	print("Default, some error other than zero division error occured")


#Exception is the base class from which the rest of the errors are derived from
try:
	print(10/0)
except Exception as e:
	print(type(e)) #We now have the error object that was created and we can access it in this except block
	#We can also get a string verison of the error
	print(str(e))
