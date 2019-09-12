# 1. Conditional Basics

# A: prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input().capitalize()
if day_of_week == "Monday":
    print("Today is " + day_of_week)
else:
    print("Today is not" + day_of_week)

# B: prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input().capitalize()

if day_of_week == 'Saturday' or day_of_week == 'Sunday':
    print(day_of_week + " is a weekend")
else:
    print(day_of_week + " is a weekday or a silly word you typed to be a meanie")

# C: create variables and make up values for

hours_worked = 45
hourly_rate = 10
if hours_worked > 40:
    (40 * hourly_rate) + ((hours_worked -40) * (hourly_rate *1.5))


# 2. Loop Basics
#A: While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
i = 0
while i < 100:
    print(i)
    i += 2
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal

i = 2
while i < 1000000:
    print(i)
    i = i * i

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5

# B: For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input())
for n in range(1,11):
    
   print(f'{number} x {n} = {n * number}')

# Create a for loop that uses print to create the output shown below.

for n in range(1,10):
    
   print(f'{str(n) * n}')
    

# C: break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.


num = input("Give me an odd number: ")
# while input is even or not odd stay in loop
while num.isdigit() == False or int(num) % 2 == 0 and int(num) >0 and int(num) <=50:
    num = input('Not an odd number between 1 and 50, try again: ')
    continue
    
print(f'Number to skip is: {num}')
num = int(num)
for n in range(1,50,2):
    if n == num:
        print(f'Yikes!, Skipping number: {n}')
    elif n % 2 == 1:
        print(f'Here is an odd number: {n}')
    else:
        print(f'Yikes!, Skipping number: {n}')


# num = input("Give me an odd number: ")
# if num.isdigit() == False:
#     print("Not an odd number try again")
# elif int(num) % 2 == 0:
#     print("Not an odd number, try again")
# else:
#     print(f'Number to skip is: {num}')
#     num = int(num)
#     for n in range(1,50,2):
#         if n == num:
#             print(f'Yikes!, Skipping number: {n}')
            
#         elif n % 2 == 1:
#             print(f'Here is an odd number: {n}')
            
#         else:
#             print(f'Yikes!, Skipping number: {n}')
    
# D: The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

num = input()

if num.isdigit() == False or int(num) < 0:
    print("Not a positive number, try again")
else:
    num = int(num)
    for n in range(0,num+1):
        print(n)
    

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

num = input()

if num.isdigit() == False or int(num) < 0:
    print("Not a positive number, try again")
else:
    num = int(num)
    for n in range(num,0,-1):
        print(n)

# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output


from math import sqrt
try_again = 'y'
while try_again == 'y':
    num = input("please enter a number: ")
    num = int(num)
    for n in range(1,num+1,1):
        print(n," ",round(sqrt(n),3)," ",n**2)
    try_again = input("would you like to try again? y or n: ")

from math import sqrt
try_again = 'y'
while try_again == 'y':
    num = input("please enter a number: ")
    num = int(num)
    print("Num | SQRT | Square")
    for n in range(1,num+1,1):
        print(n,"   ",round(sqrt(n),3),"  ",n**2)
    try_again = input("would you like to try again? y or n: ")