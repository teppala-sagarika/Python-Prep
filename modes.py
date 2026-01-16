#READ MODE
# f=open("sample.txt") #default is read mode

# print(f.read())

# f.close()

# #APPEND MODE
# f=open("sample.txt","a") #file object

# f.write("Text being appended to the file.")

# f.close()

# CREATE A FILE 
f=open("sample2.txt","x") #file object

f.write("Some random text")

f.close()