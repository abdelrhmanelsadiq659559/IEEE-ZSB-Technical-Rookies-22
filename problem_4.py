import random 
rnd=random.randint(1,10)
i=0
while True:
  num=int(input())
  i+=1
  if num == rnd :
      print("you have tries ", i)
      break
  else : 
      print("wrong number")
