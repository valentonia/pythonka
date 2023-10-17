a = input().split()
b = input().split()
lis1 = []

for i in range(len(b)):
    count = 0
    for j in range(len(a)):
        if i == 0:
            x = int(b[i])*int(a[j])
            lis1.append(x)
        else:
            if count + i == len(lis1):
                x = int(b[i])*int(a[j])
                lis1.append(x)
            else:
                x = int(b[i])*int(a[j])
                lis1[count+i] = lis1[count+i] + x
                count += 1
for k in lis1:
    print(k,end=' ')












