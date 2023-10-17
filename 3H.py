x = int(input())
ball = 0

if x > 3:
    while True:
        print(ball + 1)
        ball = (ball + 3) % x
    
        if ball == 0:
         break