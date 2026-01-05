#class
class Student:
    #class attributes
    clg="VIIT"
    PI=3.14
    def __init__(self,name,cgpa): #constructor - for initializing object
        #instance attributes
        self.name=name
        self.cgpa=cgpa
        self.PI=3.1


#objects
stu1=Student("Sagarika",9.3)
stu2=Student("Moukhika",8.2)
print("Names=",stu1.name," ",stu2.name)
print("CGPAs=",stu1.cgpa," ",stu2.cgpa)

#class and instance attributes value check
print(Student.clg)
print(stu1.clg)
print(stu1.name)
print(stu1.PI)
print(Student.PI)