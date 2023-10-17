n = int(input())

y = ''
if 0 <= n <= (2**20):
    while n > 0:
        b = n%2
        n = n//2
        y = str(b) + y
    
    if y == "":
        y = "0"

    print (y)

else:
    print ("Invalid input")
    


    
