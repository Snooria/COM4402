# ---------------------Holton's Quiz Program-----------------------#
from turtledemo.round_dance import stop

count=0
score=0
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
#


#
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
                    print(f"------MENU------\n----------------\n1.Quiz\n2.Score\n3.Exit")

                    try:
                        option = int(input("Enter your choice: "))
                    except ValueError:
                        print("please enter valid input")
                        continue
                    if option == 1:
                        print("Quiz")
                        break
                    elif option == 2:
                        print("Score")
                        break
                    elif option == 3:
                        print("Exiting")
                        break

                    else:
                        print("Invalid input")

        else:
            print("Wrong username or password")
    elif choice==2:
        print("---Signup---")
        username = str(input(f"Enter username:  "))
        password = input("make strong password: ")
        user_name_password.append([username, password])
        print("signup successful!")


        print()
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






