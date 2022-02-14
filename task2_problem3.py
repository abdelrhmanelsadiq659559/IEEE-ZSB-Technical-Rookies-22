input_string = input('Enter elements of a list separated by space :')
max1=0
star="*"
space=" "
user_list = input_string.split()
for  i in user_list:
    if len(i)>max1:
        max1=len(i)
y=len(user_list)-1 # used in print ***** after last index
for i in user_list:
    z=(max1-len(i))
    if i==user_list[0]   :
        print(star*(max1+4))
    print(star,end=" ") # print first star and make space
    print(i,end="")  
    print(space*z,star)

    if i==user_list[y] :
         print(star*(max1+4))

