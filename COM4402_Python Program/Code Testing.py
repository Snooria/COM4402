# ---------------------Holton's Quiz Program-----------------------#
from idlelib.mainmenu import menudefs
from turtledemo.round_dance import stop


count=0
score=0
total=6
option=""
username = ""
password = ""
login_success = False

# questions = [
#                 "1. who is the father of computer?",
#                 "2. what is the brain of a computer?",
#                 "3. who are you?"
#             ]
# options = [
#             ["1. Charles Babbage", "2. James Hortons", "3. Bill Gates", "4.Dennis James"],
#             ["1. CPU", "2. RAM", "3.GPU"],
#             ["1. Human", "2. Alien", "3.Animal"]
#         ]
# answers = [1,1,1]

question_Database = [
    {
        "question_text": "text here",
        "quesiton_options": [
            "opA",
            "opB",
            "opC"
            "opD"
        ],
        "correct_op": 2
    },
    {
        "question_text": "text here",
        "quesiton_options": [
            "opA",
            "opB",
            "opC"
            "opD"
        ],
        "correct_op": 2
    },
    {
        "question_text": "text here",
        "quesiton_options": [
            "opA",
            "opB",
            "opC"
            "opD"
        ],
        "correct_op": 2
    }
]

user_input=''
print("--------------------Welcome to Holton's Quiz-------------------")
# choice= str(input("options:\nA.Signup\nB.Login\nChoose the option: "))
user_name_password =[
                    ['harry', 'ha123'],
                    ['saima', 'sa123'],
                    ['paige', 'pa123']
    ]
user_database = [
    { "uname": "harry", "pass": "ha123" },
    { "uname": "saima", "pass": "sa123" },
    { "uname": "paige", "pass": "pa123" },
]

#--------------------------------#
#functions

def quiz_results():
    print("...View detailed Results....")
# print("--------------Menu-------------------")
# List is being used to store the data and can be appended by adding new users data who want to sign up for first time.
# data could be stored and retrieve if file handling is implemented which requires few more explanations.
# A new variable users is being created to check user input in list user_name_password if it does exist and match to help user login.
# try-except handling tool is applied to prevent code from crashing.
# else-if conditional statements will prompt to the right tab according to user input.
def get_valid_input(start, end):
    option = -1
    try:
        while option < start or option > end:
            option = int(input("Enter your choice: "))
    except ValueError:
        print("please enter valid input")
    return option

#
def handle_login(login_success):
    while login_success == False:
        print("1.Login\n2.Signup")

        choice= get_valid_input(1,2)
        if choice==1:
            print("---Login---")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user in user_name_password:
                if username == user[0] and password == user[1]:
                    login_success = True
                    break

            if login_success == False:
                print("Wrong username or password")

        elif choice==2:
            print("---Signup---")
            username = str(input(f"Enter username:  "))
            password = input("make strong password: ")
            user_name_password.append([username, password])
            print("signup successful!")


    return login_success


def handle_main_menu():
    while True:
        print(f"------MENU------\n----------------\n1.Quiz\n2.Results\n3.Exit")

        option = get_valid_input(1, 3)

        if option == 1:
            handle_quiz()

        elif option == 2:
            handle_result_display()

        elif option == 3:
            print("Exiting")
            break

        else:
            print("Invalid input")

def handle_quiz():
    print("Quiz")

    # Quiz Loop
    choices = []
    score = 0
    count_question = 0

    for question in questions:
        print("------------------------------")
        print(question)
        for i in range(len(options[count_question])):
            print(options[count_question][i])
        print("")
        user_choice = int(input("Choose the right option: "))
        choices.append(user_choice)
        if user_choice == answers[count_question]:
            score += 2
            print("correct answer!!")
        else:
            print("wrong answer!!")
            print("")
            print(f"Right answer is: {answers[count_question]}")
        count_question += 1

    print("-----------------------------------")
    print("------------RESULTS----------------")
    print("-----------------------------------")

    print("Correct Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()
    print("User Choices: ", end="")
    for choice in choices:
        print(choice, end=" ")
    print()
    # # TOTALING AND PASS/FAIL CRITERIA ON BASIS OF PERCENTAGES# #
    print("Total score:", score, "out of", total)
    if score >= 4:
        print("Pass!")
    else:
        print("Fail!")
    print()

    # ------- CALL THE FUNCTION TO DISPLAY RESULTS WITH PERCENTAGE###

    while score == 'pass':
        user_input = int(input("Enter 1 if you wish to view detailed results: "))
        if user_input != 1:
            print("Level_2")
    #         print("questions")
        # else:
        #     def quiz_results()

def handle_result_display():
    print("---Detailed Results---")

    percentage = (score / total) * 100
    # print(f"percentage :{percentage:.2f}")
    # print()

    if percentage < 40:
        print("------Results-----")
        print(f"user name: {username}")
        print("Unfortunately, you have to retake the test")
        print("Results: Grade: D", "", "score:", score, "/", total, "Percentage", f"{percentage:.2f}")
    elif (percentage > 40 and percentage < 50):
        print("------Results-----")
        print(f"user name: {username}")
        print("You have passed the test by getting grade C")
        print("Results: Grade: C", "", "score:", score, "/", total, "Percentage", f"{percentage:.2f}")
    elif percentage > 50 and percentage < 70:
        print("------Results-----")
        print(f"user name: {username}")
        print("You have passed the test by getting grade B")
        print("Results: Grade: B", "", "score:", score, "/", total, "Percentage", f"{percentage:.2f}")
    elif percentage > 70 and percentage < 80:
        print("------Results-----")
        print(f"user name: {username}")
        print("Well done! You have passed the test by getting grade A")
        print("Results: Grade: A", "", "score:", score, "/", total, "Percentage", f"{percentage:.2f}")
    elif percentage > 80:
        print("------Results-----")
        print(f"user name: {username}")
        print("Excellent! You have passed the test by getting grade A+")
        print("Results: Grade: A+", "", "score:", score, "", "Percentage", f"{percentage:.2f}")





while True:

    login_success = handle_login(False)

    if login_success:
        handle_main_menu()


#--------------------------------#


###########MENU################

#applied try-except handling tool to prevent code from crashing.
# else-if statements will prompt to the right tab according to user input.


# while True:
#    print(f"------MENU------\n----------------\n1.Quiz\n2.Score\n3.Exit")
#
#    try:
#        option = int(input("Enter your choice: "))
#    except ValueError:
#       print("please enter valid input")
#       continue
#    if option == 1:
#       print("Quiz")
#       break
#    elif option== 2:
#       print("Score")
#       break
#    elif option== 3:
#       print("Exiting")
#       break
#
#    else:
#       print("Invalid input")






