# practice question

#print the line no. where the word is found

word = input("Enter a word= ")
c=1
data=True
with open("wordSearch.txt","r") as f:
    while(data):
        if(word in f.readline()):
            print(f"'{word}' found at line",c)
            break
        c+=1