from operator import index
#
# # key questions and options
# # value --- options
#
# count=0
# score=0
# total_score=6
# #function to display total based on questions attempted by user.
# # def attempted_question(answer_count):
# #     answer_count=2+2
# #     return answer_count
# # total_score=attempted_question(answer_count)
#
#
#
# q1="""1.what is name of American president?
# a. william Harold
# b. Donald Trump
# c. George Bush"""
# q2="""2. Which software is used for creating and managing spreadsheets?
# a. Microsoft Excel
# b. Microsoft PowerPoint
# c. Adobe Illustrator
# d. Google Drive
# """
# q3="""3. What is the function of presentation software?
# a. Creating and editing images
# b. Designing websites
# c. Creating visually engaging presentations
# d. Writing computer programs"""
#
# quiz_questions={q1:"b",q2:"a",q3:"b"}
# # to iterate through dictionary, we need for loop
# for i in quiz_questions:
#     print()
#     print(i)
#     flag1=input("--Do you want to skip the question(Yes/No)?:").lower()
#     if flag1=='yes':
#         continue
#     answer= input("enter the answer(a/b/c/d): ")
#     if answer==quiz_questions[i]:
#         print()
#         print("correct answer you got +2")
#         score =score+2
#         print()
#     else:
#         print()
#         print("wrong answer")
#     flag2=input("--Do you want to quit the quiz(Yes/No)?:").lower()
#     if flag2=='yes':
#         break
# print("Total score is:", score,"/",total_score)
#
#
#
from tkinter.messagebox import QUESTION

import percentage

quiz_questions = [{"Question":"1. Which software is used for creating and managing spreadsheets?\na. Microsoft Excel\nb. Microsoft PowerPoint\nc. Adobe Illustrator",
                   "Answer": "b"},
                  {"Question":"2.what is name of American president?\na. william Harold\nb. Donald Trump\nc. George Bush",
                   "Answer": "b"},
                  {"Question":"3.what is capital of UK?\na.london\nb.bolton\nc.brighton",
                   "Answer":"a"},
                  {"Question":"4. what is cupid known for?\na.love \nb.hatred \nc.warrior ",
                   "Answer":"a"},
                  ]


count=0
score=0
total_score=8
user_answers=[]
correct_answers=['b','b','a','a']
total_questions=1



def quiz_grading(score, total_score):
    percentage=(score/total_score)*100
    return percentage
# user_name_password =[
#                     ['harry', 'ha123'],
#                     ['saima', 'sa123'],
#                     ['paige', 'pa123']
#     ]
# # for line in lines:
# #     print("\n".join(lines))
# # # multi_line = "\n".join(lines)
# # # print(multi_line)
#
# print("                                       Welcome to the Quiz")
# def get_valid_input(start, end):
#     option = -1
#     try:
#         while option < start or option > end:
#             option = int(input("Enter your choice: "))
#     except ValueError:
#         print("please enter valid input")
#     return option
# def handle_login(login_success):
#     while login_success == False:
#         print("1.Login\n2.Signup")
#
#         choice= get_valid_input(1,2)
#         if choice==1:
#             print("---Login---")
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#
#             for user in user_name_password:
#                 if username == user[0] and password == user[1]:
#                     login_success = True
#                     break
#
#             if login_success == False:
#                 print("Wrong username or password")
#
#         elif choice==2:
#             print("---Signup---")
#             username = str(input(f"Enter username:  "))
#             password = input("make strong password: ")
#             user_name_password.append([username, password])
#             print("signup successful!")
#     return login_success
for i in list(quiz_questions):
    print()
    flag2 = input("                       Do you want to QUIT the quiz at this point (Yes/No)?:").lower()
    if flag2 == 'yes':
        print("You chose to quit the quiz")
        print("Total Score is:", score, "/", total_score)
        break
    print(i["Question"])
    print()
    flag1=input("                       Do you want to SKIP the question(Yes/No)?: ").lower()
    if flag1=='yes':
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
#---------------------------------------------#
    answer = valid_option()
    user_answers.append(answer)
    if answer==quiz_questions[count]["Answer"]:
        print()
        print("correct answer you got +2")
        score +=2
        count+=1
        print()
    else:
        print()
        print("wrong answer")
        # print(f"Correct answer is:",quiz_questions["Answer"])
        count=count+1



total_questions+=1

# def detailed_results(score, total_score, user_answers, correct_answers):
#     percentage=quiz_grading(score, total_score)

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
# print("percentage is:", f"{percentage:.2f}%")






# def detailed_results(score, total_score, user_answers, correct_answers):








# def valid_option():
#     valid={"a","b","c","d"}
#     while True:
#         answer=input("enter the answer(a/b/c/d): ").lower()
#         if answer in valid:
#             return answer
#         else:
#             print("invalid option")
# answer=valid_option()
#








# for index, (key, value) in enumerate(d.items()):
#     print(index, "-", key, ":", value)

# while True:
#     quiz_grading(score, total_score)








# print("Total score is:", score,"/",total_score)
# print("user choice:",user_answers)
# print("correct answers are:",correct_answers)







### scoring logic with try/except
# try:
#     marks = float(input("Please enter the marks (0-100): "))
#     # Validate the marks are within a plausible range (0-100)
#     if 0 <= marks <= 100:
#         if marks >= 90:
#             grade = 'A'
#         elif marks >= 80:
#             grade = 'B'
#         elif marks >= 70:
#             grade = 'C'
#         elif marks >= 60:
#             grade = 'D'
#         else:
#             grade = 'F'
#         print("Grade:", grade)
#     else:
#         print("Invalid marks. Please enter a value between 0 and 100.")
# except ValueError:
print("Invalid input. Please enter a numeric value.")
