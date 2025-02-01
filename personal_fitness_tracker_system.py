from time import sleep
from colorama import Fore

# Personal Fitness Tracker System 🏋️‍♂️


workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals


workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type: str, duration: int) -> str: #log workout type and duration
    workouts.append(workout_type)
    workouts.append(duration)
    return f"{duration} minutes of {workout_type} added successfully!\n"



def log_calorie_intake(calories_consumed: int) -> str: #log calories intake for current meal
    calories.append(calories_consumed)
    return f"{calories_consumed} calories added!\n"



def view_progress() -> str:
    total_workout_time = 0
    for i in range(1, len(workouts), 2):
        total_workout_time += workouts[i]
    total_calories = sum(calories)

    return  f"Total workout time for today: {total_workout_time} minutes.\
    \nTotal calories consumed today: {total_calories} calories.\
    \nKeep going!\n"


def reset_progress() -> str: #progrss reset
    workouts.clear()
    calories.clear()
    return f"Your workout and calories logs are clear.\n"



def set_daily_goals(workout_minutes: int, calorie_limit: int) -> str:
    global workout_goal
    global calorie_goal

    workout_goal = workout_minutes
    calorie_goal = calorie_limit
    return f"Workout and Calories goals are set successfully!\n"



def encouragement_system() -> str:
    total_workout_time = 0
    for i in range(1, len(workouts), 2):
        total_workout_time += workouts[i]
    total_calories = sum(calories)

    workout_percent = round(total_workout_time / workout_goal * 100)
    calories_percent = round(total_calories / calorie_goal * 100)
    return f"You reached {workout_percent}% of daily workout goal and {calories_percent}% of daily calories goal\
    \nPush harder than yesterday if you want a different tomorrow.\n"


def main():
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print(Fore.MAGENTA + "1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Check daily progress compared to goals")
        print("7. Exit")
        sleep(1)

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")


        if choice == '1':
            type_of_workout = input("Enter the type of workout: ")
            sleep(0.5)
            duration_of_workout = int(input("Enter duration of workout in minutes: "))
            sleep(0.5)
            if duration_of_workout <= 0:
                print(Fore.RED + "Invalid input. Program is restarting!")
                continue
            print(Fore.GREEN + log_workout(type_of_workout, duration_of_workout))
            sleep(1)


        elif choice == '2':
            current_calories = int(input("Enter calories for current meal:"))
            sleep(0.5)
            if current_calories <= 0:
                print(Fore.RED + "Invalid input. Program is restarting!")
                continue
            print(Fore.GREEN + log_calorie_intake(current_calories))
            sleep(1)


        elif choice == '3':
            sleep(0.5)
            print(Fore.GREEN + view_progress())
            sleep(1)

        elif choice == '4':
            confirmation = input("Are you sure?:")
            sleep(0.5)
            if confirmation.lower() == "yes":
                print(Fore.GREEN + reset_progress())
                sleep(1)

        elif choice == '5':
            print("Please enter your daily goals:")
            sleep(0.5)
            minutes = int(input("Workout minutes for today:"))
            sleep(0.5)
            if minutes <= 0:
                print(Fore.RED + "Invalid input. Program is restarting!")
                continue
            calorie = int(input("Calories to consume today:"))
            sleep(0.5)
            if calorie <= 0:
                print(Fore.RED + "Invalid input. Program is restarting!")
                continue
            print(Fore.GREEN + set_daily_goals(minutes, calorie))
            sleep(1)

        elif choice == '6':
            if workout_goal == 0 or calorie_goal == 0:
                print(Fore.RED + "Your daily goals are not set!")
            elif not workouts:
                print(Fore.RED + "You don't have any workouts yet.")
            elif not calories:
                print(Fore.RED + "No meals consumed today.")
            else:
                sleep(0.5)
                print(Fore.GREEN + encouragement_system())
                sleep(1)

        elif choice == '7':
            sleep(0.5)
            print(Fore.CYAN + "Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break

        else:
            print(Fore.RED + "Invalid choice, please try again.")


if __name__ == "__main__":
    main()