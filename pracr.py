b = float(input())
n = int(input())
price = []
future = []
diff = 0 
diff_lis = []
top = 0
test = 0
top1 = 0
top2 = 0
top3 = 0


for i in range(n):
    pv = input()
    p = float(pv.split()[0])
    price.append(p)
    v = float(pv.split()[1])
    future.append(v)

for j in range(len(price)):
    diff = float(future[j]) - float(price[j])   
    diff_lis.append(diff)
    
    
for a in range(len(price)):
    if float(diff_lis[a]) > 0:

        for first in range(len(price)):
            for second in range(first+1,len(price)):
                for third in range(second+1,len(price)):
                    test += price[second]

        
        
        
        
        
        
        if float(price[a]) <= b:
            top += float(future[a])    
print(test)    
print(float(top))
print(diff_lis)
print(price)
print(future)
