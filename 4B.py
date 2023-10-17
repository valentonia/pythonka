n = int(input())

y = 0
if (-2**40) <= n <= (2**40):
    if n < 0:
        n = (n*-1)
    
    while n>0:
         y = y + (n%10)
         n = n //10

    print (y)
    
    

