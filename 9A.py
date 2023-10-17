lis = []
mean = 0
var = 0
sum = 0
while True:
    n = input()
    if n == '$':
        break

    n = int(n)
    lis.append(n)
    
    var += n
    mean = var / len(lis)

for i in lis:
    num = (i-mean)**2
    sum += num
    ans = (sum / len(lis)) ** (1/2)
    
print (round(ans,2))
    
            
        

