count = 0
sum = 0
while count < 2:
    try:
        if count == 0:
            num = float(input('Enter a number: '))
        else:
            num = float(input('Enter another number: '))
            
        sum += num
        count += 1
    except ValueError:
        print('ERROR: Invalid input')
        
print('The sum is', sum)