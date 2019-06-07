n=int(input())
y=input().split()
y=list(map(int,y))
y.sort()
for i in y:
    print(i,"",end="")
