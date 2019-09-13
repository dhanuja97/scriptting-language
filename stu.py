students = {'1MS18IS100':'asha','1MS18IS101':'Ashok','1MS18IS102':'rekha','1MS18IS103':'suma'}
list = ["value1","value2","value3","value4"]
list2=[]
j=0

for i in students:

	print("key is",i, "value is",students[i])
	list[j]=students[i]
	j=j+1

print(list)
print(students.keys())
print(students.values())
print(students.items())
