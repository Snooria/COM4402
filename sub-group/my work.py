#variables
from random import choice

count=0
score=0

username=[]
user_answers=[]
total_score=20
correct_answers=['b','b','a','a']
total_questions=1


#list of dictionaries for username and password
# user_database=[{"username":"Harry", "password":"ha123"},
#                {"username":"Maria", "password":"ma123"},
#                {"username":"Harsh", "password":"ha123"},
#                {"username":"Sarah", "password":"sa123"},
#                {"username":"William","password":"wi123"}
#                ]
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

# created login menu and added while-loop as user can make countless tries to login.
#added valid_choice function to make sure user choose the given valid options to log_in or signup.
#Added .lower()  function for user input to make sure code goes smoothly without any difficulty.
#for-loop is used to validate if username and password matches the database to help user login.
#if-else conditions are implied to move user to right tab according to user's choice.
#isalpha() method is being used within valid_signup function to make sure user input is string not integer.
#initially used list of dictionaries but as it does not save sign up user details.
#so changed to list of lists which is easy to store new data input by users.



while True:
        print(str("------Welcome to the holton's quiz------").title())
        print(str("1.Login and Quiz\n2.Signup\n3.Quit").title())
        try:
            choice = int(input("Enter your choice: "))

            if choice==1 and choice==2 and choice==3:
                break
        except ValueError:
            print("please enter valid input")
        if choice == 1:
            print("---Login---")
            username = input("Enter your username: ").lower()
            password = input("Enter your password: ").lower()
            for user in user_database:
                if username == user[0] and password == user[1]:
                    print("Welcome " + username + "!!")
                    print("You are successfully logged in..!!!")
                while True:
                        print(str("----Welcome to the Quiz----").title())
                        print(str("Test you knowledge").title())

                        for i in list(quiz_questions):
                            print()
                            flag2 = input(
                                "                       Do you want to QUIT the quiz at this point (Yes/No)?:").lower()
                            if flag2 == 'yes':
                                print("You chose to quit the quiz")
                                print("Total Score is:", score, "/", total_score)
                                break
                            print(i["Question"])
                            print()
                            flag1 = input("                       Do you want to SKIP the question(Yes/No)?: ").lower()
                            if flag1 == 'yes':
                                continue
                            # create function to make sure user answer falls within the valid options range.
                            def valid_option():
                                valid = {"a", "b", "c", "d"}
                                while True:
                                    answer = input("enter the answer(a/b/c/d): ").lower()
                                    if answer in valid:
                                        return answer
                                    else:
                                        print("invalid option")
                            # ---------------------------------------------#
                            answer = valid_option()
                            user_answers.append(answer)
                            if answer == quiz_questions[count]["Answer"]:
                                print()
                                print("correct answer you got +2")
                                score += 3
                                count += 1
                                print()
                            else:
                                print()
                                print("wrong answer")
                                count = count + 1
                                total_questions += 1
                                for i in list(quiz_questions):
                                    if i==10:
                                        print("quiz is over")
                                        print("====================================")
                                        print("user choice:", user_answers)
                                        print("====================================")
                                        print("correct answers are:", correct_answers)
                                        print("====================================")
                                        print()
                                        print("---Thank you for testing your knowledge---")
                                        print("-----------see you next time--------------")
                                        print()
                                    break
            else:
                print("Wrong username or password")
        elif choice == 2:
                    print("---Signup---")
                    def valid_signup(username):
                        return username.isalpha()
                    while True:
                        username = str(input(f"Enter username:  ")).lower()
                        if not valid_signup(username):
                            print("invalid input.Use only letters, please")
                        else:
                            password = input("make strong password: ")
                            user_database.append([username, password])
                        print("signup successful!!!")
                        break
        elif choice == 3:
            print("---Exiting---")
            print("Thank you for testing your knowledge")




###=================================##############
# while quiz_questions == 10:
#     print("---Quiz is Over---")
#     if score >= 10:
#         print("Pass!")
#     else:
#         print("Fail!")
#         percentage = (score / total_score) * 100
#         print("============Quiz is over===========")
#         print("-----------Final Results-----------")
#         print("===================================")
#         print("You scored:", score, "/", total_score)
#         if score >= 10:
#             print("Congratulations, you have Passed the quiz..!!")
#         else:
#             print("Fail....You need more practice.")
#             if percentage < 40:
#                 print("------Results-----")
#                 print(f"user name: {username}")
#                 print("Unfortunately, you have to retake the test")
#                 print("Results: Grade: D", "", "score:", score, "/", total_score, "Percentage",
#                       f"{percentage:.2f}")
#             elif (percentage > 40 and percentage < 50):
#                 print("------Results-----")
#                 print(f"user name: {username}")
#                 print("You have passed the test by getting grade C")
#                 print("Results: Grade: C", "", "score:", score, "/", total_score, "Percentage",
#                       f"{percentage:.2f}")
#             elif percentage > 50 and percentage < 70:
#                 print("------Results-----")
#                 print(f"user name: {username}")
#                 print("You have passed the test by getting grade B")
#                 print("Results: Grade: B", "", "score:", score, "/", total_score, "Percentage",
#                       f"{percentage:.2f}")
#             elif percentage > 70 and percentage < 80:
#                 print("------Results-----")
#                 print(f"user name: {username}")
#                 print("Well done! You have passed the test by getting grade A")
#                 print("Results: Grade: A", "", "score:", score, "/", total_score, "Percentage",
#                       f"{percentage:.2f}")
#             elif percentage > 80:
#                 print("------Results-----")
#                 print(f"user name: {username}")
#                 print("Excellent! You have passed the test by getting grade A+")
#                 print("Results: Grade: A+", "", "score:", score, "", "Percentage",
#                       f"{percentage:.2f}")



