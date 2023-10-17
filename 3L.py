t = int(input()) #amount of teddy
k = int(input()) #amount of kitty
m = int(input()) #money
ans_found = False
#a = int(input()) teddy's price
#b = int(input()) kitty's pricey

for x in range (m//t,-1,-1):
    if (m-t*x) % k == 0:
        ans_found = True
        y = (m - t*x) // k
        print ("Teddy bear:",x,"Kitty doll:",y)
        
        
if not ans_found:
     print("Not possible")
     
    
