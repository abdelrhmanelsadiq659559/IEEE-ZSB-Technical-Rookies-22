data={"ahmed":[99,96,95],"mohammed":[97,99,95],"dina":[96,98,100]}
average=0
search_name="dina"
for i in data:
    if i==search_name:
        average=sum(data[i])/(len(data[i]))
        print(" the averge marks of the student is :",average)
if average==0:
    print(" there isnet student by this name")
