n = int(input())
fav = set(input().split())

for i in range(n - 1):
    like = input().split()
    fav.intersection_update(like)

if fav:
    print(' '.join(sorted(fav)))
else:
    print('Nothing')