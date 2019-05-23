n,l=input().split()
n = int(n)
l = int(l)

for num in range(n, l + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
