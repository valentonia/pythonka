n = int(input())
k = int(input())
list = []

if 0<=n<=1000000000 and 1<=k<=10:
    while True:
        if n == 0:
            break
    
            
        if n % 16 == 0:
            list.append(0)
        elif 1 <= n % 16 <= 9:
            list.append(n%16)
        else:
             
            if n % 16 == 10:
                list.append("A")
            elif n % 16 == 11:
                list.append("B")
            elif n % 16 == 12:
                list.append("C")
            elif n % 16 == 13:
                list.append("D")
            elif n % 16 == 14:
                list.append("E")
            elif n % 16 == 15:
                list.append("F")
                
        n = n // 16
    try:
        print(list[k-1])
    except Exception as e: 
        print(0)
else:
    print("Invalid input")
    

    
