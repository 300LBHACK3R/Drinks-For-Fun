#!/usr/bin/env python3
# Fun and Interactive Drinking Game.
# 2025 Tate R.A Byers - Crafted with Intellect and Ingenuity 😎
# 2025 Tate R.A Byers - Crafted with Intellect and Ingenuity 😎
# 2025 Tate R.A Byers - Crafted with Intellect and Ingenuity 😎

import random
from datetime import datetime

LEGAL_DRINKING_AGE = 19
MIN_AGE_TO_ENTER = 16
MIN_YEAR = 1900
CURRENT_YEAR = datetime.now().year

ALCOHOLIC_DRINK_MENU = {
    "Beer": "A classic! Cold and refreshing.🍺",
    "Wine": "Sophisticated choice! Great for savoring.🍷",
    "Vodka": "Bold pick! Let’s keep it smooth.🧈",
    "Whiskey": "Strong and timeless, just like you.🕓",
    "Rum": "Ahoy! A pirate’s favorite.🍶",
    "Tequila": "One shot or the whole bottle? Your call.🥄🌫"
}

NON_ALCOHOLIC_DRINK_MENU = {
    "Smoothie": "Fruit-packed and refreshing. 🍓🥭",
    "Pop": "Classic fizzy drink, great for any occasion. 🍹",
    "Milkshake": "Sweet, creamy, and irresistible. 🍦",
    "Water": "Stay hydrated, it’s always a good choice. 💧",
    "Energy Drink": "Boost your energy with a kick. ⚡"
}

ADULT_COMMENTS = [
    "YOU WIN, Enjoy, That is my personal favorite.",
    "YOU WIN.. BUT DAMN, Drinking that!?!?! You must be a ROCK-STAR⭐!",
    "YOU WIN, but remember the drink you choose defines you.",
    "YOU WIN, Although I would not have too many of those, ENJOY!",
    "YOU WIN, ** BONUS PRIZE ** Your drink is on the house, Enjoy!",
    "YOU WIN, Cheers! Remember, moderation is key, even for legends like you!"
]

UNDERAGE_COMMENTS = [
    "GAME OVER, !!!!! UNDERAGE !!!!! No drinks for you.",
    "GAME OVER, Sorry, you are too young. Enjoy being young, do not rush it.",
    "GAME OVER, Your time will come, Then you will have wished it did not come so fast.",
    "GAME OVER, But hey, how about a milkshake? Those are timeless!"
]

def get_valid_input(prompt: str, valid_choices=None, value_type=int) -> int:
    """Prompts for valid user input and handles errors."""
    while True:
        try:
            user_input = value_type(input(prompt))
            if valid_choices and user_input not in valid_choices:
                raise ValueError("Invalid choice.")
            return user_input
        except ValueError as e:
            print_colored(f"Error: {str(e)}. Please try again.", "red")


def print_colored(message: str, color="white") -> None:
    """Prints messages with specified color using ANSI escape codes."""
    color_codes = {
        "white": "37", "yellow": "33", "cyan": "36", "green": "32", "magenta": "35", "red": "31"
    }
    color_code = color_codes.get(color, "37") 
    print(f"\033[{color_code}m{message}\033[0m")


def display_drink_menu(is_adult: bool) -> None:
    """Displays the appropriate drink menu based on the user's age."""
    print_colored("Here’s what we have on the menu:", "cyan")
    if is_adult:
        for drink, description in ALCOHOLIC_DRINK_MENU.items():
            print_colored(f"- {drink.title()}: {description}", "yellow")
    else:
        for drink, description in NON_ALCOHOLIC_DRINK_MENU.items():
            print_colored(f"- {drink.title()}: {description}", "yellow")


def calculate_age(birth_year: int) -> int:
    """Calculates the age based on Year of Birth."""
    return CURRENT_YEAR - birth_year


def get_user_data() -> tuple:
    name = input("What is your name, friend?: ").strip()

    #  EASTER EGG !!!!!
    if name.lower() == "tate":
        print_colored("The One, The Only, TATE! You've unlocked a EASTER EGG! 🎉", "magenta")
        print_lightsaber_art()

    birth_year = get_valid_input("What Year were you born in? ", value_type=int)
    while birth_year < MIN_YEAR or birth_year > CURRENT_YEAR:
        print_colored("Please enter a valid year of birth between 1900 and the current year.", "red")
        birth_year = get_valid_input("What Year were you born in? ", value_type=int)
        
    age = calculate_age(birth_year)

    return name, birth_year, age


def display_results(name: str, age: int, birth_year: int) -> None:
    """Displays the results with user's age and other information."""
    print_colored("\nUser Data Summary:", "yellow")
    print_colored(f"NAME               : {name}", "green")
    print_colored(f"AGE                : {age}", "cyan")
    print_colored(f"YEAR OF BIRTH      : {birth_year}", "green")

    if age >= LEGAL_DRINKING_AGE:
        process_drinks(age, name, is_adult=True)
    elif age >= MIN_AGE_TO_ENTER:
        process_drinks(age, name, is_adult=False)
    else:
        print_colored(random.choice(UNDERAGE_COMMENTS), "red")


def process_drinks(age: int, name: str, is_adult: bool) -> None:
    """Processes drink orders for users and gives a fun interaction based on age."""
    if is_adult:
        print_colored(f"You're old enough, {name}, time to choose your drink! 🍻🍇🍂", "green")
        display_drink_menu(is_adult=True)

        drink_choice = input("What would you like to drink? ").strip().title()

        if drink_choice in ALCOHOLIC_DRINK_MENU:
            print_colored(f"Great choice, {name}! Enjoy your {drink_choice}!", "green")
            print_colored(random.choice(ADULT_COMMENTS), "magenta")
        else:
            print_colored("Oops, we don’t serve that here. Please try again.", "red")
            process_drinks(age, name, is_adult=True)
    else:
        print_colored("You're allowed in, but you can't drink alcohol yet. Maybe try one of these non-alcoholic drinks?", "yellow")
        display_drink_menu(is_adult=False)

        drink_choice = input("What would you like to drink? ").strip().title()

        if drink_choice in NON_ALCOHOLIC_DRINK_MENU:
            print_colored(f"Great choice, {name}! Enjoy your {drink_choice}!", "green")
            print_colored(random.choice(UNDERAGE_COMMENTS), "magenta")
        else:
            print_colored("Oops, we don’t serve that here. Please try again.", "red")
            process_drinks(age, name, is_adult=False)


def get_greeting() -> str:
    """Returns a greeting based on the time of day."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def print_lightsaber_art() -> None:
    """Prints ASCII art of Darth Maul's Lightsaber."""
    lightsaber = """
     __        __   _                                _ _____ ____ ___ 
    \ \      / /__| | ___ ___  _ __ ___   ___      | | ____|  _ \_ _| 
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \  _  | |  _| | | | | |  
      \ V  V /  __/ | (_| (_) | | | | | |  __/ | |_| | |___| |_| | |  
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \___/|_____|____/___|  
    """
    print_colored(lightsaber, "red")


def main() -> None:
    """Main function to execute the program, ask for inputs, calculate results, and display them."""
    greeting = get_greeting()
    print_colored(f"{greeting}, welcome to The Drinking Game!", "yellow")
    
    name, birth_year, age = get_user_data()
    display_results(name, age, birth_year)

    input("I hope you enjoyed your drink & the game! NOW GET OUT...")

if __name__ == "__main__":
    main()


# 2025 Tate R.A Byers - Crafted with Intellect and Ingenuity 😎
# 2025 Tate R.A Byers - Crafted with Intellect and Ingenuity 😎
# 2025 Tate R.A Byers - Crafted with Intellect and Ingenuity 😎
