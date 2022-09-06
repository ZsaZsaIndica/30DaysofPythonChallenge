#  ---  this script has one dice option with range of 1-6  ---


# import necessary libraries
import random2

# ask the user if they want to play . if yes, start the dice roll. if no, print a farewell statement
player_choice = (input('\nOkey dokey, folks! \nStep on up for the Dice Roll of the Century! \nReady to roll the 6-sided dice? \nyes or no?'))

# assign game to boolean for intitation
let_the_dice_roll = True
while let_the_dice_roll:
  if player_choice == "yes":
    dice_roll = random2.randint(1,6)
    print("\nThe die is cast! \nThe number given is a: ", dice_roll)
# give user option to roll again
    dice_continue = (input("Press Enter to roll again. \n Or \nType \"see ya\" to leave the game. ").lower())
    if dice_continue == "y":
      continue
    elif dice_continue == ("see ya"):
      let_the_dice_roll = False
      print('Well I had a great time. Thanks for rollin :)')
# if user chooses to not play at all, print a farewell statement
  elif player_choice == "no":
    let_the_dice_roll = False
    print("\nFarewell! Stay Thirsty!")
