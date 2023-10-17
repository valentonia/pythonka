n = int(input())  # changeable, must be odd

zeros = n // 2
ones = 1

for i in range(n // 2):  # do what is inside this loop n // 2 times
    a = "0" * zeros
    b = "1" * ones
    print(a + b + a)

    zeros -= 1
    ones += 2

print("1" * n)
zeros += 1
ones -= 2

for i in range(n // 2):  # do what is inside this loop n // 2 times
    a = "0" * zeros
    b = "1" * ones
    print(a + b + a)

    zeros += 1
    ones -= 2

    
   




