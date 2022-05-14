#Python Decorators

#Assume we want to password protect a function based on a list of users
users = {
	"john": "password"
	"tom": "abcd1234"	

} 

def show(username,password):
	if username in users and users[username] == password:
		print("Hello world!")
	else:
		print("Not Authenticated")



#However, if we want to protect another function, we will have to re-type this whole function
#Hence we will be creating a wrapper function to wrap our current function and make it password protected

def login_required(func): #Taking in a function
	def wrapper(username,password,*args,**kwargs):
		if username in users and users[username] == password:
			func(*args) #Putting * in front of args will inflate the tuple that args holds into indivdual parameters
		else:
			print("Not authenticated")
	return wrapper




#Now lets make an add func that will be password protected
@login_required #Using decorators in python (Call this before function declaration)
def add(a,b):
	return a+b
#Hence, now to call add, we need to provide the username,password,a,b

#add = login_required(add) #This is one way to wrap the function


#This is the way to call using decorators


