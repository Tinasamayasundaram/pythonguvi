a=input().split()
b=input().split()
a=list(map(int,a))
b=list(map(int,b))
m1=a[0]*60+a[1]
m2=b[0]*60+b[1]
m=abs(m1-m2)
hr=m//60
m=m-(hr*60)
print(hr,m)