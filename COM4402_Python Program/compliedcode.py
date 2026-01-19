import time
from random import choice

from click.exceptions import Exit
from colorama import Fore, Back, init

init(autoreset=True)

count=0



user_answers=[]
total_score=30
correct_answers=['b','b','a','a']


user_database=[['harry','ha123'],['william','wi123'],
               ['maria', 'ma123'],['sarah','sa123'],
                ['alina','al123'],['bushra','bu123']]
#Question database. #List of dictionaries being used because it offers us key and value features.

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
# print(str("------Welcome to the holton's quiz------").title())

def main_menu():
    print(str("1.Login and Quiz\n2.Signup\n3.Quit").title())
    while True:
            try:
                choice=int(input("Please enter your choice: "))
                if choice==1:
                    login_quiz()
                    break
                elif choice==2:
                    sign_up()
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
                    print(Fore.BLACK+Back.CYAN+"Hello " + username + "!!!")
                    print()
                    time.sleep(1)
                    print(Fore.BLACK+Back.GREEN+str("welcome to the quiz").title())
                    print(str("Test you knowledge").title())
                    quiz_questionair()
                    return None
                else:
                    print("Wrong username or password")
                    login_quiz()
                return login_success






def sign_up():
    print("bye")



def quiz_questionair():
    count = 0
    score=0

    for i in list(quiz_questions):
        print()
        flag2 = input("Do you want to QUIT the quiz at this point (Yes/No)?:").lower()
        if flag2 == 'yes':
            print("You chose to quit the quiz")
            print("Total Score is:", score, "/", total_score)
            break
        print(i["Question"])
        print()
        flag1 = input("Do you want to SKIP the question(Yes/No)?: ").lower()
        if flag1 == 'yes':
            continue

        # create function to make sure user answer falls within the valid options range.
        def valid_option():
            valid = {"a", "b", "c", "d"}
            while True:
                answer = input(Fore.BLACK+Back.WHITE+"enter the answer(a/b/c/d): ").lower()
                if answer in valid:
                    return answer
                else:
                    print("invalid option")

        answer = valid_option()
        user_answers.append(answer)
        if answer == quiz_questions[count]["Answer"]:
            print()
            print(Fore.BLACK+Back.GREEN+"correct answer you got +2")
            score += 3
            count += 1
            print()
        else:
            print()
            print(Fore.BLACK+Back.RED+"wrong answer")
            count = count + 1
            for i in list(quiz_questions):
                if i == len(quiz_questions):

                    print(Fore.BLACK + Back.BLUE + "the quiz is over")






main_menu()


