# week 2 session 3 file
#print("Hello")
#1.Cinema Ticket Category
#Ask the user for their age and classify the ticket as:
#Age < 5 → “Free entry”
#5–17 → “Child ticket”
#18–64 → “Adult ticket”
#65+ → “Senior ticket” Use if/elif/else.


#age = int(input("enter your age: "))
#if age<5:
#    print("you are eligible for free entry")
#elif 5 < age <= 17:
#    print("child ticket")
#elif 18< age <=64:
#    print("adult ticket")
#elif age>64:
#    print("senior ticket")


#2. Library Fine Calculator
# Ask for days_late (int).
# 0 → “No fine”
# 1–5 → “Fine = £1”
# 6–10 → “Fine = £5”
# > 10 → “Fine = £10 and membership review” Print the correct message with a single if/elif/else
# chain.

#days = int(input("enter number of days you were late: "))
#if days<=0:
#    print("you have nothing to pay")
#elif 0< days <=5:
#    print("Fine=£1.00")
#elif 5< days <=10:
#    print("Fine=£5.00")
#elif days>10:
#    print("Fine=£10.00")

# 3. Exam Borderline Check (Nested)
# Ask for score (0–100).
# If score ≥ 40:
# If score is between 38 and 42 (inclusive), print “Borderline pass, consider review.”
# Else print “Clear pass.”
# Else print “Fail.” Use a nested if inside the pass branch.

# score = int(input("enter your score:  "))
# if score>=40:
#    if 40< score <=42:
#          print("Borderline pass, consider review")
#    else:
#        print("clear pass")
# else:
#    print("Fail")



#4. Discount Eligibility
#Ask for is_student (“yes”/“no”) and age (int). The user gets a discount if:
#They are a student or
#Their age is below 18. Use if/elif/else and logical operators (and / or) to decide whether to print
#“Discount applied” or “No discount”.

# student = str(input("are you a student?: "))
# age = int(input("enter your age: "))
# if student!="Y" and age>18:
#         print("sorry, discount can not applied.")
# else:
#         print("discount applied")


# 5. Traffic Light Action
# Ask for a colour: "red", "amber", or "green" (any case). Normalize with .lower().
# "red" → “Stop”
# "amber" → “Get ready”
# "green" → “Go”
# Anything else → “Invalid colour” Use if/elif/else.

# color = str(input("choose one color from the following;red, amber, green:   ")).lower()
# if color == "red":
#     print(color,"Stop")
# elif color == "amber":
#     print(color,"Get ready")
# elif color == "green":
#     print(color,"Go")
# else:
#     print("Invalid color")

#---------------------

# 6. Multiple of 3, 5, or Both
# Ask for a number.
# If it is divisible by both 3 and 5 → “FizzBuzz”
# Else if divisible by 3 → “Fizz”
# Else if divisible by 5 → “Buzz”
# Else → “No match” Use % and an ordered if/elif/else chain.

# num = int(input("enter number: "))
# if num%3 ==0 and num%5 ==0:
#     print("FizzBuzz")
# elif num%3 ==0:
#     print("Fizz")
# elif num%5 == 0:
#     print("Buzz")
# else:
#     print("invalid input")


# 7. Meal Recommendation (Nested)
# Ask for time_of_day ("morning", "afternoon", "evening") and is_hungry ("yes"/"no").
# If is_hungry == "no" → “Have some water and rest.”
# If is_hungry == "yes":
# If time_of_day == "morning" → “Have breakfast.”
# "afternoon" → “Have lunch.”
# "evening" → “Have dinner.”
# Anything else → “Snack time.” Use nested if for the hungry branch.


# 8. Module Mark Status
# Ask for coursework mark and exam mark (both 0–100). Overall rule:
# If either mark < 35 → “Automatic fail (component below 35).”
# Else if average of the two ≥ 40 → “Module passed.”
# Else → “Module failed (average below 40).” Use combined conditions and if/elif/else.


# 9. Simple Two-Stage Verification
# Ask the user for a 4-digit PIN.
# If PIN is exactly "1234":
# Ask a security question: “What is your favourite colour?”
# If answer equals "blue" (any case) → “Access granted.”
# Else → “Security answer incorrect.”
# Else → “Wrong PIN.” Use nested if and .lower().



# 10. Sport Suggestion by Weather and Mood
# Ask for weather ("sunny", "rainy", "cold") and mood ("active", "tired").
# If weather is "sunny" and mood "active" → “Go for a run.”
# If weather "sunny" and mood "tired" → “Relax in the park.”
# If weather "rainy" → “Indoor workout.”
# If weather "cold" → “Go to the gym.”
# Anything else → “No suggestion available.” Use if/elif/else with combined logical conditions.










