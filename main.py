import requests
import random
import html

question_number = 1
score = 0
response = None
data = None
question = None
correct_answer = None
incorrect_answers = None
quiz = {}


def generate_random_num(length):
    return random.randint(0,length)

url = 'https://opentdb.com/api.php?amount=1&category=9'

def increase_score():
    global score
    score+=1

def increase_question_number():
    global question_number
    question_number+=1

def handle_correct_answer():
    print("\nThat's correct!\n\n")
    increase_score()
    increase_question_number()
    generate_new_question()

def handle_incorrect_answer():
    global correct_answer
    print(f"\nSorry, that's incorrect. The correct answer is {correct_answer}\n\n")
    increase_question_number()
    generate_new_question()

def check_answer(user_response):
    global data, correct_answer
    if user_response.lower() == correct_answer.lower():
        handle_correct_answer()
    else:
        handle_incorrect_answer()

def format_answers(answers):
    return [html.unescape(word) for word in answers]

def true_or_false_question():
    global question, data
    print(f"{question_number}. {question}\n")
    user_response = input("Type 'True' or 'False': ")
    check_answer(user_response)

def format_multiple_choice_answers(answers):
    return ', '.join(answers[0:3])+ " or "+ answers[3] +"?"
    
def multiple_choice_question():
    global correct_answer, question, incorrect_answers, data, question_number
    random_num = generate_random_num(len(incorrect_answers))  
    possible_answers = incorrect_answers[:]
    possible_answers.insert(random_num, correct_answer)
    possible_answers = format_answers(possible_answers)
    possible_answers = format_multiple_choice_answers(possible_answers)
    print(f"{question_number}. {question}\n")
    print(possible_answers, "\n")
    user_response = input('Enter the correct answer: ')
    check_answer(user_response)

def check_question_type():
    global question, data
    type = data['results'][0]['type']
    if type == 'boolean':
        true_or_false_question()
    if type == 'multiple':
        multiple_choice_question()

def get_question():
    global question
    question = data['results'][0]['question'] 
    question = html.unescape(question)


def get_answers():
    global correct_answer, incorrect_answers, data
    correct_answer = data['results'][0]['correct_answer']
    incorrect_answers = data['results'][0]['incorrect_answers']
    return correct_answer, incorrect_answers

def create_quiz_question():
    global question_number, correct_answer, incorrect_answers, quiz, question, answer
    quiz[question_number] = {'question': question, 'correct answer': correct_answer, 'incorrect answers': incorrect_answers or []}  
    
def generate_new_question():
    global data, quiz
    if question_number <11:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                get_question()
                get_answers()
                create_quiz_question()
                check_question_type()
            else:
                generate_new_question()
        except:  
            print('An error occurred')   
            generate_new_question()
    else: 
        print(f'\nEnd of quiz, you scored {score}\n')
        print(quiz)


def start_quiz():
    print("\n")
    generate_new_question()


print('Welcome to the Quiz!\n')
are_you_ready = input("Are you ready? Type 'yes' or 'no'! ")

if are_you_ready == 'yes':
    start_quiz()


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
# add in choice of quiz type at start
# add questions to array/object
# add each object to a file
# handle errors!!

# You should use:
# done:
# boolean values and if..else statements to branch logic of your program a data structure like a list, dictionary, set or tuple to store values
# string slicing
# any free API to get some information as json.
# Import an additional module and use it. If it needs to be installed, explain how to do that in the comments, and briefly note what it is for.
# a for loop or a while loop to reduce repetition
# functions with returns to make code reusable
# at least two inbuilt functions (print, input, join)
    

# to do:
# + Add comments to explain how your instructor can set up any necessary API keys and briefly how you are using the API
# + Write your final results to a file