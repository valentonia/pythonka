price = input().split()
product = input().split()
lis_price = []
lis_products = []
#products = (input())
n = 0

for i in price:
    lis_price.append(float(i))
for j in product:
    lis_products.append(float(j))
for x in range(len(price)):
    sum = lis_price[x]*lis_products[x]
    n = n+sum
    
print(round(n,2))
    
    

