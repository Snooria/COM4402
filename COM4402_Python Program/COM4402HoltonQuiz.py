import time
from random import choice

from click.exceptions import Exit
from colorama import Fore, Back, init
from numpy.ma.core import maximum

init(autoreset=True)

#Login_menu
# For Menu means  whole program code, While-Loop is used as user can make countless attempt to log in.
# Try_Except method is applied to restrict code from breaking. user has to choose the right option from options provided
# or else the program will not show advancement.
# List is being used to store the data and can be appended by adding new users data who want to sign up for first time.
# data could be stored and retrieve if file handling is implemented which requires few more explanations.
# if/else conditional statements are used to prompt to right tab as per user choice.
# A new variable users is being created to check user input in list user_name_password if it does exist and match to help user login.
# try-except handling tool is applied to prevent code from crashing.
# Whole code is divided into multiple functions to appear composed and manageable.
# Functions-->  questionnaire()---valid_option(),(to choose the right option from given options to answer quiz questions)---percentage_grading(score)---quiz_grading(score)---result_com(score)
#Loops-- for-loop is used as it iterate through counted questions. While-Loop for login as user can make multiple attempts.

count=0
score=0
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
# Functions-->  questionnaire()---valid_option(),(to choose the right option from given options to answer quiz questions)---percentage_grading(score)---quiz_grading(score)---result_com(score)
#Loops-- for-loop is used as it iterate through counted questions. While-Loop for login as user can make multiple attempts.

def main_menu():
    print(Fore.BLACK+Back.CYAN+str("------Welcome to the holton's quiz------").title())
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
                    print(Fore.BLACK+Back.CYAN+"Thank you for using Holton's Quiz Application  :) ")
                    exit
                    break
                else:
                    print("Invalid choice, Enter 1-3")

            except ValueError:
                print("Invalid choice, Enter 1-3")
    exit

def login_quiz():
    print("---Login---")
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
                print("....Each question carries 2 scores....")
                quiz_questionnaire()
                return
        else:
            print("Wrong username or password")




def sign_up(user_database):
    while True:
        print("---Signup---")
        username = str(input(f"Enter username:  ")).lower()
        if not username.isalpha():
            print("username has to be letters only")
        else:
            password = input("Make strong password: ").lower()
            user_database.append([username, password])

            print()
            print(Fore.BLACK + Back.CYAN + "      Hello " + username + "...!!!  You have successfully signed up!!!!!     ")
            print()
            time.sleep(1)
            print(Fore.BLACK + Back.GREEN + str("welcome to the quiz ").title())
            print(Fore.BLACK + Back.GREEN + str(" Test you knowledge ").title())
            print("....Each question carries 2 scores....")
            quiz_questionnaire()
            return


class Grade:
    pass


def valid_option():
        valid = "a", "b", "c", "d"
        while True:
            answer = input(Fore.BLACK + Back.WHITE + "Choose the answer(a/b/c/d): ").lower()
            if answer in valid:
                return answer
            else:
                print("invalid option")


def quiz_questionnaire():
    score=0
    count =0
    while True:
        selection = input("A.5 Qs\nB.10 Qs\nMake choice: ").lower()
        try:
            if selection == "b":
                max_question = len(quiz_questions)
                total_score = 20
                break
            elif selection == "a":
                max_question = len(quiz_questions) / 2
                total_score = 10
                break
            else:
                print("invalid choice")
        except ValueError:
            return


    for i in list(quiz_questions):
        if count == max_question:
            break


        print(i["Question"])
        answer = valid_option()
        user_answers.append(answer)


        if answer == quiz_questions[count]["Answer"]:
            print()
            print(Fore.BLACK+Back.GREEN+"correct answer you got +2")
            score += 2
        else:
            print()
            print(Fore.BLACK+Back.RED+"wrong answer")

        count +=1
        time.sleep(1)
    print(Fore.BLACK + Back.BLUE +"----Quiz is over----")
    time.sleep(1)
    print(Fore.BLACK + Back.BLUE + "------Results------")
    print()
    time.sleep(1.5)
    print(result_com(score,total_score))
    time.sleep(1.5)
    print("your score is:", score,'/', total_score)
    time.sleep(1.5)
    print("percentage:", percentage_grading(score,total_score))
    time.sleep(1.5)
    print("Grade:",quiz_grading(score,total_score))
    time.sleep(1.5)

    print(Fore.BLACK + Back.CYAN + "---Thank you for taking part in quiz---")
    back_menu()
    main_menu()
    return  score

def back_menu():
    print("Press any key to get back to main menu.... :) ")
    time.sleep(1.5)
    input()
    return




def percentage_grading(score,total_score):
    percentage=(score/total_score)*100
    return percentage
#
def quiz_grading(score,total_score):
    percentage=percentage_grading(score,total_score)
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
def result_com(score,total_score):
    grade=quiz_grading(score,total_score)
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








