n = int(input())
m = int(input())
if m <= 0 or n <= 0:
 print ("Invalid input")

# ปริ้น จน แถวนอน
for i in range(1,m+1):  
   
  for j in range(i,n+1,m): 
    if j > n: 
     break
    print(j,end=" ")
  print ()
