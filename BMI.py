height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

# Convert height and weight to float
height = float(height)
weight = float(weight)

# Calculate BMI
bmi = weight / (height ** 2)
bmi = round(bmi, 2)  # Round to two decimal places

# Print the result
if bmi < 18.5:
    print("Your BMI is", bmi, "You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("Your BMI is", bmi, "You are normal weight.")
elif 25 <= bmi < 29.9:
    print("Your BMI is", bmi, "You are overweight.")    