import math
avg = 0
sun = 0
lis = []
sd = 0
diff_square = 0
variance = 0
n = int(input())

for i in range(n):
    n1 = int(input())
    if 1 <= n1 <= 1000000:
        lis.append(n1)

        sun += int(lis[i])
    mean = sun / n

for j in range(n):
    diff_square += ((int(lis[j])-mean)**2)
    variance = diff_square / n
    sd = round(math.sqrt(variance),2)

max_bond = mean + sd
min_bond = mean - sd

lis.sort()
lis1 = lis[:]
for y in range(len(lis)):  
    if max_bond < int(lis[y]) or int(lis[y]) < min_bond:
        lis1.remove(lis[y])

num = sum(int(lis1[x]) for x in range(len(lis1)))
avg = num / len(lis1)
print(round(avg,2))