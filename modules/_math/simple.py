#Simple calculation(add,sub,div,mul)

def add(a,b):
	return a+b

def div(a,b):
	return a // b


#In python, each module has a special variable named __name__ which tells us the name of the file
#When this module is run directly, __name__ will be equal to __main__.
#But when this module is imported its __name__ will be math.simple

#Hence, if we want to run certain checks/code only when this module is run directly we can do so by checking if the name of this file is __main__


if __name__ == '__main__':
	print("hello") #This line will only run if this python file is run directly. When this file is imported and called in another file it will not run
