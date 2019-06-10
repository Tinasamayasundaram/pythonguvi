import math
n,m = input().split()
n=int(n)
m=int(m)
number=n*m
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print("yes")
else:
    print("no")
