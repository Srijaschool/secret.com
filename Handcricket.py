import random

def player_bats():
    score = 0
    print("\nYou are batting!")
    while True:
        player_choice = int(input("Enter a number (1-10): "))
        if player_choice < 1 or player_choice > 10:
            print("Invalid input! Choose a number between 1 and 10.")
            continue
        computer_choice = random.randint(1, 10)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("You're OUT!")
            break
        else:
            score += player_choice
            print(f"Your score: {score}")
    
    return score

def computer_bats(target):
    score = 0
    print("\nComputer is batting!")
    while score < target:
        player_choice = int(input("Enter a number (1-10) to bowl: "))
        if player_choice < 1 or player_choice > 10:
            print("Invalid input! Choose a number between 1 and 10.")
            continue
        computer_choice = random.randint(1, 10)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("Computer is OUT!")
            break
        else:
            score += computer_choice
            print(f"Computer score: {score}")
    
    return score

def hand_cricket():
    print("Welcome to Hand Cricket!")
    
    # Player bats first
    player_score = player_bats()
    
    print(f"\nYour final score: {player_score}")
    print("Computer needs to chase your score...\n")
    
    # Computer bats second
    computer_score = computer_bats(player_score)
    
    print(f"\nComputer's final score: {computer_score}")
    
    # Determine the winner
    if player_score > computer_score:
        print("Congratulations! You WIN!")
    elif player_score < computer_score:
        print("Computer WINS! Better luck next time.")
    else:
        print("It's a TIE!")

# Run the game
hand_cricket()