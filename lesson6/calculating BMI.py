height=float(input("enter yur height in meters"))
weight=float(input("enter your weight in kg"))
BMI=weight/height*height
print("your BMI value is", BMI)
if BMI<=18.4:
    print("you are underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
elif BMI<=34.9:
    print("you are severly overweight")
elif BMI<=39.9:
    print("you are obese")
else :
    print("you are severly obese")


