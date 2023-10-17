x = input()
y = ""

for i in x:
    if i not in y:
        y += i
    else:
        continue
print(y)
