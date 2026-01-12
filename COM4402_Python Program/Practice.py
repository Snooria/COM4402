#print("Hello World")
import statistics
from importlib.metadata import pass_none

from turtledemo.round_dance import stop

#print("whats your name?:  ")
#name = input()
#print("Hello", name)

# 1.  # arithmatic operations
# increment + , - , * , / , %
#friends=1
#friends += 3
#print(friends)

# increment + , - , * , /
# friends =3
# friends -= 2
# print(friends)

# friends =3
# friends **= 2
# print(friends)

# friends =10
# friends /= 2
# print(friends)

# friends =3
# friends **= 2
# print(friends)

# friends =11
# remainder = friends % 2
# print(remainder)
#.............................................
#.............................................

# 2. # IF Statements
# IF = do some code if some condition is true.
# ELSE do something else

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("you can sign up")
# elif age<5:
#     print("you are infant to sign up for this program")
# else:
#     print("you have to 18+ to sign up")

#..............................................
#..............................................

# Dictionary  = (key:value}
# name = input("What is your name? ")
# studentID = {"Amir" : "am11",
#              "syeda" : "sy12",
#              "nazho" : "naz13"}
# get something from dictionary
# print(studentID.get("mehreen"))

# if name in studentID:
#     print(studentID[name])
# else:
#     print("that name does not exist in the database")

# update the existing key value or add new one
# studentID.update({"Hanan": "han12"})
# print(studentID)

#........................................
#........................................

# questions_index = ["who made first apple phone?: ",
#                     "whats the color of sky?: ",
#                     "name the capital of united kingdom?: ",
#                    "what are two colors we find inside egg?: "]
# options = [["a.william ", "b.drake ", "c.harry "],
#             ["a.blue", "b.red ", "c.blue "],
#             ["a.brighton ", "b.wales ", "c.london"],
#             ["a. red and blue ", "b. yellow and white ", "c.green only "]]
#
# answer = ["a", 'a', "c", "b"]
# guesses= []
# question_num = 0
#score=0
#-----------------------------
# for question in questions_index:
#     print("...................")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter (a,b,c,d): ")
#     guesses.append(guess)
#     if guess == answer[question_num]:
#         print("Correct!")
#     else :
#         print("Wrong!")
#         print(f"{answer[question_num]} is the correct answer!")
#     question_num +=1
#
#
# print("----------------------------")
# print("            RESULTS         ")
# print("----------------------------")
#
# print("answer: ", " ".join(answer))
#
# print("guesses: ", " ".join(guesses))


# for i in range(5):
#     number = int(input("Enter a number: "))
#     print("You entered:", number)

#----------------------------------#
#-----------------------------------#

#WHILE loop
# Conditional loop based on condition.
# it will keep looping unless until the condition turns false.
# if true, loop will keep continuing.
# never forget to put count condition within WHILE Loop.
#while loop → “check condition first”
#do-while style → “run once, then check with while”
# x=0
# while x<=3:
#     print(x)
#     x=x+1

###----------------------------------###

# menu

# choice=""

# while choice!=0:
#     print("1. Login to Holton's Quiz")
#     print("2. signup to Holton's Quiz")
#     print("0. Exit")
#
#     choice = input("Please enter your choice: ")
#
#     if choice=="1":
#         username = str(input("Please enter your username: "))
#         password = str(input("Please enter your password: "))
#     elif choice=="2":
#         username = str(input("Please enter username to sign up: "))
#         password = str(input("Please enter some strong password: "))
#     elif choice=="0":
#         print("existing")
#     else:
#         print("invalid input")

####---------------------------####
# DO-WHILE LOOP
##do-while style → “run once, then check with while”
# DO
#  do something
# WHILE condition
## after running once, it checks the condition.
        # if num is greater than 0, so checks if its positive num or neative.
        # if negative then print the message and keep looping
        #else print the positive number and quit.


 #  PRACTICE
# while True:
#     num=int(input("enter the number: "))
#     if num>0:
#         break
#
#     print("that number is not positive.")
# print("you have entered number:", num)
# stop()

####--------------------------------------------#####

# correct = "apple123"
#
# while True:
#     password=str(input("Please enter your password: "))
#     if password == correct:
#         print("access granted")
#         break
#         stop()
#     else:
#         print("wrong password")



# correct_password = "python123"
#
# while True:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Access granted")
#         break
#     else:
#         print("Wrong password, try again")



# Summing Until 0 (Sentinel Loop)
# Activity 3 – Average Until 0
#Keep asking for marks (0–100)
# 0 means “stop”
# At the end, print:
# how many marks
# the average mark

# count=0
# num= []
# total=0
#
# while True:
#     num=int(input("Enter a number: "))
#
#     if num!=0:
#         count = count + 1
#
#     else:
#         stop()
#         break
#     total += num
# print(f"total: {total}")
# print(f"average: {total/count}")

##-----------------------------##

#Activity 4 – Convert for to while

# for i in range(3):
#     name = input("enter name: ")
#     print("Hello", name)

#-----------------------for loop-----------------#
# count=0
# names=[]
# while True:
#     if count!=3:
#         name=str(input("enter name: "))
#         names.append(name)
#         count=count+1
#     else:
#         break
# print(f"names stored in database:", names)
#-------------------------------------------------#
#-------------------------------------------------#
#-------------------------------------------------#

# Mini Design Task – Simple Login Menu
#Design a program that:

# Shows a menu:
# 1. Login
# 0. Exit
# If user chooses 1:
# Ask for username and password
# Check them against stored values
# Say success or failure
# Menu repeats until user chooses 0
# Use a while loop around the menu.
#
# Stretch:
# Use a do-while style pattern for the login attempts.

# user_name_password ={'harry': 'ha123',
#                      'saima': 'sa236',
#                      'paige': 'pa123'}
#
# print("--------------Menu-------------------")
#
# while True:
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         print("Login")
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if username in user_name_password and password == user_name_password[username]:
#             print("Welcome " + username + "!")
#             print("login successful")
#             break
#         else:
#             print("Wrong username or password")
#     elif choice==2:
#         print("Exit")
#     print("thanks")

##-------------------------------------##
##------------------------------------##
##-----------------------------------##

## nested loops ###

# Single for Loops
# names = ["Aisha", "Bilal", "Chen"]
# for name in names:
#     print("Hello", name)


# A nested loop is:
# A loop inside another loop.
# Analogy:
# Outer loop = rows in a grid
# Inner loop = columns in each row
# For each row, we run through all columns

# for i in range(4):
#     for j in range(3):
#         print("*", end="")
#     print()

#  Right-Angled Triangle of Stars

# rows = 5
# for i in range(1, rows+1):
#     for j in range(i):
#         print("*", end="")
#     print()
####-----------------------######
####-----------------------######

# rows=5
#
# for i in range(1, rows+1):
#     for j in range(i):
#         print(i,end="")
#     print()

####-----------------####
####-----------------####

#
# user_name_password =[
#                     ['harry', 'ha123'],
#                     ['saima', 'sa123'],
#                     ['paige', 'pa123']
#     ]
#
#
#
#
# print("--------------Menu-------------------")
#
# while True:
#     print("1.Login\n2.Exit")
#
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         print("---Login---")
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         for user in user_name_password:
#             if username == user[0] and password == user[1]:
#                 print("Welcome " + username + "!!")
#                 print("login successful")
#                 break
#         else:
#             print("Wrong username or password")
#
#     elif choice==2:
#         print("---Signup---")
#         username = str(input(f"Enter username:  "))
#         password = input("make strong password: ")
#         user_name_password.append([username, password])
#         print("signup successful!")
#
#     print("thanks")

####--------------------------###
# file creation to store user input data.
# user_data=[ ['syeda' , 'sy123'],
#             ['bushra', 'bu123'],
#             ]
# f=open("user_data.txt","w")
#
#
# username = str(input(f"Enter username:  "))
# user_data.append(username)
# password = input("make strong password: ")
# user_data.append(password)
# with open("user_data.txt","a") as f:
#     f.write(f"{username},{password}\n")
# print("sign up successfully stored")
#
# f.close()

####
# file handling in python ; r,w,a, x create.
# user_name_password =[
#                     ['harry', 'ha123'],
#                     ['saima', 'sa123'],
#                     ['paige', 'pa123']
#                     ]
#
# with open('user_data.txt', 'r') as f:
#
#         while True:
#             print("1.Login\n2.Signup")
#
#             choice=int(input("Enter your choice: "))
#             if choice==1:
#                 print("---Login---")
#                 username = input("Enter your username: ")
#                 password = input("Enter your password: ")
#                 for user in user_name_password:
#                     if username == user[0] and password == user[1]:
#                         print("Welcome " + username + "!!")
#                         print("login successful")
#                         break
#                 else:
#                     print("Wrong username or password")
#
#             elif choice == 2:
#                 with open('user_data.txt', 'a') as f:
#                     print("---Signup---")
#                     username = str(input(f"Enter username:  "))
#                     password = input("make strong password: ")
#                     user_name_password.append([username, password])
#                     f.write(f"{username},{password}\n")
#                     print("signup successful!")
#
#             print("thanks")
########-----------------------------------------------------------###############


# menu with choices

# while True:
#     choice = int(input(f"     MENU     \n1.Quiz\n2.Score\n3.Exit\nMake a choice: "))
#     if choice== 1:
#         print("Quiz")
#         break
#     elif choice== 2:
#         print("Score")
#         break
#     elif choice== 3:
#         print("Exiting")
#         break
#     else:
#         print("Invalid input")

# while True:
#     choice = int(input("     MENU     \n1.Quiz\n2.Score\n3.Exit\nMake a choice: "))
#     try:
#         choice = int(choice)
#         break
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#
#         if choice == 1:
#                 print("Quiz")
#                 break
#         elif choice== 2:
#                 print("Score")
#                 break
#         elif choice== 3:
#                 print("Exiting")
#                 break
#         else:
#                 print("Invalid input")

###------------------------##
##-------------------------##
                #############
                # menu done #
                #############
# while True:
#    print(f"     MENU     \n1.Quiz\n2.Score\n3.Exit")
#
#    try:
#       choice = int(input("Enter your choice:"))
#    except ValueError:
#       print("please enter valid input")
#       continue
#    if choice == 1:
#       print("Quiz")
#       break
#    elif choice== 2:
#       print("Score")
#       break
#    elif choice== 3:
#       print("Exiting")
#       break
#
#    else:
#       print("Invalid input")

########-------------------------------------#########
##--##--##--##
# functions that we need.

# def new_quiz():
#     pass
# def check_answer():
#     pass
# def display_score():
#     pass
# def re_attempt():
#     pass
#
# questions_index=[
#     "1", "who is the father of computer?"
#     "2", "what is the brain of a computer?"
#     "3", "who are you?"
# ]
# options_index=[
#     ["A. Charles Babbage", "B. James Hortons", "C. Bill Gates", "D.Dennis James"],
#     ["A. CPU", "B. RAM", "C.GPU"],
#     ["A. Human", "B. Alien", "C.Animal"]
#
# ]
#----------------------------------------------------------#
# questions= [
#         "1. who is the father of computer?",
#         "2. what is the brain of a computer?",
#         "3. who are you?"
# ]
# options= [
#     ["A. Charles Babbage", "B. James Hortons", "C. Bill Gates", "D.Dennis James"],
#     ["A. CPU", "B. RAM", "C.GPU"],
#     ["A. Human", "B. Alien", "C.Animal"]
# ]
# answers= ["A", "A", "A"]
# choices=[]
# score=0
# total=6
# count_question=0
#
# for question in questions:
#     print("------------------------------")
#     print(question)
#     for  option in options[count_question]:
#         print(option)
#     print("")
#     choice=input("Choose the right option: ").upper()
#     choices.append(choice)
#     if choice == answers[count_question]:
#         score+=2
#         print("correct answer!!")
#     else:
#         print("wrong answer!!")
#         print("")
#         print(f"Right answer is: {answers[count_question]}")
#     count_question+=1
#
# print("-----------------------------------")
# print("------------RESULTS----------------")
# print("-----------------------------------")
#
# print("Answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()
# print("Choices: ", end="")
# for choice in choices:
#     print(choice, end=" ")
# print()
#
#
#=----------------------------====######
# TOTALING AND PASS/FAIL CRITERIA ON BASIS OF PERCENTAGES#
# print("Total score:",score, "out of", total)
#
# # convert the score into percentage and then decide whether the user pass or failed the quiz.
# print("Total score:",score, "out of", total)
# percentage= (score/total)*100
# print(f"percentage :{percentage:.2f}")
# print()
#
# if percentage<40:
#     print("Unfortunately, you have to retake the test")
#     print("Results: Grade: D","", "score:", score, "", "Percentage",f"{percentage:.2f}")
# elif(percentage>40 and percentage<50):
#     print("You have passed the test by getting grade C")
#     print("Results: Grade: C","","score:", score, "", "Percentage",f"{percentage:.2f}")
# elif percentage>50 and percentage<70:
#     print("You have passed the test by getting grade B")
#     print("Results: Grade: B","", "score:", score, "", "Percentage",f"{percentage:.2f}")
# elif percentage>70 and percentage<80:
#     print("Well done! You have passed the test by getting grade A")
#     print("Results: Grade: A","","score:", score, "", "Percentage",f"{percentage:.2f}")
# elif percentage>80:
#     print("Excellent! You have passed the test by getting grade A+")
#     print("Results: Grade: A+","", "score:", score, "", "Percentage",f"{percentage:.2f}")

######---------------------------------------------------------------------------#####
# maximum three attempts to pass the test. else locked out for fifteen minutes.
# to view detailed results, click enter to move to records tab.
result=""


while True:
    if result=='pass':
        results=str(input("Press 1 if you wish to view detailed results or 2 to move to next level: "))
        if results == "1":
            print("Level 1 results")
            break
        elif results == "2":
            print("Quiz__Level 2 ")
            break
        else:
            stop()
    else:
        print("Press 3 to exit")




































