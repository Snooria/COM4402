### Assignment COM4402 - Shahana N Bilal - ID- 2418730

## Code Description**


This console interface based python quiz is designed to prompt user to test their knowledge.<br>
Below is the breakdown of the whole code.

#### Key Components

## Data Structure

list of dictionaries is used to create quiz_database(questions).<br> 
Key field contain variable 'Question' , while Value contains question text and options.<br>
Next key field contains variable 'Answer' and value field holds correct answer.<br>
Questions can be modified by adding more dictionaries into list.<br>

## Menu - user interaction**

Menu comes with three tabs; 1. log-in and quiz 2. sign-up and quiz 3. exit.<br> 
Once user login or sign up then quiz will be prompted with two options;<br> 
a. quiz 5 questions b. quiz 10 questions.<br> 
It allows users to decide whether they want to attempt half of the quiz or full.<br>  
Once user decided then questions will start displaying on screen with options a,b,c or d.<br> 
If choice is correct then program will display correct message with +2 score.<br> 
Other-wise only 'wrong answer' message will be displayed.<br> 
Results will be displayed at the end of quiz.<br> 

## Score Tracker

score counter is initialized with the start of the quiz.<br> 
Correct answer will add 2 scores or wrong answer will add no score.<br>  

## How Code Works

1. ## Initialization

Quiz starts with main menu displaying three options ; 1. login 2.sign-up 3.exit<br> 
Both login and sign up take user to quiz_questionnaire.<br> 

2. ## Main Loop

Once the login process is done, program prompted to quiz options;<br> 
a. quiz 5 questions    b. quiz 10 questions.<br> 
Once choice is made, quiz starts displaying question with options and prompt user to make right choice.<br> 
Two initialization take place; score+=2 and count+=1<br> 
If answer is correct, score is incremented by +2 along with displayed message.<br> 
If not then message is displayed 'wrong answer'.<br> 

3. ## Calculation and Results

Calculations are done with help of function created in program.<br> 
Pass/fail is based on percentage achieved.<br> 
Results will display along with marks, percentages and feedback message.<br> 

## Getting back to main menu

Screen message will be displayed to click any key to get back to main menu<br> 

Exit point

### If user type integer 3, quiz will be closed with thank you message. 

## Thank you 