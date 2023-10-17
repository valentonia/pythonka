def avg(num1,num2=None,num3=None):
    if num2!=None and num3!=None:
        value = (round((num1+num2+num3)/3,2))
    elif num2!=None:
        value = (round((num1+num2)/2,2))
    else:
        value = float(num1)
 
    return value


a = int(input())
b = int(input())
c = int(input())
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))