x = int(input())
if x <= 20 and x >= 1:
  for i in range (x,-1,-1):
    print(((x - i)*" ")+(i*"*"))
else:
  print("Invalid input")