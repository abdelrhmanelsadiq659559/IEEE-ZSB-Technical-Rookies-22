num=int(input(" please int the number:"))
if num >1:
    for i in range ( 2, num+1):
        for j  in range (2,i):
            if (i%j)==0:
                break
        else:
           print(i,end=" ")
                
else:
    print(" you should enter the number greater than 1")
