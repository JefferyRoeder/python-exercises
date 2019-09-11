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
hourly_rate = 58
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


    