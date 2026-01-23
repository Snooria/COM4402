### Assignment COM4402 - Shahana Nooria Bilal - ID- 2418730

**Code Description**
This console interface based python quiz is designed to prompt user to test their knowledge.
below is the breakdown of the whole code.

** Key Components**
** Data Structure**
list of dictionaries is used to create quiz_database(questions). 
key field contain variable 'Question' , while Value contains question text and options.
next key field contains variable 'Answer' and value field holds correct answer.
questions can be modified by adding more dictionaries into list.

** Menu - user interaction**
Menu comes with three tabs; 1. log-in and quiz 2. sign-up and quiz 3. exit
once user login or sign up then quiz will be prompted with two options;
a. quiz 5 questions b. quiz 10 questions 
it allows users to decide whether they want to attempt half of the quiz or full. 
Once user decided then questions will start displaying on screen with options a,b,c or d.
If choice is correct then program will display correct message with +2 score. 
Otherwise only 'wrong answer' message will be displayed. 
Results will be displayed at the end of quiz

** Score Tracker**
score counter is initialized with the start of the quiz.
correct answer will add 2 scores or wrong answer will add no score. 

**# How Code Works**

1. Initialization
quiz starts with main menu displaying three options ; 1. login 2.sign-up 3.exit
both login and sign up take user to quiz_questionnaire.

2. Main Loop
Once the login process is done, program prompted to quiz options;
a. quiz 5 questions    b. quiz 10 questions
once choice is made, quiz starts displaying question with options and prompt user to make right choice.
Two initialization take place; score+=2 and count+=1
if answer is correct, score is incremented by +2 along with displayed message.
If not then message is displayed 'wrong answer'.

3. Calculation and Results
Calculations are done with help of function created in program.
pass/fail is based on percentage achieved.
Results will display along with marks, percentages and feedback message. 

**Getting back to main menu**
Screen message will be displayed to click any key to get back to main menu

**Exit point**
if user type integer 3, quiz will be closed with thank you message. 

Thank you 