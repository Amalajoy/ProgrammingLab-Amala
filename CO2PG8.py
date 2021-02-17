a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter the word" + str(x+1) + ":")
    a.append(element)
    max=len(a[0])
    temp=a[0]
for i in a:
    if(len(i)>max):
       max=len(i)
       temp=i
print("Longest Word:",temp)
print("Length of longest word :",max)
