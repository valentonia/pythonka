'''
dic = {}
while True:
    n = input()
    if n == '$':
        break
    else:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
            
dic = list(dic.items())
dic.sort(key = lambda x: (x[1], x[0]))
print(dic)            

'''
'''
lis_letter = []
while True:
    n = input()
    if n == '$':
        break
    else:
        n = input().split()
        lis_letter.append(n)
        
print(lis_letter)
'''

