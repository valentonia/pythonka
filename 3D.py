sum = 0
while True:
    n = input()
    if n == "$":
        print (sum)
        break
    n = int(n)
    if n:
        sum += n 
    
