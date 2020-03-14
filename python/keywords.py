#!/bin/python
sum1 = 0
sum2=0
def simpleArraySum(ar,n):
    for x in range(0,n):
        sum1 = sum1+ar[x]
    return sum1
ar = [1,2,3,4,10,11]
n = len(ar)
print(n)
sum2 = simpleArraySum(ar,n)
print(sum2)
