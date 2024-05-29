# Write a program to check whether a person is eligible to vote or not?
# '''
user_age = 18;

if user_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
#using the input field   
# user_age_input = int(input('Please enter your age: '));

# if user_age_input >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
    

    
# Write a program to check char is vowel or not.    
char = input('Enter a character: ')
if (char.lower() == 'a' or char.lower() == 'e' 
   or char.lower() == 'i' or char.lower() == 'o'
   or char.lower() == 'u'):
    print("Vowel")
else:
    print("Consonant")    


# Write a program to check the number is positive or negative. User input.
number = int(input('Please enter a number: '))
if number >=0 :
    print('Number is positive');
else:
    print('Number is negative');
    

# Write a program to check whether a number is odd or even?   
number_even_odd = 5
if number_even_odd % 2 ==0 :
    print('Number is even');
else:
    print('Number is odd');
 
number_even_odd_input = int(input('Please enter a number: '))
if number_even_odd_input % 2 ==0 :
    print('Number is even');
else:
    print('Number is odd');
    
    
# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
subject_score = int(input('Please enter a number: '))
if subject_score >=80 :
    print('Your grade is A+');
elif subject_score>=70:
    print('Your grade is A');
elif subject_score>=60:
    print('Your grade is B');
elif subject_score>=50:
    print('Your grade is C');
elif subject_score>=40:
    print('Your grade is D');
else:
    print("Fail");



# Write a program to check whether a number is divisible by 7
divisible = int(input('Please enter a number: '))
if divisible % 7 ==0 :
    print('Number is divisible by 7');
else:
    print('Number is not divisible by 7');
    
    
# Write a program to check if year is leap year.
year = 2012
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):   
    print("Given Year is a leap Year");  
else:  
    print ("Given Year is not a leap Year")      
    


# Write a program to ask user its name and check whether name consists of 5 or more letters

# user_name = input('Please enter your name: ')
# if len(user_name) >= 5:
#     print(f'Your name has {len(user_name)} letters');
# else:
#     print('Your name has less than 5 letters')
    
    
    

# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator.

input_1 = int(input('Please enter a number: '))
input_2 = int(input('Please enter a number: '))
operator = input('Please enter an operator(x , + , - , / , %): ')

if operator == '+':
    print(input_1 + input_2)
elif operator == '-':
    print(input_1 - input_2)
elif operator == '/':
    print(input_1 / input_2)    
elif operator == '*' or operator.lower() =='x':
    print(input_1 * input_2)
elif operator =='%':
    print(input_1 % input_2)  
else:
    print('Invalid operator') 
    
    
# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
num_input = int(input('Please enter a number: '))
if num_input % 2 == 0 and num_input % 3 ==0 :
    print(f'{num_input} is divisible by 2 and 3')
elif num_input % 2 == 0 and num_input % 3 != 0 :
    print(f'{num_input} is divisible by 2')
elif num_input % 2 != 0 and num_input % 3 == 0 :
    print(f'{num_input} is divisible by 3') 
else:
    print(f'{num_input} is not divisible by 2 and 3')       
 

# Write a program that accepts 2 inputs from user and check which number is largest.  
num1_input = int(input('Please enter a number: '))
num2_input = int(input('Please enter a number: '))

if num1_input > num2_input :
    print(f'{num1_input} is greater than {num2_input}')
elif num1_input < num2_input:
    print(f'{num2_input} is greater than {num1_input}')
else:
    print(f'{num1_input} and {num2_input} are equal')
    

    
# Write a program that accepts 3 input from user and check which number is largest.
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a number: '))    
num3 = int(input('Please enter a number: '))   

if num1 == num2 == num3 :
    print(f'{num1}, {num2} and {num3} are equal')
elif num1 >= num2 and num1 >= num3  :
    print(f'{num1} is greater than {num2} and {num3}')  
elif num2 >= num1 and num2 >= num3 :
    print(f'{num2} is greater than {num3} and {num1}')
elif num3 >= num1 and num3 >= num2 :
    print(f'{num3} is greater than {num1} and {num2}')
    
    
# '''  
    
# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15
             
num_1 = int(input('Please enter a number: '))
num_2 = int(input('Please enter a number: '))    
num_3 = int(input('Please enter a number: '))  

if (num_1 > num_2 and num_1 < num_3) or (num_1 < num_2 and num_1 > num_3):
    print(f'{num_1} is second largest')
elif (num_2 > num_1 and num_2 < num_3) or (num_2 < num_1 and num_2 > num_3):
    print(f'{num_2} is second largest')
elif (num_3 > num_1 and num_3 < num_2) or (num_3 < num_1 and num_3 > num_2):
    print(f'{num_3} is second largest')                     


# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

color = input('Enter the color of the traffic light (GREEN, RED, YELLOW): ')

if color.lower() =='green':
    print('Car is allowed to go')
elif color.lower() =='red':
    print('Car has to stop')
elif color.lower() =='yellow':
    print('Car has to wait')  
else :
    print('Invalid input')
    

# Write a program that takes two numbers as input and prints:

# "First number is greater" if the first number is greater than the second number.
# "Second number is greater" if the second number is greater than the first number.
# "Both numbers are equal" if the two numbers are equal.                  

num1_input = int(input('Please enter a number: '))
num2_input = int(input('Please enter a number: '))

if num1_input > num2_input :
    print('First number is greater')
elif num1_input < num2_input:
    print('Second number is greater')
else:
    print('Both numbers are equal')
    

# Write a program that takes a password as input and checks its strength:

# If the password length is less than 6, print "Weak password".
# If the password length is between 6 and 12, print "Moderate password".
# If the password length is more than 12, print "Strong password".  

user_password = input('Enter your password: ')

if len(user_password) < 6 :
    print('Weak password')
elif len(user_password) >=6 and len(user_password) < 12 :
    print('Moderate password')
elif len(user_password) >= 12:
    print('Strong password')       
    

# Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

# If the years of service are less than 5, no bonus.
# If the years of service are between 5 and 10, bonus is 10% of the salary.
# If the years of service are more than 10, bonus is 20% of the salary.
# Print the bonus amount.   

salary = int(input('Please enter your salary')) 
years_of_service = int(input('Please enter your year of service'))
bonus = 0

if years_of_service < 5 :
    print(f"your bonus is {bonus}")
elif years_of_service >= 5 and years_of_service <= 10 :
    bonus = salary * 0.10
    print(f'Your bonus is {bonus}')
elif years_of_service > 10:
    bonus = salary * 0.20
    print(f'Your bonus is {bonus}')
    
    
    
# Write a program that takes the total amount of a purchase as input and applies a discount:

# If the amount is less than $100, no discount.
# If the amount is between $100 and $500, apply a 10% discount.
# If the amount is more than $500, apply a 20% discount.
# Print the final amount after the discount.

purchase_amount = int(input('Please enter a purchase amount'))

if purchase_amount < 100 :
    print(f'Your final amount is {purchase_amount}')
elif purchase_amount >=100 and purchase_amount <= 500:
    discount = purchase_amount * 0.10
    print(f'Your final amount is {purchase_amount - discount}')
elif purchase_amount > 500 :
    discount = purchase_amount * 0.20
    print(f'Your final amount is {purchase_amount - discount}')
    
    

# Write a program that takes a person's age as input and prints the age group they belong to:

# If the age is less than 13, print "Child".
# If the age is between 13 and 19 (inclusive), print "Teenager".
# If the age is 20 or above:
#     If the age is less than 65, print "Adult".
#     If the age is 65 or above, print "Senior".    

user_age = int(input('Enter your age: '))

if user_age < 13 :
    print('Child')
elif user_age >= 13 and  user_age <= 19:
    print('Teenager')
elif user_age >=20 :
    if user_age < 65:
        print('Adult')
    elif user_age >= 65:
        print('Senior')
        


# Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

# If the customer is a member:
#     If the purchase amount is $50 or more, print "Eligible for 10% discount".
#     Otherwise, print "Eligible for 5% discount".
# If the customer is not a member:
#     If the purchase amount is $100 or more, print "Eligible for 5% discount".
#     Otherwise, print "No discount".

member_ship_status = True
amount = int(input('Please enter your purchase amount: '))

if member_ship_status == True :
   if amount >= 50:
    print("Eligible for 10% discount")
   else:
       print("Eligible for 5% discount")
        
elif member_ship_status == False :
    if amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")


# create the same ATM machine program that we do in last class.
# features:
#     allow only affiliated_card if age < 60
#     allow govt employee regardless of age and affiliated_card
#     charge 10 Rs more if grade is less than 18    

balance = 500
affiliated_card = True
age = 50
is_govt_employee = True
high_grade = True
transaction_charges = 10

withdraw_amount = int(input('Enter the amount to withdraw from this transaction: '))

# if withdraw_amount > balance :
#     print('Insufficient balance')

if affiliated_card and age < 60 :
    if withdraw_amount > balance :
        print('Insufficient balance')
    else:
        balance -= withdraw_amount
        print(f'Your balance is {balance}')
elif is_govt_employee and withdraw_amount > balance :
    if high_grade : 
        balance -= withdraw_amount
        balance -= transaction_charges
        print(f'Your balance is {balance}')
    else : 
        balance -= withdraw_amount
        print(f'Your balance is {balance}')
        
            