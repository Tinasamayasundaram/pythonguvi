a,b=input().split()
a=int(a)
b=int(b)
c=d=0
s=list(map(int,input().split()))
for i in range(len(s)):
    if(s[i]==b):
        c+=1
    else:
        d+=1
if(c>=1):
    print("yes")
else:
    print("no")
