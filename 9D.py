lis = []
while True:
    n = input()
    if n == '$':
        break
    n = float(n)
    lis.append(n)
    lis.sort()
    

if len(lis) % 2 == 0:
    median = (lis[len(lis) // 2] + lis[(len(lis)//2) -1 ]) / (2)
    print(round(median,2))
if len(lis) % 2 == 1:
    median1 = (lis[len(lis) // 2])
    print(round(median1,2))


    