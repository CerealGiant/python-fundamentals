#Python File handling

#Opening a file

file = open("hello.txt","r")


print(file.read()) #Inside the .read() function, you can add the number of bytes you want the function to read:


#It is very important to close the file once done handling it
file.close()

#Writing to a file
file = open("something.txt","w")

file.write("hello from the other side")

file.close()

#Reading from a file
file = open("hello.txt","r")
file.readline() #This will loop through all the lines in the file when run multiple times
file.readlines() #This creates a list of all the lines in the file
file.close()

#Moving the cursor
file = open("hello.txt","r")
print(file.read(5))
print(file.read(5))
#To move back the cursor we can call seek
file.seek(0)
print(file.read(5))
file.close()



#Smarter way of opening a file
#By using the with statement, you get better syntax and exceptions handling
#In additon, using with automatically closes the file. The with statement provides a way for ensuring that a clean-up is always used.
#This means you do not need to write file.close()
print("----------------")
with open("hello.txt","r") as file:
	print(file.readline())
	print(file.readline())
	file.seek(0)
	print(file.readline())

#Once you exit the with block, the file is already closed.
	
