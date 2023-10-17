n = int(input())
if n in range (1,30) and n % 2 == 1:
        for x in range (0, n//2):
                print(" "*x + "\\" + " "*(n-2*(x+1)) + "/")
        print (" "*(n//2) +"X")
        for y in range(n//2, 0, -1):
                print(" "*(y-1) + "/" + " "*(n-2*y) + "\\")
else:
  print("Invalid input")