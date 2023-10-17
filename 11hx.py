a=int(input())
b=int(input())
nft=[]
values=[]
dict1=[]
for i in range(b):
    x=input().split()
    x= [int(y) for y in x ]
    value=x[0]/x[1]
    nft.append(x)
    values.append(value)


values.sort()
list1=[]

for i in range(len(nft)):
    count=0
    list2=[]
    for j in nft:
      if values[i]==j[0]/j[1]:
        list2.append(j)
        count+=1
    if count==1:
        list1.append(list2[0])
    else:
        max=0

        for k in list2:
            v=k[0]//k[1]
            if k[0]%k[1]!=0:
                v+=1
            all=v*k[1]-k[0]
            if all>max:
                max=all
                k_max=k
        list1.append(k_max)
        nft.remove(k_max)        

for i in range(1,b):
    list3=list1[0:i]
    cost=a
    pro=0
    for j in list3:
        cost+=j[0]
        pro+=j[1]
    day=cost//pro
    if cost%pro!=0:
        day+=1  
    if i==1:
        date=day      
    elif day<date:
        date=day    
print(date)