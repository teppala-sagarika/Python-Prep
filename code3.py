#strings
word="python"

#indexing
print(word[0]) #p

for ch in word:
    print(ch)

#concatenation
s1="Hi"
s2="Sag"
s=s1+" "+s2
print(s)

#slicing
print(word[:]) #python
print(word[2:4]) #th
print(word[:4]) #pyth
print(word[2:]) #thon
print(word[-4:-2]) #th

#string formatting
a=10
b=5
sum=a+b
#normal formatting
print("sum of {} and {} is {}".format(a,b,sum))
#index based formatting
print("sum of {1} and {0} is {2}".format(a,b,sum))
#value based formatting
print("{a} and {b}".format(a=1,b=2))


#f-strings
print(f"sum of {a} and {b} is {a+b}")

#Lists
marks=[50,60,90,70,80]
print(f"length of list={len(marks)}") #5
#slicing
print(marks[2:4]) #[90,70]

#lists methods 
print(marks)
marks.append(2) # insert at end
print(marks)
marks.insert(2,4) #insert at a particular index (idx,element)
print(marks)
marks.reverse() #reverse the order
print(marks)
marks.sort() #sort in ascending order
print(marks)
marks.sort(reverse=True) #sort in descending order
print(marks)

#looping through list
nums=[7,8,9,4]
for val in nums:
    print(val)
print("once again")
for i in range(len(nums)):
    print(nums[i])

#tuples (immutable)
print("tuples")
tup=(1,2,2,3,2,4)
print(tup[3])
#tuple methods
print(tup.index(2))
print(tup.count(2))

#dictionary 
info={
    "name":"Sagarika",
    "cgpa":9.3,
    3.14:"PI",
}
print(info)
print(f"name={info["name"]}")
info["name"]=7
print(info["name"])

info["marks"]=99
print(info)

#dictionary methods
print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
info.update({
    "city":"My city",
    "vibe":"happy"
})
print(info)

#sets
s={1,2,7,3,3,2,2}
print(s)
#to create an empty set
emp_set=set()
print(emp_set)
emp_set.add(7)
print(emp_set)

#set methods
s1={1,2,3,4,5}
s2={3,4,5,8,7}

print(s1)
s1.add(6)
print(s1)
print(s2)
s2.remove(7)
print(s2)
print(s1)
s1.pop()
print(s1)
s=s1.union(s2)
print(s)
s=s1.intersection(s2)
print(s)

#list of tuples
lt=[("sag",1),("raj",2)]
for name,no in lt:
    print(name,no)
for val in lt:
    print(val[0])