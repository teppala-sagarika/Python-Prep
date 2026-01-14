#ENCAPSULATION - wrapping of data and functions into a single unit called as class
#data hiding 
#public     - accessed everywhere
#_protected  - accessed within class and sub class
#__private    - accessed inside class

class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance #private - data mangling
    
    def getBalance(self): #getter
        return self.__balance
    
    def setBalance(self,newBalance): #setter
        self.__balance=newBalance

acc1=BankAccount("Rahul",48_000)

# print(acc1.name,acc1.__balance) #no access
# print(acc1.name,acc1._BankAccount__balance) #access
print(acc1.name,acc1.getBalance())
acc1.setBalance(60000)
print("new balance=",acc1.getBalance())