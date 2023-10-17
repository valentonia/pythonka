'''
i=0
max=0
count=0
while 0<1:
    a=input()
    if a=='$':
        break
    else:
        a=int(a)
        if i==0:
            same=a
            count=1
        else:
            if a==same:
                count+=1
            else:
                if count>max:
                    max=count
                same=a
                count=1
    i+=1   

#if count>max:
# max=count 
print(max)
'''

count = 0
i = 0
max = 0
while True:
    n = input()
    if n == '$':
        break
    else:
        n = int(n)
        if i == 0:
            same = n 
            count = 1
            i = 1
        elif i >= 1 :
            if n == same:
                count += 1
            else:
                count = 1
            if count > max:
                max = count
                
        i += 1
        same = n
print(max)        
            