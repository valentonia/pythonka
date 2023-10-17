'''
x = input()
z = ''
count = ''
for i in x:
    if count == '':
        count += i
    elif count[0] == i:
        count += i
    else:
        if len(count) > 1:
            z += str(len(count))
        z += count[0]
        count = ''
        
        count = i

if count:
    if len(count) > 1:
        z += str(len(count))
    z += count[0]
    
print(z)
'''

n = input() + '0'
count = 0
ori = n[0]
for i in n:
    if ori == i:
        count += 1
    else:
        if count == 1:
            print(ori, end = '')
        else:
            print(str(count)+ori, end = '')
        
        ori = i
        count = 1