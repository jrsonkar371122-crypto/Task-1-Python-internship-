words=input("Enter the string:")
word=words.lower()
strings={}

for i in word:
    if i in strings:
        strings[i]+=1
    else:
        strings[i]=1
print(strings)