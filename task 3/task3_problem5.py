import collections
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
total=0
counted_ar=collections.Counter(ar)
for i in counted_ar:
    total=total+counted_ar[i]//2
print("the number of pairs is :",total)
