y=[5,12 ,9 ,61,5,14]
x=[]
reverse_num=0
num=y[0]
for i in range (len(y)):
     if y[i]>0:
         x.append(True)
     else:
         x.append(False)
while num>0:
    digit=num%10
    num=num//10
    reverse_num=reverse_num*10+digit
if reverse_num==y[0]:
    x.append(True)
else:
    x.append(False)
z=all(x)
print(z)
