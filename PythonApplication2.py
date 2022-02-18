input1=input("please inter the word:")
number_of_repeat=int(input("please enter number of repeating:"))
number_of_repeat_r=0

x=[]
y=[]
j=0

#for  i in input1:  # for to convert list to string
    #x.append (i)
x=list(input1) # # for to convert string to list
for i in range(0,number_of_repeat):  # for reapt string which converted to list
    z=x[j]
    y.append(z)
    j+=1
    if j >(len(x)-1):
        j=0
for i in range (number_of_repeat):
    if y[i]=='r':
        number_of_repeat_r +=1
print(" the letter of r is reapted:",number_of_repeat_r)

    
    
