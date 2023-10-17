'''
m = int(input())
n = int(input())

if 0<n<20 and 0<m<20:
    print ((m*'*'+'\n')*n)
else:
    print("Invalid input")
'''

xa1 = int(input())
ya1 = int(input())
xa2 = int(input())
ya2 = int(input())
xb1 = int(input())
yb1 = int(input())
xb2 = int(input())
yb2 = int(input())

if(yb2>ya1 or xa2>xb1) and (ya1>yb2 or xb1>xa2):
    print (0)
else:
    x = min(xa2,xb2) - max(xa1,xb1)
    y = min(ya1,yb1) - max(ya2,yb2)
    print (x*y)