n = int(input())
count = {}
for i in range(n):
        food = input()
        if food in count:
            count[food] += 1
        else:
            count[food] = 1

count = list(count.items())
count.sort(key=lambda x: (x[1], x[0]))

for food, counter in count:
    print(food,counter)
