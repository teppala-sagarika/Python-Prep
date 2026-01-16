# FILE OPERATIONS 

#1 Open a file
f=open("sample.txt","r") #returns a file object
#mode =r # to read , mode=w "to write"

#2 Read from a file

#read() is used to read the entore file
# data = f.read() 
# print(data)

#readline() is used to read line by line
data=f.readline() #reads 1st line 
print(data)

data=f.readline() #reads 2nd line
print(data)

# #3 Write to a file
# f.write("Text to override \n the complete data")

#4 Close a file 
#(its better to close a file after performing the required operations on it)
f.close()