def guess_number_game():
    import random

    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 50.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def rock_paper_scissors_game():
    
    import random

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to Rock-Paper-Scissors!")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Main Program

def main():
    
    while True:
        print("\nSelect a game (1-3):")
        print("1. Guess the Number game")
        print("2. Rock-Paper-Scissors game")
        print("3. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

        if choice != '3':
            again = input("Would you like to play another game? (y/n): ").lower()
            if again != 'y':
                print("Exiting program. Goodbye!")
                break



if __name__ == "__main__":
    main()