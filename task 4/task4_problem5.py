matrix=[]
sum_main=0
sum_secondary=0
length_of_matrix=int(input("please enter the length of matrix:"))
for i in range (length_of_matrix):
    print(i+1,end=" ")
    x=input("row:" )
    y=x.split()
    matrix.append(y)
j=length_of_matrix-1
for i in range (length_of_matrix):
    sum_main+=int(matrix[i][i])
    sum_secondary+=int(matrix[i][j])
    j-=1
digional_difference=abs(sum_secondary-sum_main)
print("the digional diference is :",digional_difference)

