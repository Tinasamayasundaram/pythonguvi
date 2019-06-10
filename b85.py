st=input()
l11=[]
l22=[]
for i in range(0,len(st),2):
    l11.append(st[i])
for i in range(1,len(st),2):    
    l22.append(st[i])
n="".join(map(str,l11))
print(n,end=' ')
print("".join(map(str,l22)))
