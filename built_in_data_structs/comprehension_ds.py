#Comprehension of creating Data Structures in Python
#Using comprehension, we can create a list,set or dict in a single line of python

#Creating a list of squares till 10.
a = []

for i in range(10):
	a.append(i**2)


print(a)

#List Comprehension
#We will be squeezing the above lines in 1 sentence
b = [i**2 for i in range(10) if i % 2 == 0] #Getting only the even number
print(b)

#Dict Comprehension
c = {i : i**2 for i in range(10) if i % 2 == 0}
print(c)

#Set Comprehension
d =  {i**2 for i in range(10) if i % 2 == 0}

#Tuple Comprehension
e = {i**2 for i in range(10)} #This is a generator expression not tuple comprehension
