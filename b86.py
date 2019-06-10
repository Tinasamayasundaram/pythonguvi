str=input().split()
for i in str:
    st=set(i)
    if(len(st) == len(i)):
        print("Yes")
    else:
        print("No")
