#Strings are defined as the collection of characters. 
#ASCII provides the index of each character. Hence storing a string in python is interpreted by python as a list of ASCII characters.
#Strings are stored continuosly in memory. Strings are stored char by char based on ASCII value.

#Strings are immutable data structures in python meaning that once a string is initialised, we cannot change 
#a single char of the string again e.g. changing the first char of a string.

#Defining a string

a = "test"
print(a)

#Multi line string in python
a = """
	This is a multi line string

"""

#Python also does not support characters


ord('a') #This returns the ASCII value of the char
chr(65) #This returns the char based on ASCII value

#String operations

#Format String

print("{}-{}-{}".format("hello","test",5)) #This is one way to generically format a string

#Another way to do so
print("%d-%d-%d"%(5,4,3)) #However this method requires you to specify the type of data you want to print

#Format also supports keyworded arg
print("{lastname}, {firstname}".format(lastname="john",firstname="apple"))

#In newer versions of python:
username = "hello"
password = "test"

print(f"{username},{password}")



#To strip whitespaces, use .strip()
a = "            a             "
print(a.strip())
#Strip is particularly important especially whenever we take input and there is an extra space.
a = input()
print(a.strip())


#We can also use the split method to obtain a list based on the input
a = input()
a.split(' ') #Here we are telling .split that the delimeter will be the space
print(a)


#Given that strings in python are immutable, we use replace method to replace a certain char
a = "hello"
a.replace('h','b') #Multiple occureneces of h will also be replaced by b


#We can also count the number of occurence of a substring/char using .count
a = "aaaabbbbcccc"
print(a.count('a'))
