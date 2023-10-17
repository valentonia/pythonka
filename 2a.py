n = int(input())
m = int(input())
if m <= 0 or n <= 0:
  print ("Invalid input")

# ปริ้น จน แถวตั้ง
for i in range(1,m+1):  
  #ปริ้น จน แถวนอน
  for j in range(i,n+1,m): 
    # ถ้า จน แถวแนอนปริ้นไปจนเกิน 20 แล้ว ให้หยุด
    if j > n: 
      break
    print(j,end=" ")
  print ()
