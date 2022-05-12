# 2 types of lines: either a statement or an expressions
# statments can be if statements if,elif and for statements
# expressions are the combination of opertos and operands
# An expression yields an output -> the expression is evaluated by the interpreter and it returns an output
# The output of the epxression is called the result. However this output is not equal to the print function
# When you print it prints to the STDOUT Stream 


# Arithmetic Operators
print(10 // 20)
print(10 / 20)
print(5**2)
print(5%2)

#Comparision Operators 
#Python supports the same comparision operators as other programming langauges
#For strings, python compares strings lexicographically.

#Assignement Operators
#Python supports the same assignments operators as other programming languages such as *=, +=

#Logical Operators
#Logical operators work on True and False values
a = True
#In python, the True value is actually an integer
print(isinstance(True,int))
#Although type of True is a bool, this is actually inherited from int class
#Bool in python is not a primitive type

# Hence, then how does python handle booleans?
# It does so by making use of Truthy values and Falsy values
# Truthy values are values that are not absolutely true but can be considered true such as
# positive integers, negative integers, strings that are not empty and True
# Falsy values are values that are not absolutely true but can be considered true such as
# 0, empty strings and False


