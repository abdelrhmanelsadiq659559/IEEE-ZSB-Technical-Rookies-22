num=int(input("please enter number:"))
a,b=-1,1
if num>0:
    for i in range (0,num):
        c=a+b
        print(c,end=" ")
        a=b 
        b=c

else:
    print("the number should be more than zero ")
