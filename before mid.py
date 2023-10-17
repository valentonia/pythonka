'''
n = int(input())
print(n**2)

'''
'''
x = int(input())
y = int(input())
z = int(input())
print(round((x+y+z)/3,2))
'''
'''
money = int(input())
if money > 0:
    THB = money * 30.85
    print(round(THB,2))
'''
'''
n = int(input())
print(n*'*')
'''
'''
w = int(input())
h = int(input())
if 1 < w < 20 and 1 < h < 20:
    print((w*'*'+'\n')*h)
else:
    print("Invalid input")
'''
'''
w = int(input())
h = int(input())

BMI = (w/((h/100)**2))

print(BMI)
'''
'''
mon = int(input())
cur = str(input())

if 0 < mon < 1000000:
    if cur == "USD":
        print (mon // 34.20, "THB")
        print (round(mon % 34.20,2),"THB")
    elif cur == "EUR":
        print (mon // 38.47, "THB")
        print (round(mon % 38.47,2),"THB")
    elif cur == "GBP":
        print (mon // 44.73, "THB")
        print (round(mon % 44.73,2),"THB")
    elif cur == "JPY":
        print (mon // 24.76, "THB")
        print (round(mon % 24.76,2),"THB")
else:
    print("Invalid input")
'''
'''
n = int(input())
if 0 < n < 20:
    for i in range(n,-1,-1):
        print(i)
else:
    print("Invalid input")  
'''
'''
n = int(input())
if 0 < n < 20:
    for i in range(n):
        print(i*' ','*')
else:
    print("Invalid input")
'''
'''
n = int(input())
if 0 < n < 20:
    for i in range(n):
        print(i*' ',(n-i)*'*')
else:
    print("Invalid input")
'''
'''
xa1 = int(input())
xa2 = int(input())
ya1 = int(input())
ya2 = int(input())

xb1 = int(input())
xb2 = int(input())
yb1 = int(input())
yb2 = int(input())

if (xa2 <= xb1) or (xb2 <= xa1) or (ya2 >= yb1) or (yb2 >= ya1):
    print(0)
else:
    x1 = max(xa1,xb1)
    x2 = min(xa2,xb2)
    y1 = max(ya2,yb2)
    y2 = min(ya1,yb1)
    
    w = x2-x1
    h = y2-y1

    print(w*h)
'''
'''
n = int(input())
fspace = 0
mspace = n-2
# top part
if 1 < n < 29 or n%2 == 0:
    while True:
        if fspace > 0:
            print ((fspace*' ')+'\\'+(mspace*' ')+'/')
        fspace += 1
        mspace -= 1
        
else:
    print("Invalid input")
'''
'''
n = int(input())
fspace = 0
mspace = n-2


if 29 < n < 1 or n%2 == 0:
    print("Invalid input")
else:
    # top part
    while True:
        if mspace > 0:
            print ((fspace*' ')+'\\'+(mspace*' ')+'/')
            fspace += 1
            mspace -= 2
        else:
            break
    #mid part
    print((n//2)*' '+'X')
    #bottom part
    fspace = 1
    mspace = 1
    while True:
        if fspace >= 0:
            print ((fspace*' ')+'/'+(mspace*' ')+'\\')
            fspace -= 1
            mspace += 2
        else:
            break
'''
'''
n = int(input())
m = int(input())

if n > 0 and m > 0:
    for i in range(n):
        for j in range(i+1,m+1):
            if j % m == 0:
                print(j)
            else:
                print (j, end=' ')
           
else:
    print("Invalid input")
'''
'''
n = int(input())
m = int(input())
for i in range(1,n+1):
    print(i, end=' ')
    if i % m == 0:
        print()
'''
'''
n = int(input())
m = int(input())
if n <= 0 or m <= 0:
    print("error")
elif n>=m:
    for i in range(1,m+1):
        for j in range(i,n+1,m):
            print(j, end= ' ')
        print()
else:
    for i in range(1,n+1):
        print(i)         
'''
'''
n = int(input())
m = int(input())

for i in range(m):
    for j in range(n):
        if (i+j)%3 == 0:
            print (0,end='')
        elif (i+j)%3 == 1:
            print (1,end='')
        elif (i+j)%3 == 2:
            print(2,end='')
    print()
'''
'''
n = int(input())
m = int(input())

for i in range(m):
    for j in range(n):
        if (i+j)%3 == 0:
            print (0, end='')
        elif (i+j)%3 == 1:
            print (1, end='')
        elif (i+j)%3 == 2:
            print (2, end='')
    print()       
''' 
''' 
n = int(input())
m = int(input())

for i in range(m):
    for j in range(n):
        print((i+j)%3, end="")
    print()
'''
'''
sum = 0
while True:
    x = input()
    if x == '$':  
        break
    else:
        x = int(x)
        sum += x
print(sum)  
'''
'''
min = 0
max = 0
count = 0
while True:
    num = input()
    if num == '$':
        break
    else:
        num = int(num)
        if count == 0:
            min = num
            max = num
        elif num < min:
            min = num
        elif num > max:
            max = num     
    count += 1
    
if count == 0:
    print("Invalid input")
else:
    print(min)
    print(max)
'''
'''
n = int(input())
if 1 < n < 1000:
    for i in range(1,n+1):
        if n % i == 0:
            print (i)
else:
    print("Invalid input")    
'''
'''
n = int(input())
if 2 < n < 10:
    for i in range (1,n+1):
        for j in range (i,n+1):
            for k in range (j,n+1):
                if i < j < k <= n:
                    print ('('+str(i)+','+str(j)+','+str(k)+')')      
'''
'''
hr = int(input())
min = int(input())
ex_min = int(input())
new_day = 0

new_min = (min+ex_min) % 60
new_hr = hr + ((min+ex_min)//60)
new_day = new_hr // 24
new_hr = new_hr % 24

if new_min < 10:
    if new_hr == 0:
        print('0'+ str(new_hr)+':'+'0'+str(new_min),end = '')
    else:
        print(str(new_hr)+':'+'0'+str(new_min),end = '')
elif new_min >= 10:
    print(str(new_hr)+':'+ str(new_min), end= '')
if new_day == 1:
    print (' +',new_day,'day')
elif new_day > 1:
    print (' +',new_day,'days')
elif new_day == -1:
    print (' -',-new_day,'day')
elif new_day < -1:
    print (' -',-new_day,'days')
'''
'''
lis = []
while True:
    n = (input())
    if n == '$':
        break
    if int(n) >= 0:
        lis.append(int(n))
    if int(n) < 0:
        continue
    
if len(lis) <= 0:
    print(None)
else:
    print(min(lis))        
'''
'''
min = 0
max = 0
count = 0
while True:
    n = input()
    if n == '$':
        break
    if count == 0:
        min = n
        max = n
    
    if len(n) < len(min):
        min = n
    if len(n) > len(max):
        max = n
    count += 1      
print(min)
print(max)        
'''
'''
n = int(input())
ball = 1

while True:
    print (ball)
    ball = (ball+3)%n
    
    if ball == 1:     
        break
    elif ball == 0:
        ball = n
'''
'''

n = int(input())
ball = 0
while True:
    print(ball+1)
    ball = (ball+3) % n
    
    if ball == 0:
        break
'''
'''
team = int(input())
mem = int(input())
max = 0
winteam = 0

for t in range(1,team+1):
    min = 0
    for m in range(mem):
        score = int(input())
        if score < min:
            min = score
    if min > max:
        max = min
        winteam = t
print ('Team',winteam)      
'''
'''
old_num = input()
old_diff = 0
if old_num == '$':
    print ("insufficient data")
else:
    new_num = (input())
    if new_num == '$':
        while True:
            diff = abs(int(new_num)-int(old_num))
            if old_diff < diff:
                old_diff = diff
            old_num = new_num
            new_num = input()
            if new_num == '$':
                print(old_diff)
                break
'''
'''
max1 = 0
max2 = 0
max3 = 0
old_num = input()


if old_num == '$':
    print ("Insufficient")
else:
    while True:
        num = input() 
        if num == '$':
            print(max1)
            break
        
        if int(num) > max1:
            max1 = num
            
        if int(num) < max1:
            max2 = num
print(max1)
print(max2)
'''
'''
n = int(input())
y = ''

if n in range(0, (2**20)+1):
    while n > 0:
        y = str(n%2) + y
        n = n // 2
    print(y)
else:
    print("Invalid")
'''
'''
n = int(input())
y = 0
if n in range(-2**40,2**40):
    if n < 0:
        n = (n*-1)
    while n > 0:
        y = y + (n%10)
        n = n // 10
        
    print(y)    
'''
'''
n = int(input())
y = ''
if n in range(0,(2*20)+1):
    while n > 0:
        y = str(n % 2) + y
        n = n // 2
    print(y)
else:
    print("Invalid input")    
'''
'''
n = int(input())
y = 0
if n in range((-2**24),2**24):
    if n < 0:
        n = (n*-1)
    while n > 0:
        y = y + (n%10)
        n = n // 10
    print(y)
'''
'''       
n = float(input())
print (n.__ceil__())
'''
'''
num = int(input())
sum = 0 

for number in range(num+1):
    for char in str(number):
        sum = sum + int(char)
    if int(sum) == 9:
        print(number)       
    sum = 0  
'''
'''
n1 = (input())
diff_max = 0
if n1 == '$':
    print("Invalid")
else:
    n2 = input()
    if n2 == '$':
        print("Invalid")
    else:
        while True:
            diff = abs(int(n1)-int(n2))
            if diff > diff_max:
                diff_max = diff
            n2 = (input())
            if n2 == '$':
                break
    print (diff_max)
'''

'''
num1 = input()
diff_max = 0

if num1 == '$':
    print("invalid")
else:
    num2 = input()
    if num2 == '$':
        print("invalid")
    else:
        while True:
            diff = abs(int(num1) - int(num2))
            if diff > diff_max:
                diff_max = diff
            num2 = input()
            if num2 == '$':
                break
    print (diff_max)
'''
'''
n1 = input()
diff_max = 0
if n1 == '$':
    print('invalid')
else:
    n2 = input()
    if n2 == '$':
        print('invalid')
    else:
        while True:
            diff = abs(int(n1)-int(n2))
            if diff > diff_max:
                diff_max = diff
            n2 = input()
            if n2 == '$':
                break
        print(diff_max)
'''
'''
n = int(input())
m = int(input())

for i in range(1,n+1):
    print(i, end = ' ')
    if i % m == 0:
        print()
'''
'''
sum = 0
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    if n:
        sum += n
print(sum)
'''
'''
min = 0
max = 0
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    if n < min:
        min = n
    if n > max:
        max = n
print(min)
print(max)
'''
'''
n = int(input())
if n <= 0:
    print("invalid")
else:
    for num in range(1,n+1):
        if n % num == 0:
            print(num)
'''
'''
n = int(input())
if 2 < n < 10:
    for i in range(1,n+1):
        for j in range(i,n+1):
            for k in range(j,n+1):
                if i < j < k <= n:
                    print('('+str(i)+','+str(j)+','+str(k)+')')    
'''
'''
hr = int(input())
min = int(input())
ex_min = int(input())
day = 0 

new_min = (min + ex_min) % 60
new_hr = hr + ((min+ex_min) // 60)
new_day = new_hr // 24
new_hr = new_hr % 24

if new_min < 10:
    if new_hr == 0:
        print(('0'+str(new_hr)+':'+'0'+str(new_min)),end = '')
    else:
        print((str(new_hr)+':'+'0'+str(new_min)),end = '')
elif new_min >= 10:
    print(str(new_hr)+':'+str(new_min))
if new_day == 1:
    print(' +',new_day,'day')
if new_day > 1:
    print(' +',new_day,'days')
if new_day == -1:
    print(' -',-new_day,'day')
if new_day < -1:
    print(' -',-new_day,'days')
'''
'''
a = int(input())
n = (a // 1000) * 1000
k = a % 1000


if k <= 500:
    print(n)
else:
    print(n+1000)                 
'''

min = float('inf')
lis = []
while True:
    n = input()
    
    if n == '':
        break
    n = int(n)
    lis.append(n) 
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        g = abs(lis[i] - lis[j])
        
        if g < min:
            min = g
print(min)    
        
        
            
                












     
        

