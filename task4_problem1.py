x=[]
numbers_of_bottels=int(input("please enter the numbers of bottels:"))
if numbers_of_bottels >1:
    for i in range (numbers_of_bottels):
       input_user=input("please enter the volume and capacity between them space:")
       y=input_user.split()
       x.append(y)
    for i in  range (len(x)):
        x[i][0]=int(x[i][0])
        x[i][1]=int(x[i][1])
    x_index0=[]
    x_index1=[]
    total=0
    max_two=0
    for i in range(len (x)):
      x_index0.append(x[i][0])
      x_index1.append(x[i][1])
    total=sum(x_index0)
    x_index1.sort()
    max_two=x_index1[-1]+x_index1[-2]
    if max_two>=total:
      print("yes")
    else:
       print("no")
else:
    print("please enter the number of bottels more than one")
    
