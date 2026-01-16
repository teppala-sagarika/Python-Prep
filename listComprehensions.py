#LIST COMPREHENSIONS

#list=[Output Iterable Condition]

list=[i*i for i in range(6)] #square of no.s 0 to 5 [0,1,4,9,16,25]
print(list)

list=[i*i for i in range(6) if i%2!=0] #only squares of odd no.s (0 to 5)
print(list)

nums=[-2,-3,3,4,-1,7,0,9]
#convert all negative no.s to 0
nums=[0 if val<0 else val for val in nums]
print(nums)
