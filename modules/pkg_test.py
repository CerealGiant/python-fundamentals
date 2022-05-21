#Trying to import the math package here
#import math

#print(math.complex) #This will not work


#If you try to print the math,
#print(math) #you will notice that when you try to import math, you are actually trying to import the __init__.py file

#We need packages to differentiate/divide our python program with their own namespace. For example, in the complex file the square function could have a different implementation than simple's square function. Thus to prevent the clashing with their own global scope.

#from _math import *
from _math import( 
simple,
complex
)

print(complex.cube(2))
print(simple.add(1,2))
