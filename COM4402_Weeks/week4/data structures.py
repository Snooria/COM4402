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

##============================##
#ATM-MACHINE#

# balances={
#     "alice": 2000.00,
#     "harry": 1000.00
# }
# username= input("enter name: ").lower()
#
# #check if we have user in our database
#
# if username in balances:
#     print("current balance:", balances[username])
#     amount = float(input("deposit amount: "))
#     balances[username] = float(balances[username]) + amount
#     print(f"new balance: £{balances[username]:.2f}")
# else:
#      ("unknown username")
##=================================##
##----Choose a Data Structure + CRUD Functions####
#Dictionary will be used. as we can update its data.
#add or update student's mark.

# def add_mark(marks,name,mark):
#     #my_dictionary.update()

# my_dictionary={
# #     "harry" : 65,
# #     "peter" : 90,
# #
# # }

#==================================#
#==================================#
#==================================#
#==================================#


# Activity 1 – Student Marks (SOLVED EXAMPLE)
#CRUD Functions
# my_dictionary = {
#     'harry'  : 56,
#     'charlie': 62,
#     'schism':70,
#     'Sarah':50,
#     'william':42
# }
# # print(my_dictionary)
#
# name=str(input("enter your name: "))
# if name in my_dictionary:
#     print(my_dictionary[name])
# else:
#     print("your name is not in the dictionary")


#update#
# my_dictionary.update({"Maria": 63})
# print(my_dictionary)
#---------------------------#
# #delete#
# my_dictionary.pop('harry')
# print(my_dictionary)
#---------------------------#
#retrieve information by using key#
#call some specific information
# if "name" in my_dictionary:
#     print("name",my_dictionary["name"])

#-------------------------------------------------------------------##
my_dictionary = {
    'harry'  : 56,
    'charlie': 62,
    'schism':70,
    'Sarah':50,
    'william':42
}
#function

# def add_mark(marks,name,mark):
#     marks[name]=mark
#     return marks
# name=input("enter your name: ")







