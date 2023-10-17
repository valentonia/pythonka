n = input()
l = '('
r = ')'
count_l = 0
count_r = 0

for x in n:
    if count_r > count_l:
        break
    if l == x:
        count_l += 1
    elif r == x:
        count_r += 1
        
if count_r == count_l:
    print("True")
else:
    print("False")
