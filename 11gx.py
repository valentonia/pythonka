pv = float(input())
num = int(input())
key = []
value = []
list2 = [0]

for i in range(num):
    a = input().split()
    key.append(float(a[0]))
    value.append(float(a[1]))
max_2 = 0
max_3 = 0
result_1 = 0
result_2 = 0
result_3 = 0

for i in range(num):
    max_1 = key[i]
    if max_1 > pv:
        continue
    else:
        result_1 = value[i]
        list2.append(result_1)
    for j in range(i + 1,num):
        max_2 = max_1 + key[j]
        if max_2 > pv:
            continue
        else:
            result_2 = result_1 + value[j]
            list2.append(result_2)
        for k in range(j + 1,num):
            max_3 = max_2 + key[k]
            if max_3 > pv:
                continue
            else:
                result_3 = result_2 + value[k]
                list2.append(result_3)
  
print(round(float(max(list2)),2))