#class
class Student:
    def __init__(self,name,cgpa): #constructor - for initializing object
        self.name=name
        self.cgpa=cgpa


#objects
stu1=Student("Sagarika",9.3)
stu2=Student("Moukhika",8.2)
print("Names=",stu1.name," ",stu2.name)
print("CGPAs=",stu1.cgpa," ",stu2.cgpa)