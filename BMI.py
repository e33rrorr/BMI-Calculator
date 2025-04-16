import tkinter as tk

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            result = f"Your BMI is {bmi}. You are underweight."
        elif 18.5 <= bmi < 24.9:
            result = f"Your BMI is {bmi}. You are normal weight."
        elif 25 <= bmi < 29.9:
            result = f"Your BMI is {bmi}. You are overweight."
        else:
            result = f"Your BMI is {bmi}. You are obese."

        label_result.config(text=result)
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

# Create and place widgets
tk.Label(root, text="Enter your height (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Enter your weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

# Run the GUI event loop
root.mainloop()