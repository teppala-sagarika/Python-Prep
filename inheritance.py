#Reusing attributes and methods from a Parent/Base Class 

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
