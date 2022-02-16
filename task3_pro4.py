import collections
ar = [1,2,3,4,5,4,3,2,1,3,4]
max=0
number_max_counter=0
dub=collections.Counter(ar)
print(dub)
for i in dub:
   if (dub[i]>max):
       max=dub[i]
for i in dub :
     if (dub[i]==max):
         number_max_counter=i
         break
print(number_max_counter)
         
         
