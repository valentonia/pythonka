hr = int(input())
min = int(input())
ex_min = int(input())
new_day = 0

new_min = (min+ex_min) % 60
new_hr = hr + ((min+ex_min)//60)
new_day = new_hr // 24
new_hr = new_hr % 24

if 0 <= new_hr < 10:
    if new_min < 10:
        print('0'+ str(new_hr)+':'+'0'+str(new_min),end = '')
    elif new_min >= 10:
        print('0'+str(new_hr)+':'+str(new_min),end = '')
elif 10 <= new_hr or new_hr < 0:
    if new_min < 10:
        print(str(new_hr)+':'+'0'+str(new_min),end = '')
    elif new_min >= 10:
        print(str(new_hr)+':'+str(new_min),end = '')
elif new_min >= 10:
    print(str(new_hr)+':'+ str(new_min), end= '')
if new_day == 1:
    print (' +',new_day,'day')
elif new_day > 1:
    print (' +',new_day,'days')
elif new_day == -1:
    print (' -',-new_day,'day')
elif new_day < -1:
    print (' -',-new_day,'days')
    