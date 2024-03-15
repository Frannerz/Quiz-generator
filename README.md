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


## Project assessment criteria:
- Use boolean values and if..else statements to branch logic of your program: see line 36
- Use a data structure like a list, dictionary, set or tuple to store values: see lines 19 and 115
- Use a for loop or a while loop to reduce repetition functions with returns to make code reusable: see lines 63 and 119
- Use string slicing: see line 81
- Use at least two inbuilt functions: see lines 57, 77 and 82 
- Use any free API to get some information as json: see lines 149-151
- Add comments to explain how your instructor can set up any necessary API keys and briefly how you are using the API: see README **setup**
- Import an additional module and use it. If it needs to be installed, explain how to do that in the comments, and briefly note what it is for: see **setup** and **modules** section of README 
- Write your final results to a file: see lines 128-131
