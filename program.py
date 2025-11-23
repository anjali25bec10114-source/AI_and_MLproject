
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
