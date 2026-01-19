from colorama import Fore, Back, Style, init
from torchgen.api.cpp import return_type

init(autoreset=True)
# print(Fore.RED+"this text is red")
# print(Back.GREEN+"this text is green")
# print(Style.RESET_ALL)


import time
# for i in range(0,5):
#   print(i)
#   time.sleep(1)

# import turtle
#
# t=turtle.Turtle()
#for i in range(0,5):
#   print(i)
#   time.sleep(1)
#
# #using basic colors
# t.color("red")
# t.begin_fill()
# t.circle(30)
# t.end_fill()
#
# # Move to a new position
# t.penup()
# t.goto(100, 0)
# t.pendown()
#
# # Try another color
# t.color("blue")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
#
# # Create screen and set background color
# # screen = turtle.Screen()
# # screen.bgcolor("lightblue")  # Using a named color
# #
# # t = turtle.Turtle()
# # t.color("navy")
# # t.begin_fill()
# # t.circle(50)
# # t.end_fill()
# #
# # turtle.done()





# # #Dictionary
# prices={"coffee": "£10.50",
#        "latte": "07.50",
#        "water": "01.00"
# }
#
# item= input("enter item name: ")
#
# #if loop to check the availability of certain item data within the dictionary.
#
# if item in prices:
#     print(f"The price of {item} is:" ,prices[item])
# else:
#     print("unknown item")
import grades

# def sq(n):
#     print(f"Square of {n} is {n*n}")
#     return n * n
#
# def add(a, b):
#     return a+b
#
# def sub(a,b):
#     return a - b

#
# while True:
#     print(f"Please choose operation:\n"
#           f"1. Add\n"
#           f"2. Sub\n"
#           f"0. Exit")
#
#     choice = input()
#
#     a = int(input("Enter A: "))
#     b = int(input("Enter B: "))
#
#     if choice == "1":
#         result = add(a, b)
#         print(f"Result: {result}")
#
#     elif choice == "2":
#         result = sub(a, b)
#         print(f"Result: {result}")
#
#     elif choice == "0":
#         print("EXIT chosen")
#         break


# print(sq(5))

# create function to do something . print some value.
#create function to get the value for u
#create function to do get input from user and get into function , do the calculations and get back to you and display the output.
#means return back to you.
total_score=30

def percentage_grading(score,total_score):
    percentage=(score/total_score)*100
    return percentage



# score=float(input("enter your score: "))
# percentage=percentage_grading(score,total_score)
# print(f"percentage is: {percentage:.2f}%")

def quiz_grading(score,total_score):
    percentage=percentage_grading(score,total_score)

    if percentage<40:
        grades="D"
        print(Fore.BLACK+ Back.RED+"Failed...!!")
    elif 40<= percentage <60:
        grades="C"
        print(Fore.BLACK+Back.YELLOW+"You have passed...!!")
    elif 60<= percentage <70:
        grades="B"
        print(Fore.BLACK+Back.BLUE+ "Good..You have successfully passed...!!")
    elif 70<= percentage <80:
        grades="A"
        print(Fore.BLACK + Back.GREEN+"Great....You have passed...!!")
    elif percentage >=80:
        grades="A+"
        print(Fore.BLACK + Back.GREEN +"Brilliant.. You did a great job..!!")
        print(Style.RESET_ALL)

    return grades

# percentage = percentage_grading(score, total_score)

def Detailed_results(total_score):
    score = float(input("enter your score: "))
    Per = percentage_grading(score, total_score)
    Grade=quiz_grading(score,total_score)

    print("your percentage is:", Per)
    print("your grade is:", Grade)
    return Per,Grade

Detailed_results(total_score)



# print(f"percentage is: {percentage:.2f}%")
# print(f"Grade:{grades}")

# print(Fore.GREEN + f"Percentage: {percentage}%")
# print(Fore.BLUE + f"Grade: {grade}")
#
# for i in range(0,5):
#   print(i)
#   time.sleep(1)





