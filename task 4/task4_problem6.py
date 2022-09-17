page_numbers=int(input("please enter the  number of pages :"))
page_to_reach=int(input("please enter the number of page to reach it :"))
if page_to_reach<=page_numbers/2:
    print("they only need", page_to_reach//2,"to turn  page")
else :
    if page_numbers%2!=0:
        print("they only need",(page_numbers-page_to_reach)//2,"to reach page")
    else:
        if page_to_reach%2==0:
           print("they only need",(page_numbers-page_to_reach)//2,"to reach page")
        else :
             print("they only need",(page_numbers-page_to_reach)//2+1,"to reach page")
