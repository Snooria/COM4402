#print("Hello World")
import statistics

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

# Mini Design Task – Simple Login Menu















