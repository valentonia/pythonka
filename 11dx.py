b = 0
min_b = 0
while True:
    n = input()
    if n == "$":
        break
    n = int(n)
    b += n
    min_b = min(min_b, b)    
print(-min_b)
