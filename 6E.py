def binary(n):
    
    if n == 0:
        return '0'
        
    elif n == 1:
        return '1'
        
    else:
        return binary(n//2) + binary(n%2)
n = int(input())
print (binary(n))