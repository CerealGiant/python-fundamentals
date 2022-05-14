#Lambda Functions
#This is also known as a syntactical sugar.
#Lambda functions are a way to simplify single line functions

def add():
	return a+b

#Lambda Function
add = lambda a,b:a+b
a = [('test',5),('hello',10),('test2',30)]
#Some python functions also make use of lambda functions such as sorted
sorted(a,key=lambda x: x[1]) #We provide a key if we want to specifiy a sorting method
#makes the above function sorty by the int value rather than the string (lexicographically)

