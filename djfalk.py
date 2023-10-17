n = []
x = input()
n.append(x)
if len(n) > 0:
    for i in range(0,3):
        print(max(n))
        n.remove(max(n))