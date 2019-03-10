sum =0
for i in range(1001):
    if(i%3==0 or i%5==0):
        a=[i]
        sum = sum + i
        print(a, end="")
print ("\n Sum is ", sum)
