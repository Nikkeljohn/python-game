# Hungman game 
Welcome to hungman game , this is a python terminal game which is deployed to the Heroku. The main aim of this game is for the user to have fun to guess a random word wirhin in the given limmited life. The difficulty of this game is selected by the user.

The user can play the game at three different levels of difficulty, based on the number of lives the have: 5 lives for EASY, 7 for MEDIUM and 10 for HARD. The player wins the game if they guess the word correctly in the allotted number of guesses; Otherwise game is over.

When the game is over the user will be aske if the wanted to start over or just leave the game.  While pressing 'Y' will restart the game with a new random word and the difficulty level chosen by the player.If any other key is pressed apart from Y ('N' or another character) will conclude the game with a 'Thanks for playing...' message followed by the Hangman logo.

live webesite for game [here](https://hungman-1.herokuapp.com/).

![The Hungman Game!](/assets/frontpage.png)

## FlowChart
The game work flow was created from using [Lucid](http:lucid.app). Here you can see how the game works from the starting to end ß


![FlowChart](./assets/flowchart.png)

## Playing The Game 
The user is asked at the start and the user has to select H,M or E so the game can identify the level and random word will be shown. then the user has to guess 1 letter at a time. If the letter is not in the word, a life will be lost and a part of the gallows or a body part of the figure will appear or else If the letter is part of the word, it will appear in one of the blank spaces.

