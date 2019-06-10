pt=int(input())
qt=0
rt=1 
while rt<=pt: 
  if pt%rt==0:
      qt=qt+1 
  rt=rt+1
if qt==2:
  print('yes')
else: 
  print('no')
