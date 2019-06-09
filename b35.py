t=str(input())
c=0
for i in range(len(t)):
    if(t[i].isnumeric()):
        c=c+1
print(c)
