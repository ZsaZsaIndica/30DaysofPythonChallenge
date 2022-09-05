# Rock Paper Scissors against the Computer


# import necessary libraries
import random2

# print title of the game and instructions
PLAY = True
while PLAY:
    print('\nBonjour! Let\'s play Rock, Paper, Scissors. Here are the rules: \n rock vs paper = paper wins \n rock vs scissors = rock wins \n paper vs scissors = scissors wins.')

# ask player to choose between rock paper or scisscors as an input
    user_choice = input('\nAre you ready? Choose your weapon! rock, paper or scissors: ')

# tell the player their choice and print next step in the game which is the computer choosing
    print(f'\n{user_choice} is an excllent choice. Now it\'s my turn')

# assign computer choices to a variable for later use
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random2.choice(computer_choices)

# print the computer's choice
    print(f'\nI have chosen {computer_choice} as my weapon of defense!')

# compare the choices for the rules of the game
    if user_choice == computer_choice:
      print('\nWould you look at that? We picked the same thing...It\'s a tie. Rather unsatisfying, if you ask me...')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('\nCon-Dragulations! Rock smashes Scissors! You\'re a winner, baby!')
    elif user_choice == 'rock' and computer_choice == 'paper':
       print('\nI\'m sorry, my dear. You are up for elimination. Paper beats Rock. You\'ll have to Sashey Away.')
    elif user_choice == 'paper' and computer_choice == 'rock':
       print('\nCon-Dragulations! Paper covers Rock! You\'re a winner, baby!')
    elif user_choice =='paper' and computer_choice == 'scissors':
       print('\nI\'m sorry, my dear. You are up for elimination. Scissors cuts Paper. You\'ll have to Sashey Away.')
# ask the user if they want to continue play
    print("\nDo you want to play again? (y/n)")
    if(input() == "n"):
      PLAY = False
      print("No Worries! Have a groovy day and Thanks for playing!! :)")
    else:
      continue
