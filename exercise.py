# Excerise 1
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()  # Convert to lowercase for simplicity
    if letter.isalpha() and len(letter) == 1:  # Ensure input is a single letter
        if letter in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical letter.")

check_letter()

# 2

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


check_voting_eligibility()

# 3

def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age < 0:
            print("Age cannot be negative.")
        elif dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = 20 + (dog_age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

calculate_dog_years()

# 4

def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")

weather_advice()

# 5

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))
    except ValueError:
        print("Invalid day. Please enter a number.")
        return

    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }

    if month not in months:
        print("Invalid month. Please enter a valid month.")
        return

    month_num = months[month]

    if (month_num == 12 and day >= 21) or (month_num < 3) or (month_num == 3 and day < 20):
        season = "Winter"
    elif (month_num == 3 and day >= 20) or (month_num < 6) or (month_num == 6 and day < 21):
        season = "Spring"
    elif (month_num == 6 and day >= 21) or (month_num < 9) or (month_num == 9 and day < 22):
        season = "Summer"
    else:
        season = "Fall"

    print(f"{month} {day} is in {season}.")


determine_season()




