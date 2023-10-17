'''
x = int(input())
print (x**2)
'''
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())
print (round((num1+num2+num3)/3,2))
'''
'''
mon = float(input())
current = str(input())

if current == 'USD':
    print (round(mon*30.85),2)
'''
'''
n = int(input())
if n > 0:
    print(n*'*')
else:
    print("Invalid input")
'''
'''
width = int(input())
height = int(input())
if width > 0 and height > 0:
    print((width*'*'+'\n')*height)
else:
    print('error')
'''
'''
x = int(input())
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
'''
'''
weight = int(input())
height = int(input())

BMI = (weight/((height/100)**2))

if BMI < 18.5:
    print(BMI)
    print("Below normal weight")
elif 18.5 <= BMI < 25:
    print(BMI)
    print("Normal weight")
elif 25 <= BMI < 30:
    print(BMI)
    print("Overweight")
elif 30 <= BMI < 35:
    print(BMI)
    print("Class I Obesity")
elif 35 <= BMI < 40:
    print(BMI)
    print("Class II Obesity")
else:
    print(BMI)
    print("Class III Obesity")
'''
'''
THB = int(input())
cur = str(input())

if cur == 'USD':
    print(int(THB/34.20))
    print(round(THB%34.20,2))
    
'''
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num2 <= num1 <= num3 or num3 <= num1 <= num2:
    print(num1)
elif num1 <= num2 <= num3 or num3 <= num2 <= num1:
    print(num2)
else:
    print(num3)
'''
'''
n = int(input())
for i in range(n,-1,-1):
    print(i)
'''
'''
n = int(input())

if n > 0:
    for i in range(n):
        print(i*' ',1*'*')
else:
    print("Invalid input")
'''
'''
n = int(input())
if 20 > n > 0:
    for i in range(n):
        print(i*' ',(n-i)*'*')
else:
    print("Invalid input")
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

if xa2 >= xb1 or yb1 <= ya2 or ya1 <= yb2 or xb2 >= xa1:
    x1 = min(xa1,xb1)
    x2 = max(xa2,xb2)
    y1 = min(ya1,yb1)
    y2 = max(ya2,yb2)
    w = x2-x1
    h = y1-y2
    print (w*h)
else:
    print(0)
'''
'''
num=int(input())
if num<1 or num>29 or num%2==0:
    print("Invalid input")
else:
    for i in range(num//2):
        print(" "*i+"\\"+" "*(num-(2*i)-2)+"/")
    print(" "*((num//2))+"X")
    for i in range(num//2-1,-1,-1):
        print(" "*i+"/"+" "*(num-(2*i)-2)+"\\")
'''
'''
n = int(input())
m = int(input())
if n > 0 and m > 0:
    for i in range(1,n+1):
        print(i,end = '')
        if i % m == 0:
            print('\n',end = '')
        elif i != n:
            print(' ',end = '')
else:
    print("Invalid input") 
'''
'''
n = int(input())
m = int(input())

if n >= 0 and m >= 0:
        for i in range(1, m+1):
            for j in range(i,n+1,m):  
                if j > n:
                   break
                print(j, end= ' ')
            print()
else:
    print("Invalid input")
    
'''
'''
n = int(input())
m = int(input())

y = 0
for i in range(m):
    for j in range(n):
        print(y, end ='')
        y = (y+1)%3
    print()
'''
'''
num_so_far = 0
while True:
    num = input()
    if num == "$":
        break
    else:
        num = int(num)
        num_so_far += num
print(num_so_far)
'''
'''
max = 0
min = 0
while True:
    num = input()
    if num == '$':
        print("Invalid input")
        break
    else:
        if int(num) > max:
            max = int(num)
        if int(num) < min:
            min = int(num)
print(max)
print(min)
'''
'''
num = int(input())
if num < 0:
    print("Invalid input")
else:
    for i in range(1,num+1):
        if num % i == 0:
            print(i)
'''
'''
n = int(input())
if 2 < n < 10:
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                if i < j < k:
                    print("("+str(i)+","+str(j)+","+str(k)+")")
                else:
                    print("Invalid input")
                    
'''
'''
price_t = int(input())
price_k = int(input())
money = int(input())

v_t = money//price_t
v_k = money//price_k

for t in range(v_t,-1,-1):
    for k in range(0,v_k+1):
        total_cost = t*price_t + k*price_k
        if total_cost == money:
            print("Teddy bear:",t,"Kitty doll",k)
    
'''
'''
def num(min):
    if min >= 10:
        return str(min)
    else:
        return '0' + str(min)
    

hr = int(input())
min = int(input())
min_add = int(input())

day = 0
new_m = (min+min_add)%60
new_h = hr + ((min+min_add)//60)
day = new_h // 24
new_h = new_h % 24

print(num(new_h)+":"+num(new_m), end="")
if day == 1:
    print(" +",day,"day")
elif day > 1:
    print(" +",day,'days')
elif day == -1:
    print(" -",-day,"day")
elif day < -1:
    print(" -",-day,"days")
'''
'''
m = 0
list = []
while True:
    x = input()
    if x == '$':
        if list == []:
            print(None)
        else:
            print(min(list))
        break
    else:
        if int(x) >= 0:
            list.append(int(x))
        elif int(x) < 0:
            continue
'''
'''
num = int(input())

emt = ''
if 0 <= num <= (2**20):
    while num > 0:
        b = num % 2
        num = num // 2
        emt = str(b) + emt
    
    if emt == '':
        emt = '0'
    
    print(emt)
         
else:
    print("Invalid input")
'''
'''
num = int(input())
emt = 0
if -2400 < num < 240000:
    if num < 0:
        num = (num*-1)
    while num > 0:
        emt = emt + (num%10)
        num = num // 10
    print(emt)
    
else:
    print("Error")
'''
'''
num = int(input())
list = []
emt = 0 

if -2400 < num < 240000:
    if num < 0:
        num = (num*-1)
    while num > 0:
        if num %10 in list:
            num = num // 10
            
        else:
            list.append(num%10)
            emt = emt + (num%10)
            num = num // 10
    print(emt)
'''
'''
def min (x,y,z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z

a = int(input())
b = int(input())
c = int(input())   
print(min(a,b,c)) 
'''
'''
def progress (step = 1, num = 10):
    for i in range(num):
        print(i)


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
    if num2!=None and num3!=None:
        value = (round((num1+num2+num3)/3,2))
    elif num2 != None:
        value = (round((num1+num2)/2,2))
    else:
        value = float(num1)
        
    return value

a = int(input())
b = int(input())
c = int(input())
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))
'''
'''
team = int(input())
members = int(input())
winning_score = 0
min_score = 0
member_score = 0
winning_team = 0

for i in range (1,team+1):
    min_score = int(input())
    for j in range(members-1):
        member_score = int(input())
        if member_score < min_score:
            min_score = member_score
    if min_score > winning_score:
        winning_score = min_score
        winning_team = i    
    
print("Team", winning_team )
'''
'''
team = int(input())
member = int(input())
min_score = 0
member_score = 0
winning_score = 0


for i in range(1,team+1):
    min_score = int(input())
    for j in range(member-1):
        member_score = int(input())
        if member_score < min_score:
            min_score = member_score
            
    if min_score > winning_score:
        winning_score = min_score
        winning_team = i
print("Team", winning_team)
'''
'''
n = int(input())
m = int(input())
listmin = []

for i in range(n):
    list = []
    for j in range(m):
        score = int(input())
        list.append(score)
    listmin.append(min(list))
    
print("Team",listmin.index(max((listmin)))+1)
'''
'''
def fun(n):
    if n == 1:
        print(n)
    else:
        print(n)
        fun(n-1)
fun(int(input()))
'''
'''
def fun(n):
    if n == 1:
        print(n*'*')
    else:
        print(n*'*')
        fun(n-1)
fun(int(input()))

'''
'''
def binary(n):
    if n % 2 == 0:
        return '0'
    elif n % 2 == 1:
        return '1'
    else:
        return binary(n//2) + str(n%2)
binary(int(input()))
'''
'''
count = 0
txt = input()
for i in txt:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
    
    if count < 0:
        break

if count == 0:
    print("True")
else:
    print("False")
'''
'''
n = int(input())
if n > 3:

else:
    print("Invalid input")
'''
p_teddy = int(input())
p_kitty = int(input())
money = int(input())

max_t = money // p_teddy
max_k = money // p_kitty

for i in range(max_t,-1,-1):
    for j in range(0,max_k+1):
        totalcost = j*p_kitty + i*p_teddy
        if totalcost == money:
            print ("Teddy:",i,"Kitty doll",j)























