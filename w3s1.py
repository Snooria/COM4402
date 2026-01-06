from win32con import PASSTHROUGH

#The for loop controls how many times we repeat
#Inside the loop, we can use input, if, strings, math


# for i in range(5):
#  print(i)
#
# for i in range(3):
#     print("Hello")

# for i in range(1, 9, 2):
#     print(f"Hello {i}")

# students= ["Aisha", "Bilal", "Chen", "Dina"]
# for name in students:
#     print("Hello", name)

#Activity 2 – Count Vowels in a Word
#Asks the user for a word
# Uses a for loop to go through each character
# Counts how many are vowels (a, e, i, o, u, case-insensitive)
# Prints: "Number of vowels: <count>"

# word = input("enter a word: ")
# word = word.lower()
# vowels = 0
#
# for ch in word:
#     if ch in "aeiou":
#         vowels = vowels + 1
#
# print("number of vowels:", vowels)


# number= [3,4,8,10]
# userNum = int(input("Enter number: "))
# number.append(userNum)
# for n in number:
#     if n % 2 == 0:
#         print(n, "is even number")
#     else:
#         print(n, "is odd number")

# count down timer program
# start = int(input("start from: "))
#
# for n in range(start, 0, -1):
#     print(n)
# print("Go")


# Design a program that:
# Reads 5 student names into a list
# Then uses a for loop to print:

#####-----------------------------------#####

# Practice Problems – Python for Loops
# 1. Repeat a Word Ask the user for a word and a number n. Use a for loop to print the word n times,
# each on a new line with a counter, e.g. 1: hello.

# word = str(input("enter word: "))
# num = int(input("enter a number: "))
#
# for i in range(num):
#     print(f"{i+1}: {word}")

##------------------------------------------------##
#2. Sum of First N Numbers
# Ask the user for an integer n.
# Use a for loop to calculate the sum of numbers from 1 to n, then print the result.

# n = int(input("Please enter value of n: "))
# total = 0
#
# for i in range(n):
#     new_number = int(input(f"Enter number {i+1} of {n}: "))
#     total += new_number
#
# print("FINAL TOTAL: ", total)

#-----------------------------------#

# 3. Multiplication Table
# Ask for a number x.
# Use a for loop to print the multiplication table from 1 × x
# up to 10 × x.

# x = int(input("enter value of x: "))
# for i in range(10):
#     print(f"{i+1} * {x} = {(i+1)*x} ")

#----------------------------#

# 4. Count Characters (Non-space)
# Ask the user for a sentence.
# Use a for loop over the string to count
# how many characters are not spaces, then print the count.

# sentence= str(input("write a sentence: ")).lower()
# res = 0
# for ch in sentence:
#     if ch != " ":
#         res += 1
# print(res)

#-------------------------------------------------#

# 5. Find Maximum Mark
# Ask how many marks the user will enter.
# then read that many integers.
# Use a forloop to find and print the highest mark entered.

# m= int(input("how many marks would you like to enter: "))
# highestMark = 0
# for i in range(m):
#     marks=int(input("enter marks: "))
#     if marks > highestMark:
#         highestMark = marks
# print(f"your highest mark is: {highestMark}")
 #----------------------------------------#

# 6. Filter Passing Marks
# Ask how many marks to enter,
# then read that many integers. Using a for loop,
# print only the marks that are 40 or above, one per line, and count how many passed.

# n =int(input("how many times you want to enter the number?: "))
# pass_count = 0
# fail_count = 0
#
#
# for i in range(n):
#     num=int(input(f"Enter number {i+1} of {n}: "))
#     if num >= 40:
#         print(f"pass: {num}")
#         pass_count += 1
#     else:
#         fail_count += 1
# print(f"pass candidates: {pass_count} ")
# print(f"fail candidates: {fail_count} ")

###------------------------------------#####

# 7. Reverse a String (Manual)
# Ask the user for a word.
# Use a for loop (not slicing) to build a new string
# that is the reverse of the original,
# then print it.

# word =str(input("write a word: ")).lower()
# res = ""
# for word in reversed(word):
#     res += word + ""
#
# res = res.strip()
# print(res)


##------------------------------##

# 8. Count Specific Letter in a List of Names
# Ask how many names to enter; store them in a list.
# Then ask for a letter (e.g. "a").
# Use a for loop to count how many names contain that letter (case-insensitive)
# and print the total.

# n = int(input("give value to n: "))
# students= []
# letter_count= 0
# for i in range(n):
#     name =  str(input(f"enter name {i+1} of {n} to store in database: "))
#     students.append(name)
#
# letter= str(input("which letter you want to count?: ")).lower()
# for name in students:
#     if letter in name:
#         letter_count = letter_count+1
# print(f"number of names in students database containing letter {letter} are {letter_count}")
#-------------------------------------------#

##------------------------------------------##
# 9. Grade Statistics
# Ask for the number of students, then input that many marks (0–100).
# Use a for loop to compute:
# total marks
# average mark
# how many are Distinction (≥70) Print all three results.











##----------------------------------------------------##
# 10. Simple Text-Based Bar Chart Ask how many numbers to enter, then input that many positive integers
# into a list. Use a for loop to print a tiny bar chart using *, e.g. if the list is [3, 5, 1], output:
# ***
# *****
# *