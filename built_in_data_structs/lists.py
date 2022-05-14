#Lists in python: [] 

#Lists in python are ordered meaning that the elements are stored and retain their intial positons
#Lists are also mutable and accessed using index i.e. list[x] where x is the index.
#Lists are also heterogenous meaning that you can store data of different types in the same list



#Creating a list in python
a = [1,2,3,4]
#To create an empty list,
b = list()

#To access an index:
print(a[0])

#We can also change the elements this way
a[0]= 5 


#List operations


#To find the length of a string
a = [1,2,3,4]
print(len(a))

#To concatenate a list,
b = a + a


#To find membership in a list
print(1 in a)


#Lists are also iterables
for i in a:
	print(i)



#Indexing and List Slicing
#Python supports backward indexing
a = [1,2,3,4]
#To get last value, we can do this:

print(a[-1]) #This will return 4 which is similar to saying len(a) - 1

#List Slicing
a = [1,2,3,4,5]

print(a[1:4]) #a[start:end] -> start will be included while end will be excluded

#Slicing also supports jump as the last parameter
print(a[1:4:2])



#?? How to elegantly reverse a list in python??

#We can do so using list slicing
print(a[::-1]) #We jump by -1 which will reverse the list

#To check if given string is a palindrome,
if a == a[::-1] #If this is true then a is a palindrome



#To update the list, we can use insert
a = [1,2,3,4,5]
a.insert(1,"hello") #Now hello will be at the first index

#We can append the list as well
a.append("test") #Appending the list will add the given object at the end of the list

#Deleting list elements
a = [1,2,3,4,5]


a.pop() #Calling this will delete the last element in the list
a.pop(1) #pop also can take in an index.

#We can use .remove to remove the first instance of the object
a.remove(2) #We must provide the object


#We can also use del but del can be used to delete the list
del a



#To sort a list,
a = [4,5,2,1,0]

a = sorted(a) #We can use the sorted function which will take a list as an arguement and returns a sorted list

a.sort() #a.sort() will sort the list in place

#We can reverse a list as well
reversed(a)

#We can also reverse in place
a.reverse()

