import requests
import random
import html
import csv

# FOR SETUP AND INSTRUCTIONS: SEE README.md

class Quiz: 
    def __init__(self):
        self.index = 0
        self.question_number = 1
        self.score = 0
        self.chosen_genre = None
        self.data = None
        self.question = None
        self.correct_answer = None
        self.incorrect_answers = None
        self.quiz = {}
        self.urls = ['https://opentdb.com/api.php?amount=10&category=9','https://opentdb.com/api.php?amount=10&category=11','https://opentdb.com/api.php?amount=10&category=12','https://opentdb.com/api.php?amount=10&category=14','https://opentdb.com/api.php?amount=10&category=17','https://opentdb.com/api.php?amount=10&category=21','https://opentdb.com/api.php?amount=10&category=23', 'https://opentdb.com/api.php?amount=10&category=22']
        self.genres = ['general Knowledge', 'film', 'music', 'television', 'science and nature','sports', 'history', 'geography']

    def increase_score(self):
        self.score+=1

    def increase_question_number(self):
        self.question_number+=1

    def increase_index_number(self):
        self.index+=1

    def handle_correct_answer(self):
        print("\nThat's correct!\n\n")
        self.increase_score()
        self.increase_question_number()
        self.increase_index_number()
        if self.question_number < 11:
            self.get_question()
            self.get_answers()
            self.create_quiz_question()
            self.check_question_type()
        else:
            self.end_quiz()
    
    def handle_incorrect_answer(self):
        print(f"\nSorry, that's incorrect. The correct answer is {html.unescape(self.correct_answer)}\n\n")
        self.increase_question_number()
        self.increase_index_number()
        if self.question_number < 11:
            self.get_question()
            self.get_answers()
            self.create_quiz_question()
            self.check_question_type()
        else:
            self.end_quiz()

    def check_answer(self, user_response):
        if user_response.lower() == self.correct_answer.lower():
            self.handle_correct_answer()
        else:
            self.handle_incorrect_answer()

    def format_answers(self, answers):
        return [html.unescape(word) for word in answers]

    def true_or_false_question(self):
        print(f"Question {self.question_number}. {self.question}\n")
        while True:
            user_response = input("Type 'True' or 'False': ")
            if user_response.lower() == 'true' or user_response.lower() == 'false':
                self.check_answer(user_response)
                break
            else:
                print('Please enter true or false: ')
        

    def format_multiple_choice_answers(self, answers):
        return ', '.join(answers[0:3])+ " or "+ answers[3] +"?"
    
    def multiple_choice_question(self):
        random_num = generate_random_num(len(self.incorrect_answers))  
        possible_answers = self.incorrect_answers[:]
        possible_answers.insert(random_num, self.correct_answer)
        possible_answers = self.format_answers(possible_answers)
        possible_answers = self.format_multiple_choice_answers(possible_answers)
        print(f"Question {self.question_number}. {self.question}\n")
        print(possible_answers, "\n")
        while True:
            user_response = input('Enter the correct answer: ').strip()
            user_response = html.escape(user_response)
            if user_response == '':
                print('Please enter a response')
            elif user_response.lower() in possible_answers.lower():
                self.check_answer(user_response)
                break
            else:
                print('Please enter an answer from the list.')

    def check_question_type(self):
        type = self.data['results'][self.index]['type']
        if type == 'boolean':
            self.true_or_false_question()
        if type == 'multiple':
            self.multiple_choice_question()

    def get_question(self):
        self.question = self.data['results'][self.index]['question'] 
        self.question = html.unescape(self.question)

    def get_answers(self):
        self.correct_answer = self.data['results'][self.index]['correct_answer']
        self.incorrect_answers = self.data['results'][self.index]['incorrect_answers']
        return self.correct_answer, self.incorrect_answers

    def create_quiz_question(self):
        self.quiz[self.question_number] = {'question': self.question, 'correct answer': self.correct_answer, 'incorrect answers': self.incorrect_answers}  

    def prepare_data_for_csv(self):
        rows = []
        for key, value in self.quiz.items():
            question_number = key
            question = value['question']
            correct_answer = value['correct answer']
            incorrect_answers = ';'.join(value['incorrect answers'])
            rows.append([question_number, question, correct_answer, incorrect_answers])
    
        quiz_file = 'quiz_questions.csv'

        with open(quiz_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Question Number','Question', 'Correct Answer', 'Incorrect Answers'])
            writer.writerows(rows)
        print('Quiz written to file!')

    def play_again(self):
        play_again_choice = input("Do you want to play again?\n Enter 'yes' or 'no': ")
        if play_again_choice == 'yes':
            new_quiz()
        else:
            print("Thanks for playing! See you again soon.")
            return

    def end_quiz(self):
        self.prepare_data_for_csv()
        print(f'\nEnd of quiz, you scored {self.score}\n')
        self.play_again()
        
    def generate_new_questions(self):
        try:
            response = requests.get(self.chosen_genre)
            if response.status_code == 200:
                self.data = response.json()
                self.get_question()
                self.get_answers()
                self.create_quiz_question()
                self.check_question_type()
            else:
                self.generate_new_questions()
        except Exception as e:  
            print(f'An error occurred: {e}')   

    def generate_title(self, index):
        genre = self.genres[index]
        length = len(genre)+21
        stars = '*' * length
        print(f'\n{stars}\nWelcome to the {genre} quiz!\n{stars}\n')
            
    def choose_quiz_genre(self):
        while True:
            try:
                genre_choice = int(input('Choose your quiz genre.\n Type:\n 0 for general knowledge\n 1 for film\n 2 for music\n 3 for television\n 4 for science and nature\n 5 for sports\n 6 for history\n 7 for geography\nYour choice: '))
                if 0 <= genre_choice <= 7:
                    break
                else: 
                    print('\nPlease type an integer between 0 and 7\n')
            except ValueError:
                print("\nThat's not an integer. Please try again with a number between 0 and 7.\n")
    
        self.chosen_genre = self.urls[genre_choice]
        self.generate_title(genre_choice)
        self.generate_new_questions()
    
    def start_quiz(self):
        print("\n")
        self.choose_quiz_genre()

# END OF QUIZ CLASS
        
# COMMON FUNCTIONS

def generate_random_num(length):
    return random.randint(0,length)

def new_quiz():
    start_new_quiz = Quiz()
    start_new_quiz.start_quiz()

# START THE GAME
print('\nWelcome to the Quiz!\n')

def ready_to_play():
    are_you_ready = input("Are you ready? Type 'yes' or 'no'! ")
    while are_you_ready == '':
        are_you_ready = input("Please type 'yes' or 'no'! ")
    if are_you_ready.lower() == 'yes':
        new_quiz()
    else:
        print('Hope to see you soon!\n') 

ready_to_play()


# next steps:
# validate responses


# You should use:
# done:
# boolean values and if..else statements to branch logic of your program a data structure like a list, dictionary, set or tuple to store values
# string slicing
# any free API to get some information as json.
# Import an additional module and use it. If it needs to be installed, explain how to do that in the comments, and briefly note what it is for.
# a for loop or a while loop to reduce repetition
# functions with returns to make code reusable
# at least two inbuilt functions (print, input, join)
# + Write your final results to a file

# to do:
# + Add comments to explain how your instructor can set up any necessary API keys and briefly how you are using the API
