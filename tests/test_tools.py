import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tools import bmi_calculator, calorie_estimator

def test_tools():
    print("Testing BMI Calculator...")
    bmi = bmi_calculator(70, 1.75)
    print(bmi)
    assert "BMI" in bmi

    print("\nTesting Calorie Estimator...")
    calories = calorie_estimator(25, 70, 1.75, "male")
    print(calories)
    assert "calorie" in calories.lower()

    print("\nTool Tests Passed")


if __name__ == "__main__":
    test_tools()