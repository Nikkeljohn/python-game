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
    """
    making user to make guess a random words if 
    letters are wrong then it effect the lives
    """
    hangman_logo()
    game_rules()
    word = get_word(words)
    letter_used = set(word)
    letter = set(string.ascii_uppercase)
    letter_choose = set()

    lives = choose_level()

    while len(letter_used) > 0 and lives > 0:
        print("\nYou choose these Alphabet:", ' '.join(sorted(letter_choose)))
        print('\nLifes left',lives)

        user_choice = input('\nPlease choose a letter').upper()

        if user_choice in letter - letter_choose:
            letter_choose.add(user_choice)
            if user_choice in letter_used:
                letter_used.remove(user_choice)
                print('')

            else:
                lifes = lives - 1
                print('\nSorry', user_choice, 'is not the letter.')
        elif user_choice in letter_choose:
             print('\nYou have already selected this letter before, try agian')

        else:
            print("\nPlease try agin with valid letters,A-Z")
            
# when player lose
    if lives == 0:
        print(colors.orange + lives_left[lives] + colors.white)
        print(colors.bold + f"Am really sorry, {name.capitalize()},you have been hanged!")
        print("The answer was" + colors.green, word + colors.white)
    else:
        print(colors.bold + f"Well done {name.capitalize()}!")
        print("Congrats your answer is" + colors.cyan, word + colors.white)    
                        

def hangman_logo():
    """
    hungman logo is shown in the cyan color in the beginning of the game
    """
    print(colors.cyan + """
       _   _                                         _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
        | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |_|
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)
                            |___/
        """ + colors.white)


def game_rules():
    """
    greets the user to the game 
    tells the rules , and allow them to choose level(easy,medium and hard)
    """
    print("Greetings from Hungman! \n")
    sleep(1)
    print("Guess the Answer before you are hunged. \n")
    sleep(1)
    print("Select a level (easy, medium or hard ), and follow the rules. \n")
    sleep(1)
    print("--------------------------")
    sleep(1)

def choose_level():
    """
    Enter 'e','m', or 'h' and choose a level:
    easy(10 lives), medium (7 lives) and hard(5 lives).
    """
    print(colors.white + "\n To start game , please choose...\n") 
    print(colors.green, 'E' + colors.white, "for easy \n")
    print("You have " + colors.cyan, "10 lives. \n" + colors.white)
    sleep(1)
    print(colors.orange, "M" + colors.white, "for medium \n")
    print("you have" + colors.orange, "7 lives. \n" + colors.white)
    sleep(1)
    print(colors.red, "H" + colors.white, " for hard \n")
    print("You have" + colors.red, "5 lives. \n" + colors.white)

    difficult = True
    while difficult:
        options = input("\n ").upper()
        if options == "E":
            lives = 10
            return lives
        elif options == "M":
            lives = 7
        elif options == "H":
            lives = 5
        else: 
            print(colors.red + "\n Please enter E, M or H" + colors.white)
            print("Select your level of difficulty.")

hungman_game()

while True:
    if input("Would you like to have a rematch? preys any key = quit, Y = start again").upper() == "Y":
        hungman_game()
    else:
        print(colors.purple + "Thanks for playing Hungman.. \n")   
        break 


sleep(1)
hangman_logo()
    
    