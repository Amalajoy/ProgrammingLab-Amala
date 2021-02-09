w=input("Enter a string :")
s=w.split(" ")
print("swapped string:")
for i in reversed(range(0,len(s))):
    print(s[i],end=" ")
