numbr = int(input())
if numbr > 1:
    for i in range(2, numbr):
        if (numbr % i) == 0:
            print("yes")
            break
    else:
        print("no")
