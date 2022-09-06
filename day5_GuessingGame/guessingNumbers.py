# import necessary libraries
import random2

# introduce the game rules
print('\nHey there buddy! \nI\'m thinking of a number between 1 and 10. \nGuess what it is...Go ahead!')

# the random integer method from random2 library applied to a range between 1 and 10 and saved in a variable
computer_num = random2.randint(1, 10)

# begin game play
PLAY = True
while PLAY:
  # player must enter a guess. assign it a to a varaible
    player_guess = int(input('Enter a guess...'))
  # comparing the player input against the random integer chosen by computer
    if player_guess > computer_num:
      print("That number is too high. Press enter to try again")
    elif player_guess < computer_num:
      print("That number is too low. Press enter to try again")
  # when player guess, alert them of the win and ask if they want to play again
    else:
      print("Con-Drag-ulations!! You have guessed the correct number! \nYou must be a genius:)\nDo you want to play again? (y/n)")
  # if player chooses yes, the while loop remains true and repeats
  # if player chooses no, the while loop is false, closes and prints a farewell greeting
    if input() != "n":
      continue
    PLAY = False
    print("\nUntil next time then. Thanks for playing!! :)")
