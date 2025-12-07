# Name: Rithvik Naroth
# Date: 07-12-2025
# Project: Daily Calorie Tracker (CLI)

import time

def main():
    print("=" * 50)
    print(" Welcome to Daily Calorie Tracker ")
    print("=" * 50)
    print("This tool lets you log meals, track total calories,")
    print("compare against your daily limit, and optionally")
    print("save a session report to a file.\n")

    # ----- Task 2: Input & Data Collection -----
    meals = []
    calories = []

    while True:
        try:
            meal_count = int(input("How many meals do you want to enter today? "))
            if meal_count <= 0:
                print("Please enter a positive number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    for i in range(meal_count):
        print(f"\nMeal {i + 1} of {meal_count}")
        meal_name = input("Enter meal name (e.g., Breakfast): ").strip()
        while not meal_name:
            meal_name = input("Meal name cannot be empty. Please re-enter: ").strip()

        while True:
            cal_input = input(f"Enter calories for {meal_name}: ")
            try:
                cal_value = float(cal_input)
                if cal_value < 0:
                    print("Calories cannot be negative. Please re-enter.")
                    continue
                break
            except ValueError:
                print("Invalid number. Please enter calories like 350 or 350.5.")
        meals.append(meal_name)
        calories.append(cal_value)

    # ----- Task 3: Calorie Calculations -----
    total_calories = sum(calories)          # uses built-in sum()[web:6]
    average_calories = total_calories / len(calories)

    print()
    while True:
        limit_input = input("Enter your daily calorie limit: ")
        try:
            daily_limit = float(limit_input)
            if daily_limit <= 0:
                print("Limit should be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid number. Please try again.")

    # ----- Task 4: Exceed Limit Warning System -----
    over_limit = total_calories > daily_limit
    if over_limit:
        status_message = "Warning: You have exceeded your daily calorie limit!"
    else:
        status_message = "Great job! You are within your daily calorie limit."

    # ----- Task 5: Neatly Formatted Output -----
    print("\n\nYour Daily Calorie Report\n")
    print("Meal Name\t\tCalories")
    print("-----------------------------------------")
    for name, cal in zip(meals, calories):
        # adjust spacing with \t and string formatting
        if len(name) < 8:
            print(f"{name}\t\t\t{cal}")
        else:
            print(f"{name}\t\t{cal}")

    print("-----------------------------------------")
    print(f"Total:\t\t\t{total_calories}")
    print(f"Average:\t\t{average_calories:.2f}")
    print("\nStatus:", status_message)

    # ----- Task 6 (Bonus): Save Session Log to File -----
    save_choice = input("\nDo you want to save this session to a file? (y/n): ").strip().lower()
    if save_choice == "y":
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        filename = "calorie_log.txt"

        with open(filename, "a", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write(f"Session Time: {timestamp}\n")
            f.write("Meal Name\tCalories\n")
            f.write("-----------------------------------------\n")
            for name, cal in zip(meals, calories):
                f.write(f"{name}\t{cal}\n")
            f.write("-----------------------------------------\n")
            f.write(f"Total:\t{total_calories}\n")
            f.write(f"Average:\t{average_calories:.2f}\n")
            f.write(f"Daily Limit:\t{daily_limit}\n")
            f.write(f"Status:\t{status_message}\n")
            f.write("\n")

        print(f"\nSession saved to {filename} successfully.")
    else:
        print("\nSession not saved.")

    print("\nThank you for using Daily Calorie Tracker!")

if __name__ == "__main__":
    main()
