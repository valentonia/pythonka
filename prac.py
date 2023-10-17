count = 0
max_l = 0
i = 0
while True:
    n = input()
    if n == '$':
        break
    else:
        if i == 0:
            same = n
            count = 1
        else:
            if n  == same:
                count += 1
            else:
                if count > max_l:
                    max_l = count
                same = n
                count = 1
    i += 1            
if count > max_l:
    max_l = count
print(max_l)
        
        
    
