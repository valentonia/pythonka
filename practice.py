"""
def min(x,y,z):
    if x <= y or x <= z:
        result = x
    if y <= x or y <= z:
        result = y
    if z <= x or z <= y:
        result = z
    
    return result
    
a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))
"""
'''
def progress(step = 1, num = 10):
    for i in range (num):
        print (i*step)
input()
d = input()
n = input()
input()
if (d!='') and (n!=''):
    d = int(d)
    n = int(n)
    progress(d,n)
elif (d!=''):
    d = int(d)
    progress(d)
elif (n!=''):
    n = int(n)
    progress(num=n)
else:
    progress()
'''
'''
def avg(num1,num2=None,num3=None):
    if num2 != None and num3 != None:
        result = (round((num1+num2+num3)/3,2))
    elif num2 != None:
        result = (round((num1+num2)/2,2))
    else:
        result = float(num1)
    
    return result  
 
a = int(input())
b = int(input())
c = int(input())
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))
'''
'''
n = int(input())
if n > 0:
    print(n*("*"))
else:
    print("Invalid input")
'''
'''
m = int(input())
n = int(input())

if 1<=m<=20 and 1<=n<=20:
    print (("*"*m+"\n")*n)
            
else:
    print("Invalid input")
'''
'''

N = int(input())
coor = input()
min_x = int(coor.split(" ")[0])
max_x = int(coor.split(" ")[0])
min_y = int(coor.split(" ")[1])
max_y = int(coor.split(" ")[1])

def min(a,b):
    if a <= b:
        return a
    else:
        return b
    
def max(a,b):
    if a >= b:
        return a
    else:
        return b
    
for i in range(N-1):
    coor_i = input()
    min_x = min(min_x, int(coor_i.split(" ")[0]))
    max_x = max(max_x, int(coor_i.split(" ")[0]))
    min_y = min(min_y, int(coor_i.split(" ")[1]))
    max_y = max(min_y, int(coor_i.split(" ")[1]))
    
print (max((max_x-min_x), (max_y-min_y))**2)

'''
'''
xa1 = int(input())
ya1 = int(input())
xa2 = int(input())
ya2 = int(input())
xb1 = int(input())
yb1 = int(input())
xb2 = int(input())
yb2 = int(input())
if (yb2 > ya1 or ya2 > yb1) or (xa2 < xb1 or xb2 < xa1):
    print (0)
else:
    x = min(xa2,xb2) - max(xb1,xb1)
    y = min(ya1,yb1) - max(ya2,yb2)
    print (x*y)
'''
'''
n = []
while True:
    x = input()
    if x == "$":
        break
    if int(x) < 0:
        continue
    if int(x) >= 0:
        n.append(int(x))
if len(n) > 0:
    print(min(n))
else:
    print("None")
'''            

n = []
while True:
    x = input()
    if x == "$":
     break
    if 
    
