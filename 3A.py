n = int(input())
m = int(input())
if m <= 0 or n <= 0:
 print ("Invalid input")

for i in range((n//m)+1): #1
  sun = 1+(m*i) 
  for j in range(sun,sun+m): 
    if j > n:  
     break
    print(j,end=" ")
  print() #เว้นบรรทัด


 
