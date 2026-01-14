#Reusing attributes and methods from a Parent/Base Class 


#types of inheritance
#Single level Inheritance
#Multilevel inheritance
#Multiple inheritance


#Single level inheritance
class Employee: #parent/base class
    _startTime="10am" #protected
    _endTime="6pm" #protected

    def change_time(self,new_startTime,new_endTime):
        self._startTime=new_startTime
        self._endTime=new_endTime

class Teacher(Employee): #child/derived class
    def __init__(self,subj):
        self.subject=subj

class AdminStaff(Employee): #child/derived class
    def __init__(self,role):
        self.role=role

t1=Teacher("Math")
t1.change_time("8am","4pm")
print(t1.subject,t1._startTime,t1._endTime)

t2=Teacher("Physics")
print(t2.subject,t2._startTime,t2._endTime)

staff1=AdminStaff("Manager")
print(staff1.role,staff1._startTime,staff1._endTime)

#Multi level inheritance
class Accountant(AdminStaff): #can have Admin staff attributes as well as Employee attributes
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary

acc1=Accountant(25000,"CA")

print(acc1.role,acc1.salary,acc1._startTime,acc1._endTime)
 

#Multiple inheritance
class TeachingStaff:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,cgpa):
        self.cgpa=cgpa

class TA(TeachingStaff,Student):
    def __init__(self,salary,cgpa,name):
        super().__init__(salary) #1st class constructor
        Student.__init__(self,cgpa) #2nd class constructor
        self.name=name

ta1=TA(15_000,9.5,"Sagarika")

print(ta1.name,ta1.cgpa,ta1.salary)


