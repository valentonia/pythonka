x = float(input())
y = str(input())
if y == "USD":
 print (int(x//34.2))
 print (round (x%34.2,2))
elif y == "EUR":
 print (int(x//38.47))
 print (round (x%38.47,2))
elif y == "GBP":
 print (int(x//44.73))
 print (round (x%44.73,2))
elif y == "JPY":
 print (int(x//0.2476))
 print (round (x%(24.76/100),2))




