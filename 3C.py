x = int(input())
y = int(input())

for i in range (y):
    for j in range (x):
        if ((i+j)%3) == 0:
            print (0,end='')
        elif ((i+j)%3) == 1:
            print (1,end='')
        elif ((i+j)%3) == 2:
            print (2,end='')

    print ()
        