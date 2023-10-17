num = int(input())
coor = input()
min_x = int(coor.split(" ")[0])
max_x = int(coor.split(" ")[0])
min_y = int(coor.split(" ")[1])
max_y = int(coor.split(" ")[1])


def min(a,b):
    if a <= b:
        return a
    else: 
        return b
    
def max(a,b):
    if a >= b:
        return a
    else:
        return b 
    
for _ in range(num-1):
    coor_i = input()
    min_x = min(min_x, int(coor_i.split(" ")[0]))
    max_x = max(max_x, int(coor_i.split(" ")[0]))
    min_y = min(min_y, int(coor_i.split(" ")[1]))
    max_y = max(max_y, int(coor_i.split(" ")[1]))
    
print (max((max_x-min_x), (max_y-min_y))**2)