num=int(input())
x=input().split()
x=list(map(int,x))
x.sort()
print(x[num//2])
