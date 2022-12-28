# Hungman game 
Welcome to hungman game , this is a python terminal game which is deployed to the Heroku. The main aim of this game is for the user to have fun while guessing a random word within in the given limmited life. The difficulty of this game is selected by the user.

The user can play the game at three different levels of difficulty, based on the number of lives the have: 5 lives for EASY, 7 for MEDIUM and 10 for HARD. The player wins the game if they guess the word correctly in the allotted number of guesses; Otherwise game is over.

When the game is over the user will be aske if the wanted to start over or just leave the game.  While pressing 'Y' will restart the game with a new random word and the difficulty level chosen by the player.If any other key is pressed apart from Y ('N' or another character) will conclude the game with a 'Thanks for playing...' message followed by the Hangman logo.

live webesite for game [here](https://hungman-1.herokuapp.com/).

![The Hungman Game!](/assets/frontpage.png)

## FlowChart
The game work flow was created from using [Lucid](http:lucid.app). Here you can see how the game works from the starting to end ß


![FlowChart](./assets/flowchart.png)

## Playing The Game 
The user is asked at the start and the user has to select H,M or E so the game can identify the level and random word will be shown. then the user has to guess 1 letter at a time. If the letter is not in the word, a life will be lost and a part of the gallows or a body part of the figure will appear or else If the letter is part of the word, it will appear in one of the blank spaces.

The game has the same rule like all the other hungman game guess the correct word and win or lose & get hunged. 

## Features 

* A logo or Tittle is shown in the start of the game. various colors are also used such as green, cyan, red, green and yellow for levels and lives 

![Welcome Message](/assets/hungmanlogo.png)

* The game ask the user their name and greets them and wish 
 them good luck 

 ![Greeting the user](/assets/whoisplaying.png)

*  Next step the player has to choose the level (easy, medium, hard) and the number of lives is reflected (10, 7, 5, respectively).

![Level](/assets/level.png)

* Like any other hungman game a wrong letter is entered then a life will be gone 

![lives](/assets/currentword.png)

* Current letters is showed so user can know that he have already typed

![current](/assets/currentword.png)

* If the user types same letter 2 times or any other more than one then, the game will ask them to correct it but no lives will reduced from their game. 


* The game will identify if the letter which is entered is not part of the game , and 1 life will be reduced after that hungman picture is shown has per the difficulty level choosed by the user 

![Incorrect letter](/assets/3.png)

* If the user wins or lose then these message are showed by their name 

![Hunged](/assets/lose.png)

![congrats](/assets/win.png)








