user_input=input("please enter your sorted list  betwwen numbers space:")
y=int(input("please enter the number to serach about it "))
x=user_input.split()
for i in range (len(x)):
    x[i]=int(x[i])
l=0
index=0
h=len(x)-1
while (l<=h):
     m=(l+h)//2
     if y==x[m]:
       index=m
       break
     elif (y >x[m]):
        l=m+1
     else :
        h=m-1  
print(index)

