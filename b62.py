wt=input()
yt=0
for i in wt:
  if((i=='0')or(i=='1')):
    yt=yt+1
if(yt==len(wt)):
  print("yes")
else:
  print("no")
