'''
def backward(b):
    k=[b[0]]
    for i in range(-1,-len(b),-1):
        k.append(b[i])
    return k
def find_same(a,b):
    count=0
    while True:
        back=backward(b)
        if count==len(a):
            return 'different'
        if a==b or a==back:
            return 'same'
        first_item=b[0]
        b.remove(first_item)
        b.append(first_item)    
        count+=1

print(backward([0, 1, 2, 3]))

a=input().split()
b=input().split()
print(find_same(a,b))
'''

s1 = input().split()
s2 = input().split()
c = s1 + s1
count = 0

for i in range(len(c)):
    if c[i:i+len(s2)] == s2 or c[i+len(s2):i:-1] == s2:
     count += 1
     
if count > 0:
    print('same')
else:
    print('different')

