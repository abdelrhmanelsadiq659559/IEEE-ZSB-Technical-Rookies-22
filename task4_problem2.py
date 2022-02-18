import string
import random

upper_letters=list(string.ascii_uppercase)
lower_letters=list(string.ascii_lowercase)

numbers=[0,1,2,3,4,5,6,7,8,9]
special_char=["@", "#", "$", "%","&"]
long_of_password=10
password=[]
numbers_of_lowers=random.randint(1,4)
numbers_of_uppers=random.randint(1,4)

for i in range (numbers_of_lowers):
    z=random.randint(0,len(lower_letters)-1)
    j=lower_letters[z]
    password.append(j)
for i in range (numbers_of_uppers):
    z=random.randint(0,len(upper_letters)-1)
    j=upper_letters[z]
    password.append(j)

numbers_of_num_special=long_of_password-numbers_of_lowers-numbers_of_uppers
if numbers_of_num_special%2==0:
    number_of_nums=random.randint(1,numbers_of_num_special/2)
    for i in range (number_of_nums):
        z=random.randint(0,len(numbers)-1)
        j=numbers[z]
        password.append(j)
    number_of_special=numbers_of_num_special-number_of_nums
    for i in range(number_of_special):
        z=random.randint(0,len(special_char)-1)
        j=special_char[z]
        password.append(j)
else:
    number_of_nums=random.randint(1,numbers_of_num_special//2+1)
    for i in range (number_of_nums):
        z=random.randint(0,len(numbers)-1)
        j=numbers[z]
        password.append(j)
    number_of_special=numbers_of_num_special-number_of_nums
    for i in range(number_of_special):
        z=random.randint(0,len(special_char)-1)
        j=special_char[z]
        password.append(j)
print("password is :",end=" ")
for i in password:
    print(i,end="")
print(" ")

    
