# from colorama import Fore, Back, Style, init
# from torchgen.api.cpp import return_type
#
# init(autoreset=True)
# # print(Fore.RED+"this text is red")
# # print(Back.GREEN+"this text is green")
# # print(Style.RESET_ALL)
#
#
# import time
# # for i in range(0,5):
# #   print(i)
# #   time.sleep(1)
#
# # import turtle
# #
# # t=turtle.Turtle()
# #for i in range(0,5):
# #   print(i)
# #   time.sleep(1)
# #
# # #using basic colors
# # t.color("red")
# # t.begin_fill()
# # t.circle(30)
# # t.end_fill()
# #
# # # Move to a new position
# # t.penup()
# # t.goto(100, 0)
# # t.pendown()
# #
# # # Try another color
# # t.color("blue")
# # t.begin_fill()
# # t.circle(50)
# # t.end_fill()
# #
# # # Create screen and set background color
# # # screen = turtle.Screen()
# # # screen.bgcolor("lightblue")  # Using a named color
# # #
# # # t = turtle.Turtle()
# # # t.color("navy")
# # # t.begin_fill()
# # # t.circle(50)
# # # t.end_fill()
# # #
# # # turtle.done()
#
#
#
#
#
# # # #Dictionary
# # prices={"coffee": "£10.50",
# #        "latte": "07.50",
# #        "water": "01.00"
# # }
# #
# # item= input("enter item name: ")
# #
# # #if loop to check the availability of certain item data within the dictionary.
# #
# # if item in prices:
# #     print(f"The price of {item} is:" ,prices[item])
# # else:
# #     print("unknown item")
# import grades
#
# # def sq(n):
# #     print(f"Square of {n} is {n*n}")
# #     return n * n
# #
# # def add(a, b):
# #     return a+b
# #
# # def sub(a,b):
# #     return a - b
#
# #
# # while True:
# #     print(f"Please choose operation:\n"
# #           f"1. Add\n"
# #           f"2. Sub\n"
# #           f"0. Exit")
# #
# #     choice = input()
# #
# #     a = int(input("Enter A: "))
# #     b = int(input("Enter B: "))
# #
# #     if choice == "1":
# #         result = add(a, b)
# #         print(f"Result: {result}")
# #
# #     elif choice == "2":
# #         result = sub(a, b)
# #         print(f"Result: {result}")
# #
# #     elif choice == "0":
# #         print("EXIT chosen")
# #         break
#
#
# # print(sq(5))
#
# # create function to do something . print some value.
# #create function to get the value for u
# #create function to do get input from user and get into function , do the calculations and get back to you and display the output.
# #means return back to you.
#
#
# total_score=30
#
# def percentage_grading(score,total_score):
#     percentage=(score/total_score)*100
#     return percentage
#
#
#
# score=float(input("enter your score: "))
# # percentage=percentage_grading(score,total_score)
# # print(f"percentage is: {percentage:.2f}%")
#
# def quiz_grading(score,total_score):
#     percentage=percentage_grading(score,total_score)
#     if percentage<40:
#         grades="D"
#     elif 40<= percentage <60:
#         grades="C"
#     elif 60<= percentage <70:
#         grades="B"
#     elif 70<= percentage <80:
#         grades="A"
#     elif percentage >80:
#         grades="A+"
#     return grades
#
#
# def grade_message(Grade):
#
#     if Grade == "A+":
#         com= Fore.BLACK + Back.GREEN +"Brilliant.. You did a great job..!!"
#     elif Grade == "A":
#         com= Fore.BLACK + Back.GREEN + "Great....You have passed...!!"
#     elif Grade == "B":
#         com= Fore.BLACK + Back.BLUE + "Good..You have successfully passed...!!"
#     elif Grade=="C":
#          com= Fore.BLACK + Back.YELLOW + "You have passed...!!"
#     elif Grade=="D":
#           com= Fore.BLACK + Back.RED + "Failed...!!"
#     return com
#
#
#
#
#
# percentage = percentage_grading(score, total_score)
# score = float(input("enter your score: "))
# def detailed_results(total_score):
#     Per = percentage_grading(score, total_score)
#     Grade=quiz_grading(score,total_score)
#     comment = grade_message(Grade)
#
#     time.sleep(1.5)
#     print(Fore.BLACK+Back.BLUE+"------Results------")
#     print()
#     time.sleep(1.5)
#     print(comment)
#     time.sleep(1.5)
#     print()
#     print(f"your score is:",score,"/",total_score)
#     time.sleep(1.5)
#     print(f"percentage is: {Per:.2f}%")
#     time.sleep(1.5)
#     print("your grade is:", Grade)
#     print(Fore.BLACK+Back.CYAN+"---Thank you for taking part in quiz---")
#     return Per, Grade,comment
#
#
# detailed_results(total_score)
#
#
#
# while True:
#     user_choice = input("Do you want to continue? (y/n): ")
#     if user_choice.lower() == 'y':
#         print("Continuing...")
#         break
#     elif user_choice.lower() == 'n':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid input. Please enter 'y' or 'n'.")
#
# # in case of quitting, total score will be different . rest of functions will be called as it is.
# # total_score=number of questions attempted.
# # counter needs to be fixed or just prompt user to decide whether she wants to quit or not.
# total_score=''
# quiz_questions=''
#
# while True:
#     user_choice = input("Do you want to quit after attempting half or test or want to continue till end? (q/c): ")
#     if user_choice.lower() == 'c':
#         total_score=len(quiz_questions)
#     elif user_choice.lower() == 'q':
#         total_score=len(quiz_questions)/2
#         break
#     else:
#         print("Invalid input. Please enter 'y' or 'n'.")
#
#     # flag2 = input("Do you want to QUIT the quiz at this point (Yes/No)?:").lower()
#     # if flag2 == 'y':
#     #     print("You chose to quit the quiz")
#     #     print("Total Score is:", score, "/", total_score)
#     #     break
# # print(i["Question"])
# # flag1 = input("Do you want to SKIP the question(Yes/No)?: ").lower()
# # if flag1 == 'yes':
# #     continue
# # create function to make sure user answer falls within the valid options range.
#
#
# # total_score = len(quiz_questions)
#
#
# def get_user_choice():
#     while True:
#         user_choice = input("Do you want to proceed? (y/n): ")
#         if user_choice.lower() == 'y':
#             return True
#         elif user_choice.lower() == 'n':
#             return False
#         else:
#             print("Invalid input. Please enter 'y' or 'n'.")
#
#
# if get_user_choice():
#     print("Proceeding with the operation...")
# else:
#     print("Canceling the operation...")
#
#
#     # print("User_choices:", user_answers)
#     # time.sleep(1)
#     # print("Correct answers:",correct_answers)
# def skip_questions(skip_count):
#     while True:
#         skip = input("do you want to skip this question?(y/n): ").lower()
#         if skip == "y":
#             skip_count += 1
#             print("question skipped, count=+1")
#             break
#         elif skip == "n":
#              return
#         else:
#             print("invalid option")
#     return skip_count

###=======================================================================################
#################=======================================================##############################
#####################################=============================================##############################


import time
from random import choice

from colorama import Fore, Back, init

init(autoreset=True)

count = 0

score = 0
total_score = 30
user_answers = []
correct_answers = ['b', 'b', 'a', 'a', 'a', 'c', 'b', 'b', 'c', 'b']
username = ''
password = ''

# Question database. #List of dictionaries being used because it offers us key and value features suitable for quiz questions and right answer.
# List offer 0 , 1 item indexing which we need for quiz questions and correct answers.

# user_database. list of lists is used as it CRUD operations can easily be implemented. List is mutable.
# list maintain order.

user_database = [['harry', 'ha123'], ['william', 'wi123'],
                 ['maria', 'ma123'], ['sarah', 'sa123'],
                 ['alina', 'al123'], ['bushra', 'bu123']]

quiz_questions = [{
                      "Question": "1. Which of the following methods can be used to remove an item from a list?\nA. delete()\nB. remove()\nc. update",
                      "Answer": "b"},
                  {
                      "Question": "2.Which of the following is used to handle multiple exceptions in Python?\na.  except Exception1, Exception2\nb. except (Exception1, Exception2):\nc. except: Exception1, Exception2",
                      "Answer": "b"},
                  {"Question": "3.Which of the following is a Python built-in data type?\na.List\nb.Array\nc.Hash",
                   "Answer": "a"},
                  {
                      "Question": "4.  How do you create a function in Python that takes two parameters?\na.def function(param1, param2): \nb.function(param1, param2): \nc.function: param1, param2 ",
                      "Answer": "a"},
                  {"Question": "5. What is the correct file extension for Python files?\na. .py\nb. .python\nc. .pt",
                   "Answer": "a"},
                  {
                      "Question": "6. What does the `lambda` keyword define in Python?\na.A loop\nb.A class\nc.An anonymous function",
                      "Answer": "c"},
                  {
                      "Question": "7.  What will `lst=[1,2,3]; lst.pop(); print(lst)` output?\na.[1,2,3]\nb.[2,3]\nc.Error",
                      "Answer": "b"},
                  {
                      "Question": "8.  What is the correct way to start a Python script on Unix?\na.#!/usr/bin/python\nb.#!/usr/bin/env python\nc.start python",
                      "Answer": "b"},
                  {
                      "Question": "9.  Which of the following functions can help us to find the version of python that we are currently working on?\na. sys.version(1)\nb.sys.version()\nc.sys.version",
                      "Answer": "c"},
                  {
                      "Question": "10.  What is the output of the Python expression len([1, 2, 3] * 2)?\na.[1,2,3,1,2,3]\nb.6\nc. 12",
                      "Answer": "b"},
                  ]


# Login_menu
# For Menu means  whole program code, While-Loop is used as user can make countless attempt to log in.
# Try_Except method is applied to restrict code from breaking. user has to choose the right option from options provided
# or else the program will not show advancement.
# if/else conditional statements are used to prompt to right tab as per user choice.
# Whole code is divided into multiple functions to appear composed and manageable.
# Functions-->  questionair()---valid_option(),(to choose the right option from given options to answer quiz questions)---percentage_grading(score)---quiz_grading(score)---result_com(score)
# Loops-- for-loop is used as it iterate through counted questions. While-Loop for login as user can make multiple attempts.

def main_menu():
    print(Fore.BLACK + Back.BLUE + str("------Welcome to the holton's quiz------").title())
    print(str("1.Login and Quiz\n2.Signup\n3.Quit").title())
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                login_quiz()
                break
            elif choice == 2:
                sign_up(user_database)
                break
            elif choice == 3:
                break
            else:
                print("Invalid choice, Enter 1-3")
                # main_menu()
        except ValueError:
            print("Invalid choice, Enter 1-3")
    exit


def login_quiz():
    print("---Login---")
    # login_success = False
    while True:
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ").lower()

        for user in user_database:
            if username == user[0] and password == user[1]:
                print("Login successful!")
                print(Fore.BLACK + Back.CYAN + "      Hello " + username + "!!!     ")
                print(Fore.BLACK + Back.CYAN + "=========================")
                print()
                time.sleep(1)
                print(Fore.BLACK + Back.GREEN + str("welcome to the quiz ").title())
                print(Fore.BLACK + Back.GREEN + str(" Test you knowledge ").title())
                print("....Each question carries 2 scores....")
                quiz_questionair()
                return
        else:
            print("Wrong username or password")


def valid_signup(username):
    return username.isalpha()


def sign_up(user_database):
    while True:
            print("---Signup---")
            username = str(input(f"Enter username:  ")).lower()

            if not valid_signup(username):
                print("invalid input.Use only letters, please")
                return
            for user in user_database:
                if user[0] == username:
                    print("Username already exists.")
                    return
                password = input("make strong password: ").lower()
                user_database.append([username, password])
                print("signup successful!!!")
                quiz_questionair()
            return


class Grade:
    pass

def valid_option():
    valid = "a", "b", "c", "d"
    while True:
        answer = input(Fore.BLACK + Back.WHITE + "enter the answer(a/b/c/d): ").lower()
        if answer in valid:
            return answer
        else:
            print("invalid option")



def quiz_questionair():
    score = 0
    count = 0
    skip_count=0
    max_questions = 10
    while True:
        selection = input("choices\nA.5 Qs\nB.10 Qs\nMake choice: ").lower()
        if selection == "a":
            max_questions = 5
            total_score = (max_questions - skip_count) * 2
            break
        elif choice == "b":
            max_questions = 10
            total_score = (max_questions - skip_count) * 2
            break
        else:
            print("Invalid choice")

            for i in list([quiz_questions]):
                if count == max_questions:
                    break
        print(i[quiz_questions])
        while True:
                skip = input("do you want to skip this question?(y/n): ").lower()
                if skip == "y":
                    skip_count += 1
                    print("question skipped, count=+1")
                    break
                elif skip == "n":
                    answer = valid_option()
                    user_answers.append(answer)
                    if answer == quiz_questions[count]["Answer"]:
                        print()
                        print(Fore.BLACK + Back.GREEN + "correct answer you got +2")
                        score += 2
                    else:
                            print()
                            print(Fore.BLACK + Back.RED + "wrong answer")
                            count += 1
                else:
                    print("invalid option")


        total_score = (max_questions - skip_count) * 2
        print(Fore.BLACK + Back.BLUE + "--the quiz is over--")
        time.sleep(1)
        print(Fore.BLACK + Back.BLUE + "------Results------")
        print()
        time.sleep(1.5)
        print(result_com(score, total_score))
        time.sleep(1.5)
        print("your score is:", score, '/', total_score)
        time.sleep(1.5)
        print("percentage:", percentage_grading(score, total_score))
        time.sleep(1.5)
        print("Grade:", quiz_grading(score, total_score))
        time.sleep(1.5)

        print(Fore.BLACK + Back.CYAN + "---Thank you for taking part in quiz---")
        return score


def percentage_grading(score, total_score):
    percentage = (score / total_score) * 100
    return percentage



def quiz_grading(score, total_score):
    percentage = percentage_grading(score, total_score)
    if percentage < 40:
        grade = "D"
    elif 40 <= percentage < 60:
        grade = "C"
    elif 60 <= percentage < 70:
        grade = "B"
    elif 70 <= percentage < 80:
        grade = "A"
    elif percentage >= 80:
        grade = "A+"
    return grade


#
def result_com(score, total_score):
    grade = quiz_grading(score, total_score)
    if grade == 'A+':
        com = Fore.BLACK + Back.GREEN + "...Brilliant...!! You did a great job..!!"
    elif grade == 'A':
        com = Fore.BLACK + Back.GREEN + "well done..!!!....you have good understanding of python."
    elif grade == 'B':
        com = Fore.BLACK + Back.BLUE + "good job.. You have successfully passed...!!"
    elif grade == 'C':
        com = Fore.BLACK + Back.YELLOW + "..hmm not BAD..You have passed."
    elif grade == 'D':
        com = Fore.BLACK + Back.RED + "...NEVER give up...Better luck next time"
    return com


main_menu()




# def get_valid_input(start, end):
#     option = -1
#     try:
#         while option < start or option > end:
#             option = int(input("Enter your choice: "))
#     except ValueError:
#         print("please enter valid input")
#     return option
#
#
# option = get_valid_input(1, 3)
#
# option = get_valid_input(1, 2)
#
# option = get_valid_input(1, 4)







