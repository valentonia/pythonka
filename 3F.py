n = int(input())

if 1 <= n <= 1000:
    for d in range(1, n+1):
        if n % d == 0:
            print (d)
else:
    print ("Invalid input")