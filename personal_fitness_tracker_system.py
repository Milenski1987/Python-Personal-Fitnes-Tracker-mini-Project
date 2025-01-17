# Personal Fitness Tracker System 🏋️‍♂️


workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals


workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration): #log workout type and duration
    workouts.append(workout_type)
    workouts.append(duration)
    print(f"{duration} minutes of {workout_type} added successfully!\n")



def log_calorie_intake(calories_consumed): #log calories intake for current meal
    calories.append(calories_consumed)
    print(f"{calories_consumed} calories added!\n")



def view_progress():
    total_workout_time = 0
    for i in range(1, len(workouts), 2):
        total_workout_time += workouts[i]
    total_calories = sum(calories)

    print(f"Total workout time for today: {total_workout_time} minutes.")
    print(f"Total calories consumed today: {total_calories} calories.")
    print("Good results. Keep going!\n")


def reset_progress(): #progrss reset
    workouts.clear()
    calories.clear()
    print(f"Your workout and calories logs are clear.")



def set_daily_goals(workout_minutes, calorie_limit):
    global workout_goal
    global calorie_goal

    workout_goal = workout_minutes
    calorie_goal = calorie_limit
    print(f"Workout and Calorie goals are set successfully!\n")



def encouragement_system():
    total_workout_time = 0
    for i in range(1, len(workouts), 2):
        total_workout_time += workouts[i]
    total_calories = sum(calories)

    workout_percent = round(total_workout_time / workout_goal * 100)
    calories_percent = round(total_calories / calorie_goal * 100)
    print(f"You reached {workout_percent}% of daily workout goal and {calories_percent}% of daily calories goal\n")
    print("Push harder than yesterday if you want a different tomorrow.")


def main():
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Check daily progress compared to goals")
        print("7. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")


        if choice == '1':
            type_of_workout = input("Enter the type of workout:")
            duration_of_workout = int(input("Enter duration of workout in minutes:"))
            if duration_of_workout <= 0:
                print("Invalid input. Program is restarting!")
                continue
            log_workout(type_of_workout, duration_of_workout)


        elif choice == '2':
            current_calories = int(input("Enter calories for current meal:"))
            if current_calories <= 0:
                print("Invalid input. Program is restarting!")
                continue
            log_calorie_intake(current_calories)


        elif choice == '3':
            view_progress()


        elif choice == '4':
            confirmation = input("Are you sure?:")
            if confirmation.lower() == "yes":
                reset_progress()


        elif choice == '5':
            print("Please enter your daily goals:")
            minutes = int(input("Workout minutes for today:"))
            if minutes <= 0:
                print("Invalid input. Program is restarting!")
                continue
            calorie = int(input("Calories to consume today:"))

            if calorie <= 0:
                print("Invalid input. Program is restarting!")
                continue
            set_daily_goals(minutes, calorie)


        elif choice == '6':
            if workout_goal == 0 or calorie_goal == 0:
                print("Your daily goals are not set!")
            elif not workouts:
                print("You don't have any workouts yet.")
            elif not calories:
                print("No meals consumed today.")
            else:
                encouragement_system()


        elif choice == '7':
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()