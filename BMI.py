height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

# Convert height and weight to float
height = float(height)
weight = float(weight)

# Calculate BMI
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
