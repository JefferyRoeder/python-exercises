#4.4_function_exercises

# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2:
        return True
    else:
        return False
is_two(3)

# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    x = x.strip().lower()
    if x in 'aeiou' and len(x) == 1:
        return True
    else:
        return False
is_vowel('A ')


# 3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    x = x.strip().lower()
    if x not in 'aeiou' and len(x) == 1:
        return True
    else:
        return False
is_consonant('A ')

# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def consonant_capitalize(x):
    if x[0] in 'aeiou':
        return x.capitalize()
    else:
        return x
consonant_capitalize('yold faithful')


# 5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip,bill):
    return (tip/100) * bill
    
calculate_tip(15,50)

# 6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(price,discount):
    if discount > 0 and discount < 1:
        return price * (1-discount)
    else:
        return "Enter discount as decimal"
apply_discount(100,.15)

# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(num):
    
    return int(num.replace(",",""))
handle_commas('1,000')

# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'
    
get_letter_grade(68)

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    word = word.lower()
    for w in word:
        if w in 'aeiou':
            word = word.replace(w,"")
    return word
remove_vowels("hello")

# 10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

