n = int(input())
def recursion(n):
    if n == 0:
        return
    else:
        recursion(n-1)
        print(n)
recursion (n)