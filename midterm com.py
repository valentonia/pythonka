'''
r = int(input()) 
c = 1
i=1
while c <= r:
    for j in range (i):
        if c<=r:
            print(c,end=" ")
            c+=1
    i+=1
    print()
'''

'''
x = int(input())
if x > 20000:
    print("maximum withdraw amount is 20000 baht")
elif x <= 0:
    print("the input amount is invalid")
else:
    if x%100 == 0:
        print("Amount valid")
    else:
        print("the input amount is invalid")
'''
'''
result = ''
x = int(input())
while True:
    if x > 0:
        if x % 3 == 0:
            result = '0' + result
        elif x % 3 == 1:
            result = '1' + result
        elif x % 3 == 2:
            result = '2' + result
        x = x // 3
    else:
        print (result)
        break

'''


'''
result = ''
x = int(input())
def recursive (a):
    global result,x
    if a == 0:
        print (result)
    
    else:
        if a % 2 == 0:
            result = '0' + result
        elif a % 2 == 1:
            result = '1' + result
        a = a // 2
    recursive(a)

recursive (x)
'''
'''
result = '' 
x = int(input())
while True:
    if x > 0:
        if x % 2 == 0:
            result = '0' + result
        elif x % 2 == 1:
            result = '1' + result
        x = x//2
    else:
        print (result)
        break
    
'''
'''
result = ''
x = int(input())
def recursive(a):
    global x,result
    if a == 0:
        print(result)
    
    else:
        if a % 2 == 0:
            result = '0' + result
        elif a % 2 == 1:
            result = '1' + result
        a = a//2
        recursive(a)
        
recursive (x)

'''
'''
x = (input())
result = 0
y = len(x)-1
for i in range(len(x)):
    result += int(x[i])*(2**(y-i))
print(result)
'''
'''
num = float((input()))
x = int(num//1)
decimal = num - x
result_int = ''
result_deci = ''

while True:
    if x > 0:
        if x % 2 == 0:
            result_int = '0' + result_int
        elif x % 2 == 1:
            result_int = '1' + result_int
        x = x//2
    else:
        break
    
for i in range(20):
    if decimal * 2 >= 1:
        result_deci += '1'
        decimal = (decimal*2)-1
    elif decimal * 2 < 1:
        result_deci += '0'
        decimal = decimal * 2
        
print (result_int + '.' + result_deci)

'''
'''
def function(a,b=None,c=None):
    if b!=None and c!=None:
        result = print((a+b+c)/3,2)  
    if b!=None:
        result = print((a+b)/2,2)
    else:
        result = float(a)   
    return result

x = int(input())
y = int(input())
z = int(input())
print(function(x,y,z))
'''
'''
n = int(input())
result = ''
while True:
    if n > 0:
        if n % 3 == 0:
            result = '0' + result
        elif n % 3 == 1:
            result = '1' + result
        elif n % 3 == 2:
            result = '2' + result
        n = n // 3
    else:
        print(result)
        break
'''
'''
n = int(input())
c = 0
num = n % 1000
if num == 500:
    b = 0
elif num // 500 == 0:
    b = 0
elif num // 500 == 1:
    b = 1000

if n > 1000:
    c = (n // 1000) * 1000
result = c + b
print(result)
'''
'''
n = int(input())
c = 0
num = n % 1000

if num == 500:
    b = 0
elif num // 500 == 0:
    b = 0
elif num // 500 == 1:
    b = 1000

if n > 1000:
    c = (n//1000) * 1000
result = c + b
print(result)

'''


 


















'''
a = int(input())
c = 0
n = 0
result = 0

n = a % 1000
if n <= 500:
    n = 0
else:
    n = 1000
    
c = a // 1000
result = (c * 1000) + n
print(result)
'''




   
    
    
a = int(input())
n = (a // 1000) * 1000
k = a % 1000


if k <= 500:
    print(n)
elif k > 500:
    print(n+1000)