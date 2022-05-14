#Sets in python 
#Only thing that matters in a set is the existence of that particular object


#Creating a set
a = {1,2,3,4} #Similar to a dict but no key value pair

#To create an empty set:
a = set()

a = {1,2,3,4}
b = (3,4,5,6)


a.intersection(b) #Used to get the common values between both

a.union(b) #To get all the values in and b

#Sets are however iterable
for i in a:
	print(i)

#Sets store only unique values hence even if you init a set with multiple duplicate values set will auto delete the duplicate values

#Deleting duplicate values in a list
a = [1,2,3,1,2,5,4,5]
list(set(a))
