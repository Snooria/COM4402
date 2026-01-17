# ---------------------Holton's Quiz Program-----------------------#
from turtledemo.round_dance import stop


count=0
score=0
total_score=4
option=""

print("--------------------Welcome to Holton's Quiz-------------------")
# choice= str(input("options:\nA.Signup\nB.Login\nChoose the option: "))
user_name_password =[
                    ['harry', 'ha123'],
                    ['saima', 'sa123'],
                    ['paige', 'pa123']
    ]
# print("--------------Menu-------------------")
# List is being used to store the data and can be appended by adding new users data who want to sign up for first time.
# data could be stored and retrieve if file handling is implemented which requires few more explanations.
# A new variable users is being created to check user input in list user_name_password if it does exist and match to help user login.
# try-except handling tool is applied to prevent code from crashing.
# else-if conditional statements will prompt to the right tab according to user input.



while True:
    print("1.Login\n2.Signup")

    choice=int(input("Enter your choice: "))
    if choice==1:
        print("---Login---")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in user_name_password:
            if username == user[0] and password == user[1]:
                print("Welcome " + username + "!!")
                print("You are successfully logged in..!!!")
                while True:
                    print(f"------MENU------\n----------------\n1.Quiz\n2.Results\n3.Exit")

                    try:
                        option = int(input("Enter your choice: "))
                    except ValueError:
                        print("please enter valid input")
                    if option == 1:
                        print("Quiz")
                        questions = [{"""2. Which software is used for creating and managing spreadsheets???
a. Microsoft Excel
                        b. Microsoft PowerPoint
                        c. Adobe Illustrator
                        d. Google Drive""": "b"},
                        {"""1.what is name of American president?
                        a. william Harold
                        b. Donald Trump
                        c. George Bush""": "b"}]

                        for i in questions:
                            print("\n".join(i))
                            print()
                            flag1 = input("--Do you want to skip the question(Yes/No)?:").lower()
                            if flag1 == 'yes':
                                continue
                            answer = input("enter the answer(a/b/c/d): ")
                            if answer == questions:
                                print()
                                print("correct answer you got +2")
                                score = score + 2
                                print()
                            else:
                                print()
                                print("wrong answer")
                                print("the right answer is: ", )
                            flag2 = input("--Do you want to quit the quiz(Yes/No)?:").lower()
                            if flag2 == 'yes':
                                break
                        print("Total score is:", score, "/", total_score)



                        # choices = []
                        # score = 0
                        # count_question = 0
                        #
                        # for question in questions:
                        #     print("------------------------------")
                        #     print(question)
                        #     for option in options[count_question]:
                        #         print(option)
                        #     print("")
                        #     choice = input("Choose the right option: ").upper()
                        #     choices.append(choice)
                        #     if choice == answers[count_question]:
                        #         score += 2
                        #         print("correct answer!!")
                        #     else:
                        #         print("wrong answer!!")
                        #         print("")
                        #         print(f"Right answer is: {answers[count_question]}")
                        #     count_question += 1
                        #
                        # print("-----------------------------------")
                        # print("------------RESULTS----------------")
                        # print("-----------------------------------")
                        #
                        # print("Correct Answers: ", end="")
                        # for answer in answers:
                        #     print(answer, end=" ")
                        # print()
                        # print("User Choices: ", end="")
                        # for choice in choices:
                        #     print(choice, end=" ")
                        # print()
                        #
                        # # # TOTALING AND PASS/FAIL CRITERIA ON BASIS OF PERCENTAGES# #
                        # print("Total score:",score, "out of", total)
                        # percentage= (score/total)*100
                        # # print(f"percentage :{percentage:.2f}")
                        # print()


                        ###-------Results----####
                    elif option == 2:
                        print("-----Detailed Results-----")

                        if percentage < 40:
                            print("------Results-----")
                            print(f"user name: {username}")
                            print("Unfortunately, you have to retake the test")
                            print("Results: Grade: D", "", "score:", score, "/", total, "Percentage",
                                  f"{percentage:.2f}")
                        elif (percentage > 40 and percentage < 50):
                            print("------Results-----")
                            print(f"user name: {username}")
                            print("You have passed the test by getting grade C")
                            print("Results: Grade: C", "", "score:", score, "/", total, "Percentage",
                                  f"{percentage:.2f}")
                        elif percentage > 50 and percentage < 70:
                            print("------Results-----")
                            print(f"user name: {username}")
                            print("You have passed the test by getting grade B")
                            print("Results: Grade: B", "", "score:", score, "/", total, "Percentage",
                                  f"{percentage:.2f}")
                        elif percentage > 70 and percentage < 80:
                            print("------Results-----")
                            print(f"user name: {username}")
                            print("Well done! You have passed the test by getting grade A")
                            print("Results: Grade: A", "", "score:", score, "/", total, "Percentage",
                                  f"{percentage:.2f}")
                        elif percentage > 80:
                            print("------Results-----")
                            print(f"user name: {username}")
                            print("Excellent! You have passed the test by getting grade A+")
                            print("Results: Grade: A+", "", "score:", score, "", "Percentage", f"{percentage:.2f}")
                        break




                    elif option == 3:
                        print("Exiting")
                        break

                    else:
                        print("Invalid input")
                break
        else:
            print("Wrong username or password")
    elif choice==2:
        print("---Signup---")
        username = str(input(f"Enter username:  "))
        password = input("make strong password: ")
        user_name_password.append([username, password])
        print("signup successful!")



#--------------------------------#


###########MENU################

#applied try-except handling tool to prevent code from crashing.
# else-if statements will prompt to the right tab according to user input.









