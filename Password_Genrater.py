import random
import string


adjectives = ['sleepy', 'slow', 'smelly',
              'wet', 'fat', 'red',
              'bad', 'good', 'mad',
              'tall', 'tiny', 'small',
              'big', 'slim', 'pink']


nouns = ['apple', 'dinosaur', 'Eman',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']

print('Welcome to Password Picker!')

while True:

  for num in range(3):
   adjective = random.choice(adjectives)
   noun = random.choice(nouns)
   number = random.randrange(0, 100)
   special_char = random.choice(string.punctuation)

   password = adjective + noun + str(number) + special_char
   print('You new password is: %s' % password)

   response = input('Would you like another password? Type y or n: ')
   if response == 'n':
    response = input('Thank you for using this app!')
    break
   

    
   
