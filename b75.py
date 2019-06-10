Stt=list(input())
mid=len(Stt)//2
if len(Stt)%2==0:
    Stt[mid]='*'
    Stt[mid-1]='*'
else:
    Stt[mid]='*'
for i in Stt:
    print(i,end='')
