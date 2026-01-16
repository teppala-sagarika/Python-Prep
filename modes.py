#READ MODE
# f=open("sample.txt") #default is read mode

# print(f.read())

# f.close()

# #APPEND MODE
# f=open("sample.txt","a") #file object

# f.write("Text being appended to the file.")

# f.close()

# # CREATE A FILE 
# f=open("sample2.txt","x") #file object

# f.write("Some random text")

# f.close()

# + mode (read and write)
# # r+ mode
# f=open("sample2.txt","r+") #pointer is at beginning of file initially

# f.write("123")
# print(f.read())

# f.close()

# # w+ mode
# f=open("sample2.txt","w+") #pointer is at beginning of file initially
# #file truncates
# f.write("123")
# print(f.read())

# f.close()

# a+ mode
f=open("sample2.txt","a+") #pointer is at the end of the file initiallly 
f.write("happy birthday")
print(f.read())
f.close()