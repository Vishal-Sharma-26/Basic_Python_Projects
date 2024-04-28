'''
This script defines two functions: calculate_bmi to compute the BMI value based on weight and height,
and interpret_bmi to interpret the BMI value and categorize it into underweight, normal weight, overweight, or obese.
The main function takes user input for weight and height, calculates the BMI, and prints the result along with the category.
'''



def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height^2)
    """
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide corresponding interpretation.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    print("-------------")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Interpretation: {interpretation}")

if __name__ == "__main__":
    main()
