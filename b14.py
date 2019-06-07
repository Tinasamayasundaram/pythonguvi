m1,m2=[int(m1) for m1 in input().split()]
b=range(m1,m2)
list=[]
for c in b:
    if((c>m1) and (c<m2)):
        if(c%2!=0):
            list.append(str(c))
d=' '.join(list)
print(d)
