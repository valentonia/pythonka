'''
x = int(input())
min = int(x)
max = int(x)
dif = 0
count = 0


while True:
    x = int(input())
    count = 0
    if count == 0 and x == '$':
        print ("Insufficient data")
        break
    elif count == 1:
        print ("Insufficient data")
        break
    elif count > 1:
        for i in range(x):
                if int(x) > int(max):
                    max = int(x)
                
                if int(x) < int(min):
                    min = int(x)

        dif = max - min
        count += 1
        
    print(dif)
'''
'''
old_dif = 0
old_num = input()
if old_num != '$':
    
    new_num = input()
    if new_num != '$':
        
        while True:
            new_dif = abs(int(old_num)-int(new_num))
            
            if new_dif > old_dif:
                old_dif = new_dif
            old_num = new_num
            try:
                new_num = int(input)
            except:
                print(old_dif)
                break    
        
    else:
        print("Insufficient data")
else:
    print("Insufficient data")
'''

n = int(input())
zero = n // 2
one = 1
for i in range(n//2):
    a = '0' * zero
    b = '1' * one
    
    print (a + b + a)
    zero -= 1
    one += 2

print ('1' * n)

for i in range(n//2):
    a = '0' * zero
    b = '1' * one
    
    print (a + b + a)
    zero += 1
    one -= 2


