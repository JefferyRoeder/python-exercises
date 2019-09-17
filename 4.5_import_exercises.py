import functions_exercises


print(FE.is_vowel('d'))
print(FE.get_letter_grade(85))
print(FE.remove_vowels('The quick brown fox jumps over the lazy dog'))


from itertools import combinations

l = [1,2,3,'a','b','c']
comb = []

comb += combinations(l,2)
print(comb)

l2 = ['a','b','c','d']
comb2 = []
comb2 += combinations(l2,2)
print(comb2)

 # Total number of users

import numpy as np
import json

from collections import Counter

with open('profiles.json','r') as f:
    new_dict = json.load(f)
    count = len(new_dict)
print(count)

# number of active users
active_users = []
for i in new_dict:
    if i['isActive'] == True:
        active_users.append(i['name'])
print(len(active_users))

# of inactive

active_users = []
for i in new_dict:
    if i['isActive'] != True:
        active_users.append(i['name'])
print(len(active_users))


import numpy as np
import json

from collections import Counter

with open('profiles.json','r') as f:
    new_dict = json.load(f)

active_users = [dict['isActive'] for dict in new_dict]

n_active_users = len(active_users)


# sum of balance

def handle_balance(s):
    return float(s[1:].replace(',',""))
    
balances = [handle_balance(dict['balance']) for dict in new_dict]

print(balances)
sum(balances)

# avg bal for users

sum(balances)/len(new_dict)

#highest balance

for user in new_dict[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_lowest_balance['balance']):
        user_with_lowest_balance = user
print(user_with_lowest_balance)

#lowest balance
for user in new_dict[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_highest_balance['balance']):
        user_with_highest_balance = user
        
#alternative for lowest balance
min(new_dict, key=lambda profile: handle_balance(profile['balance']))