# Created by Muhammad Ahmed
# Checkout my Portfolio https://a03152049334.wixsite.com/muhammadahmed
# Checkout my Fiverr account https://www.fiverr.com/ahmed189
# Checkout my Upwork account https://www.upwork.com/freelancers/~01e248930a029b5290
# Follow me on LinkedIn http://www.linkedin.com/in/muhammad-ahmed189
# Follow me on GitHub https://github.com/MuhammadnAhmed

import random

# game function
def game():
    # user selection
    user = (input("\nPlease input 'r' for Rock, 'p' for Paper, Or 's' for scissors!  ")).lower()

    # computer selection
    computer = random.choice(['r', 'p', 's'])
    # check invalid selection of user
    while (user != 'r') and (user != 'p') and (user != 's'):
        user = (input("\nInvalid Answer\nPlease input 'r' for Rock, 'p' for Paper, Or 's' for scissors!\n ")).lower()

    # Display Choices
    display_choices(user, computer)

    # checking if the game is tied
    if user == computer:
        print('\nGame Tie')
    # checking the winner
    if check_win(user, computer):
        print('\nYou won the game! ')
    if check_win(computer, user):
        print('\nYou lost the game!')

    permission = (input('Press 1 to play again\n OR Press any key to exit..!\n'))
    if permission == '1':
        game()
    else:
        exit()

# Function to check if the player wins
def check_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (
            player == 's' and computer == 'p'):
        return True


# Function to show choices being made
def display_choices(player, computer):
    print("\nYour Choice = " + player + " \nComputer Choice = " + computer)


game()
