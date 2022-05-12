#Looping statements

#While loop in python
a = 5

while a == 5:
	print("Inside while loop")
	a = 6


#for loop in python
#for loop syntax in python:
# for a in b -> a is the iterator and b is the iterables
#iterables are objects which can be broken down into smaller atomic variables
#e.g. a list [1,2,3,4] -> can be broken down into 1,2,3,4

for i in "python" :
	print(i)

#Common iterable used in python is range() -> range returns an iterable
#e.g. range(5) returns an iterable ranging from 0 to 4 0,1,2,3,4
#range(2,10) returns 2-9
#range(1,11,2) -> 1,3,5,7,9 -> numbers with a jump of 2

for i in range(5,10,2):
	print(i)


