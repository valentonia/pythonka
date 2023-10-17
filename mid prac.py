min = ""
max = ""
count = 0
while True:
    x = input()
    if count == 0:
        min = x
        max = x
    if x == "$":
        print (min)
        print (max)
        break
    if len(x) > len(max):
        max = x
    if len(x) < len(min):
        min = x
    count += 1
    
    