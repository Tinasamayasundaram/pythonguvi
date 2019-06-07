a=input()
a=a.split()
b=int(a[1])
c=input()
c=c.split()
d=0
c=list(map(int,c))
for i in range(0,b):
    d=d+c[i]
print(d)
