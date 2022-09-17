x=[1,1,1,1,2,3,4,4,5,6,7,7,8,9]
i=len(x)
z=len(x)
while  z >=0:
    i=len(x)
    for j in range (i):
        if j!=i-1:
         if x[j]==x[j+1]:
            x.remove(x[j+1])
            break    
    z-=1  
print(x)
