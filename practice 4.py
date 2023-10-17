
lis = []
lis1 = []
diff = 0
max_diff = 0
while True:
    n = input()
    if n == '$':
        break
    else:
        n = int(n)
        lis.append(n)
        
        print(lis)
        
for i in range(1,len(lis)):
    diff = lis[i-1] + lis[i]
    lis1.append(diff)
    
    if int(lis1(diff)) < 0:
        diff *= (-1)
    else:
        diff *= 1
    
    if diff > max_diff:
        max_diff = diff
print(lis1)
print(max_diff)
'''
'''
dic = {}
lis = []
max_v = 0
while True:
    n = input()
    if n == '$':
        break
    else:
        name = n.split()[0]
        value = int(n.split()[1])
        if name in dic:
            dic[name] += value
        else:
            dic[name] = value
            
max_v = max(dic.values())

end = []
for name,value in dic.items():
    if value == max_v:
        end.append(name)
        
end.sort()
for i in range(len(end)):
    print(end[i])
'''
'''
b = 0
min_b = 0
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    b += n
    
    min_b = min(min_b,b)
    
print (abs(min_b))
'''   
''' 
sum = 0
price = input().split()
quant = input().split()

for i in range(len(price)):
    sum += (float(price[i])*int(quant[i]))
print(round(sum,2))
''' 
'''

n = int(input())
bin = ''

if n == 0:
    bin = '0'
else:
    bin = ''
    while n != 0:
        if n % 2 == 0:
            bin = '0' + bin
        elif n % 2 == 1:
            bin = '1' + bin
            
        n = n // 2
    print(bin)
'''
'''
lis = []
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    lis.append(n)
print(sum(lis))      
'''
'''
lis = []
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    lis.append(n)
print(max(lis))
''' 
'''
lis = []
up = 0
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    lis.append(n)
    
    avg = sum(lis) / len(lis)
for i in range(len(lis)):
    up += (int(lis[i]) - avg) ** 2
ans = (up/len(lis)) ** (1/2)
print(round(ans,2))
'''
'''
lis = []
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    lis.append(n)
    lis.sort()
    
    if len(lis) % 2 == 0:
        median = float((lis[len(lis)//2]+lis[((len(lis)//2)-1)])/2)
    elif len(lis) % 2 == 1:
        median = float(lis[len(lis)//2])
        
print(median)
'''
'''
n = int(input())
fav = set(input().split())

for i in range(n-1):
    like = input().split()
    fav.intersection_update(like)

if fav:
    print(' '.join(sorted(fav)))
else:
    print("Nothing")
'''
'''
first = 0
max_l = 0
count = 0
while True:
    n = input()
    if n == '$':
        break
    else:
        if first == 0:
            same = n 
            count = 1
        else:
            if n == same:
                count += 1
            else:
                if count > max_l:
                    max_l = count
                
                same = n
                count = 1  
            
    first += 1
print(max_l)
'''
'''
dic = {}
n = int(input())
for i in range(n):
    food = input()
    
    if food in dic:
        dic[food] += 1
    else:
        dic[food] = 1
        
sor = [(dic[x],x) for x in dic]
sor.sort()

for (v,k) in sor:
    print(k,v)
'''
'''
n = int(input())
if 0 < n < 1000000:
    if n % 7 == 0:
        b = n // 7
        print(b)
    else:
        a = (n//7) + 1
        print(a)
'''
'''
import math
n = int(input())
if 0 < n < 1000000:
    b = math.ceil(n/7)
print(b)
'''
'''
lis = []
n = int(input())
for i in range(n):
    num = int(input())
    lis.append(num)
    avg = sum(lis) / len(lis)
upper = 0
for  j in range(len(lis)):
    upper += ((lis[j] - avg) ** (2))
    before = upper / len(lis)
sd = before ** (1/2)
min_b = avg - sd
max_b = avg + sd
lis1 = lis[:]
for a in range(len(lis1)):
    if int(lis[a]) < min_b or int(lis[a]) > max_b:
        lis1.remove(int(lis[a]))
new_avg = sum(lis1) / len(lis1)
print(round(new_avg,2))
'''
'''
lis_p = []
lis_q = []

p = (input().split())
q = (input().split())

for i in p:
    lis_p.append(int(i))
for j in q:
    lis_q.append(int(j))
    
result = [0] * (len(lis_p) + len(lis_q) -1)

for i in range(len(lis_p)):
    for j in range(len(lis_q)):
        result[i + j] += lis_p[i] * lis_q[j]
        
for k in result:
    print(int(k), end = ' ')
'''
'''
dic = {}
max_v = 0

while True:
    n = input()
    if n == '$':
        break
    else:
        
        name = n.split()[0]
        value = int(n.split()[1])
        
        if name in dic:
            dic[name] += value
        else:
            dic[name] = value
            
max_v = max(dic.values())
lis = []
for (k,v) in dic.items():
    if v == max_v:
        lis.append(k)
        lis.sort()

for i in range(len(lis)):
    print(lis[i])
'''
'''
min_b = 0
b = 0
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    b += n 
    min_b = min(min_b,b)
print(min_b)
'''
'''
s1 = input().split()
s2 = input().split()

c = s1+s1
for i in range(len(c)):
    if c[i:i+len(s1)] == s2 or c[i-len(s1):i:-1]:
        print("same")
        break
    else:
        print("different")
        break
'''
'''

p = input().split()
q = input().split()

lis_p = [int(x) for x in p]
lis_q = [int(x) for x in q]

result = [0] * ((len(lis_p)+len(lis_q)) - 1)

for i in range(len(lis_p)):
    for  j in range(len(lis_q)):
        result[i+j] += lis_p[i] * lis_q[j]
        
for i in range(len(result)):
    print(result[i], end =' ' )
'''
'''
s1 = input().split()
s2 = input().split()

c = s1+s1

for i in range(len(c)):
    if c[i:i+len(s1)] == s2 or c[len(s1)+i:i:-1] == s2:
        print("same")
        break
    else:
        print("different")
        break 
    
    
