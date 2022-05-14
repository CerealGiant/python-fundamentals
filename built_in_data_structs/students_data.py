#We take input of students and store their datas in dicts -> roll-no,name,branch

students = [] #creating an empty list of students

print("Enter the number of students: ")
n = int(input())

for i in range(n):
	print("Enter name:")
	name = input()
	print("Enter Roll:")
	roll = int(input())
	print("Enter Branch:")
	branch = input()
	data = {
	"name":name,
	"roll-no":roll,
	"branch":branch

}
	students.append(data)


print(students)
