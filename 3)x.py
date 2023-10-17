old_num = input()
old_diff = 0

if old_num == '$':
    print('Insufficient data')
    
else:
    new_num = input()
    if new_num == '$':
        print('Insufficient data')
    else:
        while True:
        
        
            diff = abs(int(old_num)-int(new_num))
            if diff > old_diff:
                old_diff = diff
            
            new_num = input
            if new_num == '$':
                break
        print(old_diff)