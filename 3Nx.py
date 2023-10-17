n = int(input())
m = int(input())
listmin = []

for i in range(n):
    list = []
    for j in range(m):
        score = int(input())
        list.append(score)
    listmin.append(min(list))
    
print("Team",listmin.index(max((listmin)))+1)
