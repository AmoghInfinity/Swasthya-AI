def bmi_calculator(weight, height):
    """
    Calculate BMI given weight (kg) and height (meters)
    """
    try:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return f"Your BMI is {round(bmi, 2)} which falls under {category} category."

    except Exception as e:
        return f"Error calculating BMI: {str(e)}"


def calorie_estimator(age, weight, height, gender):
    """
    Estimate daily calorie needs using simple formula
    """
    try:
        if gender.lower() == "male":
            calories = 10 * weight + 6.25 * height * 100 - 5 * age + 5
        elif gender.lower() == "female":
            calories = 10 * weight + 6.25 * height * 100 - 5 * age - 161
        else:
            return "Invalid gender input. Please specify male or female."

        return f"Estimated daily calorie requirement is {int(calories)} kcal."

    except Exception as e:
        return f"Error estimating calories: {str(e)}"


def current_time_tool():
    """
    Returns current system time
    """
    try:
        from datetime import datetime
        now = datetime.now()
        return f"Current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error fetching time: {str(e)}"