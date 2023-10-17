a = float(input())
b = float(input())
c = float(input())
maxr = 0
maxp = 0

for r in range(0, 2001):
    r = r / 100
    
    p = a*(r**3) + b*(r**2) + c*r
    if p > maxp:
        maxp = p
        maxr = r
        
print(maxr)