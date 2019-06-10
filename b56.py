at=str(input())
ct=0
dt=0
for i in at:
    if(i.isalpha()):
       ct=ct+1
    elif(i.isnumeric()):
       dt=dt+1
if(ct>=1 and dt>=1):
    print("Yes")
else:
    print("No")
