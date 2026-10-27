#• Underweight: Below 18.5

#• Healthy Weight: 18.5 to 24.9

#• Overweight: 25.0 to 29.9

#• Obesity (Class I): 30.0 to 34.9

#• Obesity (Class II): 35.0 to 39.9

#• Severe Obesity (Class III): 40.0 or higher

weight = input("What is your weight in k"
               "Kgs?: ")
height = input("What is your height in m?: ")

w = float(weight)
h = float(height)

bmi = w / h**2

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Healthy Weight")
elif bmi >= 25.5 and bmi <= 29.9:
    print("overWeight")
elif bmi>=30.5 and bmi<=34.9:
    print("Obesity (Class I)")
elif bmi>=35.5 and bmi<=39.9:
    print("Obesity (Class II)")
else:
    print("Obesity (Class III)")

