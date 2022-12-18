
import random
from words import words
from hungman import lives_left
import string
from time import sleep

#colors for the game 
class colors:
    purple = '\033[95m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[91m'
    orange = '\033[33m'
    white = '\033[0m'
    bold = '\033[1m'

def player_name():
    """
    player has enter their name . 
    This will be used in game so their name will be used,
     in the game to wish them luck
     """
     global name
     while True:
         name = input("\nWho is playing ?")
         if name.isalpha():
             break
        print(colors.green + "Valid letters (A-Z)only please.\n"  + colors.white)
     sleep(1)
     print("\nGood luck to you," + colors.red + f"{name.capitalize()}!")
     return name    

def get_word(words):
    """
    chooses random words from 'words.py' file
    is skipped when invalid words
    """
    word = random.choice(words)

    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()
    
        
def hungman_game(): 
def hangman_logo():
def welcome_rules():
def choose_level():

sleep(1)
hangman_logo()
    
    