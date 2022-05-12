#Control Flow Statements 01

#1. Conditional Statements

#if-else statement

#Indentation rule in python:
#If you have a statement and you have a code snippet associated with the statement,
#then you indent the code snippet relative to the statement to make it clear that the 
#code snippet is part of the statement.
# Use tab to indent the code in python

a = 0
if a > 0:
	print("Positive")
elif a == 0:
	print("a is equal to 0")

else:
	print("Negative")

#Nested if-else statement

a = 6
if a > 0 :
	if(a % 5 == 0):
		print("a is divisible by 5")
	else:
		print("a is not divisible by 5")
else:
	print("a is negative")

#If statements to be used in the control flow are mutually exclusive, use elif and else not multiple if statements

