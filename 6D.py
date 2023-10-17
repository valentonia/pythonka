n = int(input())
n >= 2
def recursion(n, s = 0):
    if n == 0:
        return
    else:
        print(s*' '+n*'*')
        recursion(n-1, s+ 1)
        
def recursive (n, i=-1):
    if n == 1:
        return
    recursion (n, i+1)
    recursive (n-1, i+1)
recursive (n)
