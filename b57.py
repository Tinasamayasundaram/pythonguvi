a,b=input().split()
a=int(a)
b=int(b)
c=0
s=list(map(int,input().split()))
for i in range(len(s)):
    if(s[i]==b):
        c=c+1
print(c) 
