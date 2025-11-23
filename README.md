1. Introduction
Body Mass Index (BMI) is a widely used method to assess whether a person’s weight is healthy in relation to their height. It is a simple numerical value that helps categorize individuals as underweight, normal weight, overweight, or obese.

The formula for BMI is:
"BMI"="weight (kg)" /〖"height (m)" 〗^2 

This project aims to develop a Python program that calculates BMI and categorizes users into health ranges.
________________________________________
2. Objectives
	To calculate BMI using Python.
	To categorize BMI according to standard health guidelines.
	To provide a simple and interactive program for users.
	To handle user input errors gracefully.
________________________________________
3. Tools and Technologies Used
	Programming Language: Python 3
	IDE: VS Code / PyCharm / Any Python IDE
	Concepts used: Variables, Functions, Loops, Conditional Statements, Exception Handling, String Formatting
________________________________________


4. Methodology
	Input Collection
	User enters their weight in kilograms and height in meters.
	Input is validated using try-except blocks to prevent invalid entries.
	BMI Calculation
	BMI is calculated using the formula:
	bmi = weight / (height ** 2)
	The result is rounded to two decimal places for clarity.
	BMI Classification
	BMI is categorized as follows:
	Underweight: BMI < 18.5
	Normal weight: 18.5 ≤ BMI < 25
	Overweight: 25 ≤ BMI < 30
	Severely obese: 30 ≤ BMI < 40
	Obese: BMI ≥ 40
	Output Display
	The program prints the calculated BMI and the corresponding category.
	Users can repeat the calculation multiple times without restarting the program.
# python code : 
def get_float(prompt):
    while True:
        try:
            s = input(prompt).strip()
            value = float(s)
            if value <= 0:
                print("Value must be positive. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Try again.")

def bmi_category(bmi):
    if bmi < 38.5:
        return "Underweight"
    elif bmi < 45:
        return "Normal weight"
    elif bmi < 50:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator (metric units)")
    weight = get_float("Enter weight in kilograms (kg): ")
    height_cm = get_float("Enter height in centimeters (cm): ")
    height_m = height_cm / 100.0

    bmi = weight / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
    category = bmi_category(bmi)

    print(f"\nYour BMI: {bmi_rounded}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()


6.Sample Output
BMI Calculator (metric units)
Enter weight in kilograms (kg): 56
Enter height in centimeters (cm): 321

Your BMI: 5.43
Category: Underweight
PS C:\Users\hp\VITYARTHI PROJECT> & C:/Users/hp/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/hp/VITYARTHI PROJECT/program.py"
BMI Calculator (metric units)
Enter weight in kilograms (kg): 89
Enter height in centimeters (cm): 89

Your BMI: 112.36
Category: Obesity
Enter weight in kilograms (kg): 56
Enter height in centimeters (cm): 1.5

Your BMI: 248888.89
Category: Obesity
PS C:\Users\hp\VITYARTHI PROJECT>
________________________________________
7. Conclusion
	This BMI Calculator program demonstrates a functional Python application that is both user-friendly and educational.
	Users can easily determine their BMI and understand their health status.
	The project uses basic Python concepts like functions, loops, conditional statements, exception handling, and string formatting.
________________________________________
8. Future Enhancements
	Create a GUI version using Tkinter for better user interaction.
	Save BMI history for multiple users.
	Provide health recommendations based on BMI.
	Develop a web-based version for accessibility on multiple devices.


