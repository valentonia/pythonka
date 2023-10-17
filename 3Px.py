n = []
q = []
t = []
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

if len(n) > 0:
        print(max(n))
        n.remove(max(n))
        q.extend(n)
        print(max(q))
        t.extend(n)
        print(max(t))
        
        
    
else:
    print ("Insufficient data") 

     