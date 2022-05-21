#Importing in python
#A single file like this is known as a module in python

#import calculator

#print(type(calculator))
#print(calculator.add(4,5))
#print(calculator.div(4,5))
#print(calculator.sub(4,5))
#print(calculator.mul(4,5))


#selective import
from calculator import add #Only importing add function


#By using from, you can call add directly
#print(add(1,2))


#from calculator import * ->usd to import all the functions, however this is not reccomended.


#The method using * is not explicit enough and we do not know functions are actually being imported
#In addition we do not need to always import all the functions because it makes the file bloated and do not end up
#using all the functions
#By using print(globals()), you can see the functions that are in the current program.


#Hence what is the correct way to import?

#A form of syntactical sugar
from calculator import (
	add,
	mul,
	sub,
	div
)

#Python also supports aliases

#Lets say we are trying to import calculator and we have a function in main called calculator as well,
#To solve this issue, we can rename the import like this: import calculator as lib
#Now you can call lib and python will know you are referring to calculator.py


#Aliases can also be used with filtered import
#from calculator import (
	#add as addition
	#sub as subtraction
#)
