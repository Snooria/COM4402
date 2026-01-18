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
import grade

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
total_score=10

def percentage_grading(score,total_score):
    percentage=(score/total_score)*100
    return percentage



score=float(input("enter your score: "))
percentage=percentage_grading(score,total_score)
# print(f"percentage is: {percentage:.2f}%")

def quiz_grading(score,total_score):
    percentage=percentage_grading(score,total_score)

    if percentage<40:
        grade="D"
        print("Failed...!!")
    elif 40> percentage <60:
        grade="C"
        print("You have passed...!!")
    elif 60> percentage <70:
        grade="B"
        print("Good..You have successfully passed...!!")
    elif 70> percentage <80:
        grade="A"
        print("Great....You have passed...!!")
    elif percentage>80:
        grade="A+"
        print("Brilliant.. You did a great job..!!")
    return grade

grade=quiz_grading(score,total_score)
print(f"Percentage: {percentage}%")
print(f"Grade:{grade}")




