#  --- this script allows user to choose between several different dice options ---


# import necessary libraries
import random2

# define a dictionary to hold key value pairs of dice information.
# dice can be any size needed. range of the dice number options (value) must match dice name (key)
# player is able to choose from different dice options
dice_options = {
      "dice6": (1,6),
      "dice18": (1,18),
      "dice34": (1,34),
      "dice60": (1,60)
    }

# invite user to roll dice
game_play = input('\nShall we roll some dice? type yes or no: ')

let_the_dice_roll = True
while let_the_dice_roll:
  if game_play == "yes":
# user inputs which dice needed
    dice_chosen = input("\nPlease choose your dice from the following options:\n dice6, dice18, dice34 or dice60: ").lower()
# match the dice chosen to the dice/range in the dictionary and assign to a new variable
    dice_being_rolled = dice_options[dice_chosen]
# using the randint method fromt the random module, a random integer is chosen and printed to the console
    print("\nThe die has been cast! \nYour number is: ", random2.randint(dice_being_rolled[0], dice_being_rolled[1]))
    dice_continue = (input("\nPress enter to roll again. \n Or \nType \"see ya\" to leave the game. ").lower())
    if dice_continue == "y":
      continue
    elif dice_continue == ("see ya"):
      let_the_dice_roll = False
      print('Well I had a great time. Thanks for rollin :)')
  elif game_play == "no":
    let_the_dice_roll = False
    print("\nFarewell! Stay Thirsty!")
