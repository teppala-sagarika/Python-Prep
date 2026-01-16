import os 
#os - operating system module is imported to enable deletion of files

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

#with keyword automatically closes the file once all the operations are performed on it
with open("sample2.txt","r") as f2:
    data=f2.read()
    print(len(data))

#create a new file and delete it 

#file creation
# f=open("newFile.txt","x")

# f.write("happy new year")

# f.close()

#file deletion
os.remove("newFile.txt")