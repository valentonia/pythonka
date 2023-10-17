n = int(input()) #4

for i in range (1 ,n + 1): #(1,5)(1,2,3,4)
    for j in range (i +1, n + 1): #()
        for k in range (j + 1, n + 1):
                row = "(" + str(i) + "," + str(j) + "," + str(k) + ")"
                print (row)