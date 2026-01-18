#variables
from random import choice

count=0
score=0
username=[]
user_answers=[]
total_score=8
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
quiz_questions = [{"Question":"1. Which software is used for creating and managing spreadsheets?\na. Microsoft Excel\nb. Microsoft PowerPoint\nc. Adobe Illustrator",
                   "Answer": "b"},
                  {"Question":"2.what is name of American president?\na. william Harold\nb. Donald Trump\nc. George Bush",
                   "Answer": "b"},
                  {"Question":"3.what is capital of UK?\na.london\nb.bolton\nc.brighton",
                   "Answer":"a"},
                  {"Question":"4. what is cupid known for?\na.love \nb.hatred \nc.warrior ",
                   "Answer":"a"},
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
                                score += 2
                                count += 1
                                print()
                            else:
                                print()
                                print("wrong answer")
                                # print(f"Correct answer is:",quiz_questions["Answer"])
                                count = count + 1

                        total_questions += 1
                        print("============Quiz is over===========")
                        print("-----------Final Results-----------")
                        print("===================================")
                        print("===================================")
                        print("You scored:", score, "/", total_score)
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
            break






