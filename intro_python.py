# Identify the data type of the following values:

type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a':[]})


# What data type would best represent:

# A term or phrase typed into a search box? string
# If a user is logged in? bool
# A discount amount to apply to a user's shopping cart? float
# Whether or not a coupon code is valid? bool
# An email address typed into a registration form? string
# The price of a product? float
# A Matrix? list
# The email addresses collected from a registration form? list
# Information about applicants to Codeup's data science program? dictionary


# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

# '1' + 2 : error
# 6 % 4 : 2
# type(6 % 4) : Int
# type(type(6 % 4)): type
# '3 + 4 is ' + 3 + 4: error
# 0 < 0 : False
# 'False' == False : False
# True == 'True' : False
# 5 >= -5 : True
# !False or False : error
# True or "42" : True
# !True && !False : error
# 6 % 5 : 1
# 5 < 4 and 1 == 1 : False
# 'codeup' == 'codeup' and 'codeup' == 'Codeup' : False
# 4 >= 0 and 1 !== '1' : error
# 6 % 3 == 0 : True
# 5 % 2 != 0 : True
# [1] + 2 : error
# [1] + [2] : [1,2] : error
# [1] * 2 : [1,1]
# [1] * [2] : error
# [] + [] == [] : True
# {} + {} : error

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
mermaid_days = 3
bear_days = 5
hercules_days = 1
rate = 3
total = (mermaid_days * rate) + (bear_days * rate) + (hercules_days * rate)
print(total)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_rate = 400
amazon_rate = 380
facebook_rate = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10

total_pay = (google_rate * google_hours) + (amazon_rate * amazon_hours) + (facebook_hours * facebook_rate)

print(total_pay)


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
# can attend
course_seats_available = 2
course_overlap = False
if course_seats_available > 0 and course_overlap == False:
    able_to_enroll = True  
else:
    able_to_enroll = False
print(able_to_enroll)

# can't attend
course_seats_available = 2
course_overlap = True
if course_seats_available > 0 and course_overlap == False:
    able_to_enroll = True  
else:
    able_to_enroll = False
print(able_to_enroll)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
# discount applied
products_purchased = 1
offer_expiration = 8/12/2020
premium_memeber = True
if premium_memeber == True or (offer_expiration >= today() and products_purchased >2):
    special_offer = True
else:
    special_offer = False
print(special_offer)

# discount not applied
products_purchased = 1
offer_expiration = 8/12/2020
premium_memeber = False
if premium_memeber == True or (offer_expiration >= today() and products_purchased >2):
    special_offer = True
else:
    special_offer = False
print(special_offer)


# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword '

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters

password_character_requirement = len(password) >=5
print(password_character_requirement)

# the username must be no more than 20 characters

username_character_requirement = len(username) <= 20
print(username_character_requirement)

# the password must not be the same as the username

username_password_match = password != username
print(username_password_match)

# bonus neither the username or password can start or end with whitespace

no_leading_ending_spaces = username[0] != ' ' and username[-1] != ' ' and password[0] != ' ' and password [-1] != ' '
print(no_leading_ending_spaces)

no_leading_ending_spaces_v2 = len(username + password) == len(username.strip() + password.strip())
print(no_leading_ending_spaces_v2)