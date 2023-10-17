n = []

while True:
    x = input()
    if x == "$":
        break
    if int(x) < 0:
        continue
    if int(x) in n:
        continue
    if int(x) >= 0:
        n.append(int(x))

n.sort()
n.reverse()
if len(n) > 0:
        print(n[0])
        if len(n) > 1:
            print(n[1])
        if len(n) > 2:
            print(n[2])
        
else:
    print ("Insufficient data") 