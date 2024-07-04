import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == '1' and computer_choice == '3') or \
       (user_choice == '2' and computer_choice == '1') or \
       (user_choice == '3' and computer_choice == '2'):
        return "You win!"
    else:
        return "You lose!"

def get_choice_name(choice):
    if choice == '1':
        return 'rock'
    elif choice == '2':
        return 'paper'
    elif choice == '3':
        return 'scissors'
    else:
        return 'unknown'

def print_choices(user_choice, computer_choice):
    print(f"Your choice: {get_choice_name(user_choice)}")
    print(f"Computer's choice: {get_choice_name(computer_choice)}")

def main():
    print("Welcome to Rock-Paper-Scissors game!")

    user_score = 0
    computer_score = 0

    while True:
        choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        computer_choice = random.choice(list(choices.keys()))

        print("\nEnter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter the number corresponding to your choice: ")

        if user_choice not in choices:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        print_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nYour score: {user_score}, Computer's score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
