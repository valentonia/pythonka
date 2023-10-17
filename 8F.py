'''
x = input()
y = ''
z = ''
n = ''
for i in x:
    y = i+y
    z += i
if y == z:
    n = True
else:
    n = False
print(n)
'''

n = input()
y = n[::-1]
if y == n:
    print("True")
else:
    print("False")
    
    