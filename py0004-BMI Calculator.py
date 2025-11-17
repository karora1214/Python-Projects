# BMI Calculator

print("Welcome to the BMI Calculator...")
height = float(input("Enter your height without inches : "))
i_height = float(input("Enter the inches in height : "))
weight = float(input("Enter your weight (in kgs) : "))
bmi_i = i_height * 0.0254
bmi_h = height * 0.3048
total_height = bmi_h + bmi_i
bmi_height = total_height**2
bmi = weight/bmi_height
print(bmi)
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are great shape.")
elif bmi >= 25:
    print("You are obese, lose some weight fatty!")
else:
    print("Wrong Inputs!")