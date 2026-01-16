#
#
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
questions = [{"""2. Which software is used for creating and managing spreadsheets???
a. Microsoft Excel
b. Microsoft PowerPoint
c. Adobe Illustrator
d. Google Drive""":"b"},{"""1.what is name of American president?
a. william Harold
b. Donald Trump
c. George Bush""":"b"}



            ]
score=0
total_score=4
# for line in lines:
#     print("\n".join(lines))
# # multi_line = "\n".join(lines)
# # print(multi_line)
for i in questions:
    print("\n".join(i))
    print()
    flag1=input("--Do you want to skip the question(Yes/No)?:").lower()
    if flag1=='yes':
        continue
    answer= input("enter the answer(a/b/c/d): ")
    if answer==questions:
        print()
        print("correct answer you got +2")
        score =score+2
        print()
    else:
        print()
        print("wrong answer")
    flag2=input("--Do you want to quit the quiz(Yes/No)?:").lower()
    if flag2=='yes':
        break
print("Total score is:", score,"/",total_score)


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
#     print("Invalid input. Please enter a numeric value.")
