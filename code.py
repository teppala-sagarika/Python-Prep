print("Hello World") 
#Hello World

print("hello\nworld") 
#hello
#world

print("hello","world") 
#hello world

#Data Types
a=4
print(type(a))
b="hello"
print(type(b))
c=True
print(type(c))
d=2.4
print(type(d))
e=None
print(type(e))
'''
<class 'int'>
<class 'str'>
<class 'bool'>
<class 'float'>
<class 'NoneType'>
'''

#Single line comments
'''multi
line
comments'''

#Arithmetic operators
num1=5
num2=2
print(num1+num2) #7
print(num1-num2) #3
print(num1*num2) #10
print(num1**num2) #25
print(num1/num2) #2.5
print(num1//num2) #2
print(num1%num2) #1

#Relational/comparission operators
print(num1>num2) #True
print(num1>=num2) #True
print(num1<num2) #False
print(num1<=num2) #False
print(num1==num2) #False
print(num1!=num2) #True

#Assignment Operators
n1=4
print(n1) #4
n1+=1 #n1=n1+1
print(n1) #5
n1-=1 #n1=n1-1
print(n1) #4

#logical operators
b1=True
b2=False
print(b1 and b1) #True
print(b1 or b2) #False
print(not b1, not b2) # False True

#bitwise operators
bit=2
print(~bit) #-3
print(bit&bit) #2
print(bit|bit) #2
print(bit^bit) #0
print(2<<1) #4 (multiply by 2power)
print(2>>1) #1 (divide by 2power)

#membership operator
lst=[1,2,3]
print(2 in lst) #True
print(4 not in lst) #True

#type conversion (implicit, done by python compiler)
conv=2+3.0
#type casting (explicit, done by developer)
cast=int(2+3.0)

print(conv,type(conv)) #5.0 <class 'float'>
print(cast,type(cast)) #5 <class 'int'>

#taking input
name=input("enter ur name=")
print("welcome",name)
#default input is string if we want other inputs we must type cast
val1=int(input("enter a int no.="))
print(val1)
val2=float(input("enter a float no.="))
print(val2)

