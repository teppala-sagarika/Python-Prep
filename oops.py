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
    #instance methods
    def getInfo(self):
        print(self.name,self.cgpa,self.clg) #can access class and instance attributes
    #class methods
    @classmethod #decorator
    def getClg(cls):
        print(f"College Name={cls.clg}")
    #static method 
    @staticmethod #decorator
    def checkIfPassed(cgpa):
        if(cgpa>5):
            print("Status: Passed")
        else:
            print("Status: Failed")


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

#calling instance method
stu1.getInfo()

#calling Class method
stu1.getClg()
Student.getClg()

#calling static method 
Student.checkIfPassed(stu1.cgpa)
Student.checkIfPassed(stu2.cgpa)
stu1.checkIfPassed(stu2.cgpa)