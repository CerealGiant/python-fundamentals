#Tuples in python -> ()
#Tuples are quite similar to lists but tuples are not mutable unlike lists which means we cannot change data at a particular index


#Why use a tuple over a list?
#Tuples are much more performant than a list and take up less memory and more efficient
#We use tuples over lists when we know the data in the tuples are unlikely to change
#One example of using a tuple is in *args because once the function is called, the arguments passed cannot change


#Using tuples to swap variables values
a,b = 5,9


#One way to do so is:
#a = a+b
#a = a-b
#b = a-b



#Another way using tuples:
c = 5,9 #This is another way to define a tuple in python
b,a = c #Python unpacks the tuple in c and assign it to a and b, make sure tuple elements match number of elements you are trying to assign to

#We can convert a list to tuple and tuple into a list

a = (1,2,3)
a = list(a) #Converting a tuple to a list -> this list function takes in an iterable(such as string,tuple)


a = tuple(a) #Converting a list to a tuple-> this tuple function takes in an iterable(such as string,tuple)



#We can use tuples to return multiple values from a functions
def addSubtract(a,b):
	return a + b, a - b	

sum, diff = addSubtract(9,3) #The tuple is destuctured into sum and diff


