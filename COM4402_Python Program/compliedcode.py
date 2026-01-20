import time
from random import choice

from click.exceptions import Exit
from colorama import Fore, Back, init

init(autoreset=True)

count=0

score=0
total_score=30
user_answers=[]
correct_answers=['b','b','a','a','a','c','b','b','c','b']
username=''
password=''

#Question database. #List of dictionaries being used because it offers us key and value features suitable for quiz questions and right answer.
# List offer 0 , 1 item indexing which we need for quiz questions and correct answers.

#user_database. list of lists is used as it CRUD operations can easily be implemented. List is mutable.
#list maintain order.

user_database=[['harry','ha123'],['william','wi123'],
               ['maria', 'ma123'],['sarah','sa123'],
                ['alina','al123'],['bushra','bu123']]


quiz_questions = [{"Question":"1. Which of the following methods can be used to remove an item from a list?\nA. delete()\nB. remove()\nc. update",
                   "Answer": "b"},
                  {"Question":"2.Which of the following is used to handle multiple exceptions in Python?\na.  except Exception1, Exception2\nb. except (Exception1, Exception2):\nc. except: Exception1, Exception2",
                   "Answer": "b"},
                  {"Question":"3.Which of the following is a Python built-in data type?\na.List\nb.Array\nc.Hash",
                   "Answer":"a"},
                  {"Question":"4.  How do you create a function in Python that takes two parameters?\na.def function(param1, param2): \nb.function(param1, param2): \nc.function: param1, param2 ",
                   "Answer":"a"},
                  {"Question":"5. What is the correct file extension for Python files?\na. .py\nb. .python\nc. .pt",
                   "Answer":"a"},
                   {"Question":"6. What does the `lambda` keyword define in Python?\na.A loop\nb.A class\nc.An anonymous function",
                   "Answer":"c"},
                  {"Question":"7.  What will `lst=[1,2,3]; lst.pop(); print(lst)` output?\na.[1,2,3]\nb.[2,3]\nc.Error",
                   "Answer":"b"},
                  {"Question":"8.  What is the correct way to start a Python script on Unix?\na.#!/usr/bin/python\nb.#!/usr/bin/env python\nc.start python",
                   "Answer":"b"},
                  {"Question":"9.  Which of the following functions can help us to find the version of python that we are currently working on?\na. sys.version(1)\nb.sys.version()\nc.sys.version",
                   "Answer":"c"},
                  {"Question":"10.  What is the output of the Python expression len([1, 2, 3] * 2)?\na.[1,2,3,1,2,3]\nb.6\nc. 12",
                   "Answer":"b"},
                  ]
#Login_menu
# For Menu means  whole program code, While-Loop is used as user can make countless attempt to log in.
# Try_Except method is applied to restrict code from breaking. user has to choose the right option from options provided
# or else the program will not show advancement.
# if/else conditional statements are used to prompt to right tab as per user choice.
# Whole code is divided into multiple functions to appear composed and manageable.
# Functions-->  questionair()---valid_option(),(to choose the right option from given options to answer quiz questions)---percentage_grading(score)---quiz_grading(score)---result_com(score)
#Loops-- for-loop is used as it iterate through counted questions. While-Loop for login as user can make multiple attempts.

def main_menu():
    print(Fore.BLACK+Back.BLUE+str("------Welcome to the holton's quiz------").title())
    print(str("1.Login and Quiz\n2.Signup\n3.Quit").title())
    while True:
            try:
                choice=int(input("Please enter your choice: "))
                if choice==1:
                    login_quiz()
                    break
                elif choice==2:
                    sign_up(user_database)
                    break
                elif choice==3:
                    break
                else:
                    print("Invalid choice, Enter 1-3")
                    main_menu()
            except ValueError:
                print("Invalid choice, Enter 1-3")
    exit

def login_quiz():
        print("---Login---")
        login_success = False
        while True:
            username = input("Enter your username: ").lower()
            password = input("Enter your password: ").lower()
            for user in user_database:
                if username == user[0] and password == user[1]:
                    print("Login successful!")
                    print(Fore.BLACK+Back.CYAN+"      Hello " + username + "!!!     ")
                    print(Fore.BLACK+Back.CYAN+"=========================")
                    print()
                    time.sleep(1)
                    print(Fore.BLACK+Back.GREEN+str("welcome to the quiz ").title())
                    print(Fore.BLACK+Back.GREEN+str(" Test you knowledge ").title())
                    quiz_questionair()
                else:
                    print("Wrong username or password")
                    login_quiz()
                return login_success






#
# user_database=[]
#
# def valid_signup(username):
#
#     return username.isalpha()
#
# def sign_up():
#     while True:
#         print("---Signup---")
#         username = str(input(f"Enter username:  ")).lower()
#         if not valid_signup(username):
#             print("invalid input.Use only letters, please")
#         else:
#             password = input("make strong password: ").lower()
#             user_database.append([username, password])
#             print("signup successful!!!")
#             main_menu()
#         return





class Grade:
    pass

#
def quiz_questionair():
    score=0
    total_score=30
    count=0

    for i in list(quiz_questions):
            flag2 = input("Do you want to QUIT the quiz at this point (Yes/No)?:").lower()
            if flag2 == 'yes':
                print("You chose to quit the quiz")
                print("Total Score is:", score, "/", total_score)
                break
            print(i["Question"])
            flag1 = input("Do you want to SKIP the question(Yes/No)?: ").lower()
            if flag1 == 'yes':
                continue
            # create function to make sure user answer falls within the valid options range.
            def valid_option():
                valid = "a", "b", "c", "d"
                while True:
                    answer = input(Fore.BLACK+Back.WHITE+"enter the answer(a/b/c/d): ").lower()
                    if answer in valid:
                        return answer
                    else:
                        print("invalid option")
            #====================================================#

            answer = valid_option()
            user_answers.append(answer)
            if answer == quiz_questions[count]["Answer"]:
                print()
                print(Fore.BLACK+Back.GREEN+"correct answer you got +3")
                score += 3
                count += 1
            else:
                print()
                print(Fore.BLACK+Back.RED+"wrong answer")
                count = count + 1
                time.sleep(1)
    print(Fore.BLACK + Back.BLUE +"--the quiz is over--")
    time.sleep(1)
    print(Fore.BLACK + Back.BLUE + "------Results------")
    print()
    time.sleep(1.5)
    print(result_com(score))
    time.sleep(1.5)
    print("your score is:", score,'/', total_score)
    time.sleep(1.5)
    print("percentage:", percentage_grading(score))
    time.sleep(1.5)
    print("Grade:",quiz_grading(score))
    time.sleep(1.5)
    print("User_choices:", user_answers)
    time.sleep(1)
    print("Correct answers:",correct_answers)
    print(Fore.BLACK + Back.CYAN + "---Thank you for taking part in quiz---")
    return  score





def percentage_grading(score):
    percentage=(score/total_score)*100
    return percentage
#
def quiz_grading(score):
    percentage=percentage_grading(score)
    if percentage<40:
        grade="D"
    elif 40<= percentage <60:
        grade="C"
    elif 60<= percentage <70:
        grade="B"
    elif 70<= percentage <80:
        grade="A"
    elif percentage >=80:
        grade="A+"
    return grade
#
def result_com(score):
    grade=quiz_grading(score)
    if grade=='A+':
        com=Fore.BLACK + Back.GREEN + "...Brilliant...!! You did a great job..!!"
    elif grade=='A':
        com=Fore.BLACK + Back.GREEN + "well done..!!!....you have good understanding of python."
    elif grade=='B':
        com=Fore.BLACK + Back.BLUE + "good job.. You have successfully passed...!!"
    elif grade=='C':
        com=Fore.BLACK + Back.YELLOW + "..hmm not BAD..You have passed."
    elif grade=='D':
        com=Fore.BLACK + Back.RED + "...NEVER give up...Better luck next time"
    return com








main_menu()







