# This is how function is created in Python
# def function_name():
#     your code here
#     return something

import random

# Function to generate random choices for player and computer
def get_choices():
    options = ["rock", "paper", "scissors"] # List of possible options
    player = random.choice(options) # Random choice for player
    computer = random.choice(options) # Random choice for computer
    return player, computer # Return both choices

# Function to determine the winner based on player and computer choices
def check_win(player, computer):
    win_combinations = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")] # List of win combinations
    
    if (player, computer) in win_combinations:
        return "Player wins." # Player wins if player choice beats computer choice
    elif player == computer:
        return "Tie." # If both choices are the same, it's a tie
    else:
        return "Computer wins." # If player choice doesn't beat computer choice, computer wins

# Function to play a single game
def play_game():
    player, computer = get_choices() # Get random choices for player and computer
    result = check_win(player, computer) # Determine the winner
    print(f"Player picked {player} and Computer picked {computer}") # Output player and computer choices
    return result # Return the result

# Function to play a series of games
def play_series(rounds):
    player_win_count = 0 # Initialize player win count
    computer_win_count = 0 # Initialize computer win count
    tie_count = 0 # Initialize tie count
    
    # Loop through the desired number of rounds
    for i in range(rounds):
        result = play_game() # Play a single game
        
        # Update win counts based on result of the game
        if result == "Player wins.":
            player_win_count += 1
        elif result == "Computer wins.":
            computer_win_count += 1
        else:
            tie_count += 1
    
    # Output the final win counts
    print(f"After {rounds} rounds, player won {player_win_count} times, computer won {computer_win_count} times, and tied {tie_count} times.")

# Get number of rounds to play from user input
rounds = int(input("Enter number of rounds to play: "))
play_series(rounds) # Play the series of games
