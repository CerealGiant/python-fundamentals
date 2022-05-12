#This is a python comment

# ''' ''' -> This however is not a multiline comment rather it is a multiline string

#Literal Constants in python
# Numbers - Integers, Floats and complex numbers
#Strings - which can be written with single or double quotes, multiline strings(triple quotes), Escape sequences,
#Explicit line joining

#Numbers
#To see the type of a variable in python, use type(variable_name)

a = 5 #This is an integer
print(type(a)) #Running this command will tell you that this is a object is of type class 'int'

a = 1.5
print(type(a)) #Running this line will tell you that this object is of type class 'float'

a = 5j #Complex number example
print(type(a))

#Python does not support character types hence any text even in single quotes is seen by python as a string
a = 'a'
print(type(a))

a = "a" #This is also a string type
print(type(a))

a = '''
This is also a multiline
string
'''
print(a)
print(type(a))



#Variables are a type of identifier
#Identifier rules in python:
#First character cannot be a number or special characters except _
#Identifier names are also case sensitive
