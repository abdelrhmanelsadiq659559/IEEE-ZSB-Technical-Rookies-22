temp=0
input_list=input(" please enter the number with space ")
user_list=input_list.split()
length_list=len(user_list)
for i in range (length_list):
    user_list[i]=int(user_list[i])

for i in range (length_list):
    for j in range (i+1,length_list):
        if int( user_list[i])==int (user_list[j]):
            distance=j-i
            if distance > temp:
                distance=temp
                temp=j-i
print(distance)
