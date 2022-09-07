
import random2

dice_options = {
      "dice6": (1,6),
      "dice18": (1,18),
      "dice34": (1,34),
      "dice60": (1,60)
    }

game_play = input('\nShall we roll some dice? type yes or no: ')
dice_chosen = input("\nPlease choose your dice from the following options:\n dice6, dice18, dice34 or dice60: ").lower()
user_dice = dice_chosen
let_the_dice_roll = True
while let_the_dice_roll:
  if game_play == "yes":
    dice_being_rolled = dice_options[dice_chosen]
    print("\nThe die is cast and your number is\n: ", random2.randint(dice_being_rolled[0], dice_being_rolled[1]))
    dice_continue = (input("\nPress enter to roll again. \n Or \nType \"see ya\" to leave the game. ").lower())
    if dice_continue == "y":
      user_dice = True
    elif dice_continue == ("see ya"):
      let_the_dice_roll = False
      print('Well I had a great time. Thanks for rollin :)')
  elif game_play == "no":
    let_the_dice_roll = False
    print("\nFarewell! Stay Thirsty!")
