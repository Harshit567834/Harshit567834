def welcome_message():
    print("Welcome to CYC (Create Your Country)!")
    print("Let's start by creating your country, one step at a time.")

def get_country_name():
    name = input("\nWhat will be the name of your country? ")
    print(f"\nGreat! {name} sounds like a powerful name for a country!")
    return name

def choose_population():
    print("\nNow, let's decide on the population size.")
    print("1. Just me")
    print("2. A small village")
    print("3. A bustling city")
    print("4. Too many to count!")
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        population = "Just you, huh? A true one-person show!"
    elif choice == "2":
        population = "A small village, perfect for tight-knit communities."
    elif choice == "3":
        population = "A bustling city—busy streets and bright lights!"
    elif choice == "4":
        population = "Wow! A whole lot of citizens! How will you manage them all?"
    else:
        population = "An unknown number of people, living in mysterious ways."
    
    print(f"\nPopulation choice: {population}")
    return population

def choose_government():
    print("\nEvery country needs a government. What's your preference?")
    print("1. Democracy")
    print("2. Monarchy")
    print("3. Dictatorship")
    print("4. No government at all—anarchy!")
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        government = "Democracy, where the people have a voice!"
    elif choice == "2":
        government = "Monarchy, with royalty ruling the land."
    elif choice == "3":
        government = "Dictatorship, where one person calls all the shots."
    elif choice == "4":
        government = "Anarchy! Chaos, freedom, and no rules."
    else:
        government = "An unknown form of government, operating in secret."
    
    print(f"\nGovernment choice: {government}")
    return government

def choose_language():
    language = input("\nGreat! Now, what will be the official language of your country? ")
    print(f"\nWonderful! The people of your country will speak {language}. How poetic!")
    return language

def choose_capital():
    capital = input("\nWhat will be the capital city of your country? ")
    print(f"\nAh, {capital}, the shining jewel of your nation!")
    return capital

def choose_landscape():
    print("\nWhat kind of landscape will your country have?")
    print("1. Mountainous")
    print("2. Desert")
    print("3. Forested")
    print("4. Island")
    print("5. Plains")
    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        landscape = "Mountainous, with towering peaks and majestic views."
    elif choice == "2":
        landscape = "A vast desert, with endless sand dunes and scorching heat."
    elif choice == "3":
        landscape = "Forested, filled with lush greenery and dense trees."
    elif choice == "4":
        landscape = "An island, surrounded by water and filled with tropical vibes."
    elif choice == "5":
        landscape = "Plains, with wide open spaces and gentle rolling hills."
    else:
        landscape = "A mysterious landscape that defies all description."
    
    print(f"\nLandscape choice: {landscape}")
    return landscape

def choose_continent():
    print("\nFinally, which continent will your country be located on?")
    print("1. Africa")
    print("2. Asia")
    print("3. Europe")
    print("4. North America")
    print("5. South America")
    print("6. Australia")
    print("7. Antarctica")
    choice = input("\nChoose an option (1-7): ")

    if choice == "1":
        continent = "Africa, with its vast savannas and rich cultural heritage."
    elif choice == "2":
        continent = "Asia, the largest continent with diverse landscapes and traditions."
    elif choice == "3":
        continent = "Europe, home to historical landmarks and diverse cultures."
    elif choice == "4":
        continent = "North America, with its diverse climate and bustling cities."
    elif choice == "5":
        continent = "South America, known for its rainforests and vibrant festivals."
    elif choice == "6":
        continent = "Australia, with its unique wildlife and laid-back lifestyle."
    elif choice == "7":
        continent = "Antarctica, the frozen continent of endless snow and ice."
    else:
        continent = "An unknown continent, shrouded in mystery and adventure."
    
    print(f"\nContinent choice: {continent}")
    return continent

def main():
    welcome_message()
    country_name = get_country_name()
    population = choose_population()
    government = choose_government()
    language = choose_language()
    capital = choose_capital()
    landscape = choose_landscape()
    continent = choose_continent()
    
    print(f"\nCongratulations! You've created {country_name}.")
    print(f"It has a population of {population}.")
    print(f"The government is {government}.")
    print(f"The official language is {language}.")
    print(f"The capital city is {capital}.")
    print(f"The landscape is {landscape}.")
    print(f"And it is located in {continent}. What a magnificent country!")

if __name__ == "__main__":
    main()