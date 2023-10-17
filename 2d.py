x = int(input())
y = int(input())
z = int(input())

if (z<=x<=y) or (y<=x<=z):
 print (x)
elif (z<=y<=x) or (x<=y<=z):
 print (y)
elif (y<=z<=x) or (x<=z<=y):
 print (z)