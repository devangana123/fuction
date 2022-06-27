def i(bmi):
    if bmi <= 18.5 :
        return "Underweight"
    elif bmi <= 25.0 :
        return "Normal"
    elif bmi <= 30.0 :
        return "Overweight"
    elif bmi > 30 :
        return "Obese"
    else:
        return "no result found"
a=i(float(input("enter the numbert")))
print(a)