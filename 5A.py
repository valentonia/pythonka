def min (x,y,z):
    result = ''
    if x <= y and x <= z:
        result = x
    elif y <= x and y <= z:
        result = y
    elif z <= y and z <= x:
        result = z
    return result

a = int(input())
b = int(input())
c = int(input())

print (min(a,b,c))