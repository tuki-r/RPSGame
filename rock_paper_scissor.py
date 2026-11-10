# Ask user to pick between RPS
# If invalid value
#   Print invalid chocie, error
# Let the computer make a choice 
# Print choices (emojis)
#  Determine the winner
# ASk if they want to play again 
# if not 
#   Terminate

import random 


#dict , maps a key -> value
# 'r' -> '🪨' etc
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️' }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('invlaid choice')

def display_choices(user_choice, comp_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[comp_choice]}')

def determine_winner(user_choice, comp_choice):
    if user_choice  == comp_choice:
            print('Tie')
    elif (
            (user_choice == ROCK and comp_choice == SCISSORS) or 
            (user_choice == SCISSORS and comp_choice == PAPER) or 
            (user_choice == PAPER and comp_choice == ROCK)):
            print('You win')
    else:
            print('You lose')

def play_game():
     while True:
        user_choice = get_user_choice()

        comp_choice = random.choice(choices)

        display_choices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)

        user_play = input('Continue? (y/n): ').lower()
        if user_play == 'n':
            print('thank you for playing!')
            break

play_game()




# refactoring - changeing the  structure of code without changeing is funcationality 
# modularization - breaking downa large progrma into smaller reusable parts called modules or functions 

# Dry Principle: Dnt repeat yourself - no repetion or duplicates in code 