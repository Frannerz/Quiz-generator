import requests
import random

question_number = 0
score = 0

def generate_random_num(length):
    return random.randint(0,length)

url = 'https://opentdb.com/api.php?amount=1&category=9'

def increase_score():
    global score
    score+=1

def increase_question_number():
    global question_number
    question_number+=1

def correct_answer():
    print("That's correct!")
    increase_score()
    increase_question_number()
    generate_new_question()

def incorrect_answer():
    print("Sorry, that's incorrect")
    increase_question_number()
    generate_new_question()

def check_answer(user_response, data):
    if user_response == data['results'][0]['correct_answer']:
        correct_answer()
    else:
        incorrect_answer()

def true_or_false_question(question, data):
    print('True or false?', question)
    user_response = input("Type 'true' or 'false'")
    check_answer(user_response, data)

def multiple_choice_question(data):
    correct_answers = data['results'][0]['correct_answer']
    incorrect_answers = data['results'][0]['incorrect_answers']
    random_num = generate_random_num(len(incorrect_answers))
    possible_answers = incorrect_answers[:]
    possible_answers.insert(random_num, correct_answers)
    print(possible_answers)
    user_response = input('Enter the correct answer. Make sure you check your spelling!')
    check_answer(user_response, data)

def check_question_type(data):
    question = data['results'][0]['question'] 
    print(question)
    type = data['results'][0]['type']
    if type == 'boolean':
        true_or_false_question(question, data)
    if type == 'multiple':
        multiple_choice_question(data)

def generate_new_question():
    if question_number <10:
        response = requests.get(url)
        data = response.json()
        check_question_type(data)
    else:
        print(f'End of quiz, you scored {score}')


def start_quiz():
    generate_new_question()

print('Welcome to the Film Quiz!')
are_you_ready = input("Are you ready? Type 'yes' or 'no'!")

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
# replace chars in questions: &ldquo;    &quot;  &oacute;  &#039;  &rsquo;
# use find and replace
# join list to remove brackets in question
    

# next steps:
# add in choice of quiz type at start
# add questions to array/object
# add each object to a file


# You should use:
# done:
# boolean values and if..else statements to branch logic of your program a data structure like a list, dictionary, set or tuple to store values
# string slicing
# any free API to get some information as json.
# Import an additional module and use it. If it needs to be installed, explain how to do that in the comments, and briefly note what it is for.


# to do:
# a for loop or a while loop to reduce repetition
# functions with returns to make code reusable
# at least two inbuilt functions
# + Add comments to explain how your instructor can set up any necessary API keys and briefly how you are using the API
# + Write your final results to a file