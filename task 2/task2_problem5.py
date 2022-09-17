input_list=input(" please enter numbers with space: ")
user_list=input_list.split()
length_list=len(user_list)
for i in range (length_list ):
    user_list[i]=int(user_list[i])

if length_list>1:
    user_list.sort()
    print(" the second heightest is :",user_list[-2])
else :
    print( " you should enter more than one number")

