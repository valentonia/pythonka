try:
    reader = open(input(), 'r')
    for row in input:
        print(row)
        
    reader.close()
    
except FileNotFoundError:
    print('ERROR: File not found')