# The random2 module is a python module that implements pseudo-random generators for various distributions
# here is an example of some of its methods.


# import necessary library.
import random2 as r2

# random() results in a float between 0 and 1
num = r2.random()
print(num)

# randint() results in an integer between two given parameters
num_int = r2.randint(30,60)
print(num_int)

# uniform() results in a float number between two given parameters
num_uni = r2.uniform(1, 100)
print(num_uni)

# sample() returns a random portion of a list in no particular order
my_list = ['BeBe Zahara Benet', 'Tyra Sanchez', 'Raja', 'Jinx Monsoon', 'Sharon Needles','Bianca Del Rio']
list_sample = r2.sample(my_list, k=3)
print(list_sample)

# randrange() returns a number on the range set (low, high, range)
num_range = r2.randrange(3,33,3)
print(num_range)

# choice() returns a random element from a sequence (list, tuple, etc.)
list_choice = r2.choice(my_list)
print(list_choice)
