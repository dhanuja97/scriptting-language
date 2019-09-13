class person:
 	def __init__(self,name,age):#this is the constructor of the class person
	  self.name= name;
	  self.age= age;

p1=person("dhanuja",14)
p2=person("arpitha",12)
#to objects s1 and s2 are created. the -init_constructor is automatically called
print("\nName of the person #1 is",p1.name)
print("\nage of the person #1 is",p1.age)

print("\nName of the person #2 is",p2.name)
print("\nage of the person #2 is",p2.age)
p2.age=10 # attribute of the object can be modified


print("\nmodified age of the person #2 is",p2.age)
