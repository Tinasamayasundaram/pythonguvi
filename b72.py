st=input()
count=0
vow=['a','e','i','o','u','A','E','I','O','U']
for i in st:
    if i in vow:
        count=count+1
        break
if(count>0):
    print("yes")
else:
    print("no")
        
