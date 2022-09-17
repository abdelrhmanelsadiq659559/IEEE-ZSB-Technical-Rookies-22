number=int(input("please enter the number:"))
total =0
if number >1:
    for i in range (1,number+1):
      if i%5==0 or i%3==0:  
        total+=i
    print(total)
else:
    print("the number should be greater than 1")
