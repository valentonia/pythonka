n = int(input())

num_found = []

y = 0
if (-2**40) <= n <= (2**40):
    if n < 0:
        n = (n*-1)
    
    while n>0:
        if n % 10 in num_found:
            n = n // 10
        else:
            num_found.append(n % 10)
            y = y + (n%10)
            n = n //10
            
        #print("n", n, ",", "y", y)
        #print("num_found", num_found)
        #print()

    print (y)
    
    