# Quiz Generator!
**Running a pub quiz or a quiz night for your friends? Or just love quizzing and want to play alone? Generate your own quiz with the *Quiz Generator*!**

## Setup:
- In terminal, type: ```pip install requests```
- No API key needed
- Other modules are in the python standard library
- ‘Open Trivia Database’ API is being used to generate quiz questions
- 10 questions are generated at the start of the game, once the user selects question category

## Additional modules:
- import random: used to create a random integer to randomise the possible answers
- import html: used to unescape escape characters in questions/ escape user responses
- import csv: needed to create cvs writer() object to write dictionary to csv file

## Play:
- Press 'run code' or type ```python3 main.py``` into your terminal
- Type 'yes' if you are ready to play
- Choose a category for your questions
- Play the game in the terminal by typing your response 
- A complete copy of the quiz is written to a file (```quiz_questions.csv```) at the end for you to use with your friends!
- There are 10 questions in each round and you will receive your score at the end of the game!
