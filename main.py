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
        self.get_question()
        self.get_answers()
        self.create_quiz_question()
        self.check_question_type()
    
    def handle_incorrect_answer(self):
        print(f"\nSorry, that's incorrect. The correct answer is {html.unescape(self.correct_answer)}\n\n")
        self.increase_question_number()
        self.increase_index_number()
        self.get_question()
        self.get_answers()
        self.create_quiz_question()
        self.check_question_type()

    def check_answer(self, user_response):
        if user_response.lower() == self.correct_answer.lower():
            self.handle_correct_answer()
        else:
            self.handle_incorrect_answer()

    def format_answers(self, answers):
        return [html.unescape(word) for word in answers]

    def true_or_false_question(self):
        print(f"{self.question_number}. {self.question}\n")
        user_response = input("Type 'True' or 'False': ")
        self.check_answer(user_response)

    def format_multiple_choice_answers(self, answers):
        return ', '.join(answers[0:3])+ " or "+ answers[3] +"?"
    
    def multiple_choice_question(self):
        random_num = generate_random_num(len(self.incorrect_answers))  
        possible_answers = self.incorrect_answers[:]
        possible_answers.insert(random_num, self.correct_answer)
        possible_answers = self.format_answers(possible_answers)
        possible_answers = self.format_multiple_choice_answers(possible_answers)
        print(f"{self.question_number}. {self.question}\n")
        print(possible_answers, "\n")
        user_response = input('Enter the correct answer: ')
        self.check_answer(user_response)

    def check_question_type(self):
        type = self.data['results'][self.index]['type']
        if type == 'boolean':
            self.true_or_false_question()
        if type == 'multiple':
            self.multiple_choice_question()

    def get_question(self):
        if self.question_number < 11:
            self.question = self.data['results'][self.index]['question'] 
            self.question = html.unescape(self.question)
        else: 
            self.end_quiz()

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
        print('data written to file')

    # def reset_initial_values():
    #     index = 0
    #     question_number = 1
    #     score = 0
    #     quiz = {}

    def play_again(self):
        # global are_you_ready
        play_again_choice = input("Do you want to play again?\n Enter 'yes' or 'no': ")
        if play_again_choice == 'yes':
            new_quiz()
            # self.start_quiz()
            # reset_initial_values()
        else:
            # are_you_ready = 'no'
            print("Thanks for playing! See you again soon.")
            # reset_initial_values()

    def end_quiz(self):
        self.prepare_data_for_csv()
        print(f'\nEnd of quiz, you scored {self.score}\n')
        self.play_again()
        # print(quiz)
        
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
            

    def choose_quiz_genre(self):
        genre_choice = int(input('Choose your quiz genre.\n Type:\n 0 for general knowledge\n 1 for film\n 2 for music\n 3 for television\n 4 for science and nature\n 5 for sports\n 6 for history\n 7 for geography\nYour choice: '))
        self.chosen_genre = self.urls[genre_choice]
        self.generate_new_questions()
    
    def start_quiz(self):
        print("\n")
        self.choose_quiz_genre()


#START OF ORIGINAL CODE
# index = 0
# question_number = 1
# score = 0
# chosen_genre = None
# data = None
# question = None
# correct_answer = None
# incorrect_answers = None
# quiz = {}


def generate_random_num(length):
    return random.randint(0,length)

# urls = ['https://opentdb.com/api.php?amount=10&category=9','https://opentdb.com/api.php?amount=10&category=11','https://opentdb.com/api.php?amount=10&category=12','https://opentdb.com/api.php?amount=10&category=14','https://opentdb.com/api.php?amount=10&category=17','https://opentdb.com/api.php?amount=10&category=21','https://opentdb.com/api.php?amount=10&category=23', 'https://opentdb.com/api.php?amount=10&category=22']
# #0:general knowledge, 1:film, 2:music, 3:television, 4:science and nature, 5:sports, 6:history, 7:geography

# def increase_score():
#     global score
#     score+=1

# def increase_question_number():
#     global question_number
#     question_number+=1

# def increase_index_number():
#     global index
#     index+=1

# def handle_correct_answer():
#     print("\nThat's correct!\n\n")
#     increase_score()
#     increase_question_number()
#     increase_index_number()
#     get_question()
#     get_answers()
#     create_quiz_question()
#     check_question_type()
    
# def handle_incorrect_answer():
#     global correct_answer
#     print(f"\nSorry, that's incorrect. The correct answer is {html.unescape(correct_answer)}\n\n")
#     increase_question_number()
#     increase_index_number()
#     get_question()
#     get_answers()
#     create_quiz_question()
#     check_question_type()

# def check_answer(user_response):
#     global data, correct_answer
#     if user_response.lower() == correct_answer.lower():
#         handle_correct_answer()
#     else:
#         handle_incorrect_answer()

# def format_answers(answers):
#     return [html.unescape(word) for word in answers]

# def true_or_false_question():
#     global question, data
#     print(f"{question_number}. {question}\n")
#     user_response = input("Type 'True' or 'False': ")
#     check_answer(user_response)

# def format_multiple_choice_answers(answers):
#     return ', '.join(answers[0:3])+ " or "+ answers[3] +"?"
    
# def multiple_choice_question():
#     global correct_answer, question, incorrect_answers, data, question_number
#     random_num = generate_random_num(len(incorrect_answers))  
#     possible_answers = incorrect_answers[:]
#     possible_answers.insert(random_num, correct_answer)
#     possible_answers = format_answers(possible_answers)
#     possible_answers = format_multiple_choice_answers(possible_answers)
#     print(f"{question_number}. {question}\n")
#     print(possible_answers, "\n")
#     user_response = input('Enter the correct answer: ')
#     check_answer(user_response)

# def check_question_type():
#     global question, data
#     type = data['results'][index]['type']
#     if type == 'boolean':
#         true_or_false_question()
#     if type == 'multiple':
#         multiple_choice_question()

# def get_question():
#     global question
#     if question_number < 11:
#         question = data['results'][index]['question'] 
#         question = html.unescape(question)
#     else: 
#         end_quiz()

# def get_answers():
#     global correct_answer, incorrect_answers, data
#     correct_answer = data['results'][index]['correct_answer']
#     incorrect_answers = data['results'][index]['incorrect_answers']
#     return correct_answer, incorrect_answers

# def create_quiz_question():
#     global question_number, correct_answer, incorrect_answers, quiz, question, answer
#     quiz[question_number] = {'question': question, 'correct answer': correct_answer, 'incorrect answers': incorrect_answers or []}  

# def prepare_data_for_csv():
#     global quiz
#     rows = []
#     for key, value in quiz.items():
#         question_number = key
#         question = value['question']
#         correct_answer = value['correct answer']
#         incorrect_answers = ';'.join(value['incorrect answers'])
#         rows.append([question_number, question, correct_answer, incorrect_answers])
    
#     quiz_file = 'quiz_questions.csv'

#     with open(quiz_file, mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Question Number','Question', 'Correct Answer', 'Incorrect Answers'])
#         writer.writerows(rows)
#     print('data written to file')

# def reset_initial_values():
#     global index, question_number, score, chosen_genre, data, question, correct_answer, incorrect_answers, quiz
#     index = 0
#     question_number = 1
#     score = 0
#     quiz = {}

# def play_again():
#     # global are_you_ready
#     play_again_choice = input("Do you want to play again?\n Enter 'yes' or 'no': ")
#     if play_again_choice == 'yes':
#         start_quiz()
#         reset_initial_values()
#     else:
#         # are_you_ready = 'no'
#         print("Thanks for playing! See you again soon.")
#         reset_initial_values()

# def end_quiz():
#     prepare_data_for_csv()
#     print(f'\nEnd of quiz, you scored {score}\n')
#     play_again()
#     # print(quiz)
        
# def generate_new_questions():
#     global data, quiz
#     try:
#         response = requests.get(chosen_genre)
#         if response.status_code == 200:
#             data = response.json()
#             get_question()
#             get_answers()
#             create_quiz_question()
#             check_question_type()
#         else:
#             generate_new_questions()
#     except Exception as e:  
#         print(f'An error occurred: {e}')   
            

# def choose_quiz_genre():
#     global chosen_genre 
#     genre_choice = int(input('Choose your quiz genre.\n Type:\n 0 for general knowledge\n 1 for film\n 2 for music\n 3 for television\n 4 for science and nature\n 5 for sports\n 6 for history\n 7 for geography\nYour choice: '))
#     chosen_genre = urls[genre_choice]
#     generate_new_questions()

# def start_quiz():
#     print("\n")
#     choose_quiz_genre()
    


def new_quiz():
    start_new_quiz = Quiz()
    start_new_quiz.start_quiz()

print('\nWelcome to the Quiz!\n')
are_you_ready = input("Are you ready? Type 'yes' or 'no'! ")
if are_you_ready == 'yes':
    new_quiz()
else:
    print('Hope to see you soon!') 

# functions: random_number, check_question_type, check_answer, correct_answer, 
# incorrect_answer, new_question, increase_score

#when creating list, insert correct item into random position in correct list

# #for loop with range 10 (or have number_of_questions variable?), 
# # calls url, asks question and puts answers in a list
# # if the inoput reponse.lower() == results.correct_answer.lower(), add 1 to score and say correct!
# # if not correct say sorry, incorrect and give correct answer
# # tell user their score
# # trigger next question
# # after 10 questions- give user their score- you scored 5/10 points!
# # ask question- do you want to play again? if yes- start again!


# Bugs:
    

# next steps:
# add in play again option!
# handle errors!!
# change code to fetch once and then retrieve each question each go

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
