at=input()
count=0
bt=0
for i in range(len(at)):
    if(at[i].isalpha() or at[i].isdigit()):
        bt=bt+1
    else:
        count=count+1
print(count)
