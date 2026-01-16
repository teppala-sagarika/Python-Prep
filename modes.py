#READ MODE
# f=open("sample.txt") #default is read mode

# print(f.read())

# f.close()

#APPEND MODE
f=open("sample.txt","a") #file object

f.write("Text being appended to the file.")

f.close()