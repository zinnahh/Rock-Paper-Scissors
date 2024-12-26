import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    "Generates a random choice for the computer."
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    
    else:
        return "Computer Wins"
    
    
    
def play_game():
    """Plays a single round or Rock, Paper, Scissors."""
    user_choice = input("Enter your choice(rock/paper/scissors): ").lower()
    
    if user_choice not in choices: 
        print("Invalid Choice! Please enter rock, paper, or scissors.") 
        return
    

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

if __name__ == "__main__":
    play_game()