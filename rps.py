import random

def get_user_choice():
    """Get user's choice of rock, paper, or scissors."""
    user_input = input("Enter your choice (rock, paper, scissors): ")
    return user_input.lower()

def get_computer_choice():
    """Get computer's choice of rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    """Play a game of rock-paper-scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    print(f"User chose {user_choice} and computer chose {computer_choice}.")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("User wins!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()
