w = float(input())
h = float(input())
bmi = round(w/((h/100)**2),2)

if bmi < 18.5:
    print (bmi)
    print ("Below normal weight")
elif (18.5 <= bmi < 25):
    print (bmi)
    print ("Normal weight")
elif (25 <= bmi < 30):
    print (bmi) 
    print ("Overweight")
elif (30 <= bmi < 35):
    print (bmi) 
    print ("Class I Obesity")
elif (35 <= bmi <40):
    print (bmi) 
    print ("Class II Obesity")
elif (bmi >= 40):
    print (bmi)
    print ("Class III Obesity")
















