x=[70,80,20,60,40,50]
for i in range (1,len(x)):
    key=x[i]
    j=i-1
    while(j>=0 and x[j]>key):
        x[j+1]=x[j]
        j=j-1
    x[j+1]=key
print(x)
