n = (input())
largest = n
smallest = n

if n == "$":
    print ("Invalid input")

else:
    while True:
        n = (input())
        if n == "$":
            break  
        
        if int(n) > int(largest):
            largest = n
            
        if int(n) < int(smallest):
            smallest = n
            
    print (smallest)
    print (largest)


