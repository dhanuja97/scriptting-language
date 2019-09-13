#Demo:class in python
class person:
	def __init__(self,name,age):#this is the constructor of the class person
	  self.name= name;
	  self.age= age;

p1=person("dhanuja",14)


print("\nName of the person #1 is",p1.name)
print("\nage of the person #1 is",p1.age)

print("\n*** Printing after deleting age  attribute for p1***")
del p1.age #deleting the age attribute for p1 object
print("\nName of the person #2 is",p1.name)

print("\n*** Printing after deleting p1***")
del p1
print("\nName of the person #1 is",p1.name)#this line will give an error
#error is:Nameerror:name 'p1' is not modified

