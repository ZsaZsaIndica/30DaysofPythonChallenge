# import necessary libraries
import random2

# greetings and ask if the user wants to join the game
game_greeting = input('Hey there! Lets play a game to create a random number. Are you interested? Please type yes or type no: ')

# if the user accepts, begin the game
if game_greeting == 'yes':
  # define variables for number parameters
  low_num = int(input('Please choose your lowest number: '))
  high_num = int(input('Please choose your highest number: '))
  # print the number created to the console
  print('The number you have created is: ', int(random2.uniform(low_num, high_num)),' Thanks for playing :)')
# if the user declines the game, print a farewell message
elif game_greeting =='no':
  print('No worries. Have a groovy day')
