n = []
while True:
    x = input()
    if x == "$":
        break
    if int(x) < 0:
        continue
    if int(x) >= 0:
        n.append(int(x))
if len(n) > 0:
    print(min(n))
else:
    print("None")
