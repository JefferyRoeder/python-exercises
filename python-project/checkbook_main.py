
print('~~~~ Welcome to your terminal checkbook! ~~~')
print('\n'*2)
print('What would you like to do?\n')
print('1) View current balance')
print('2) Record a debit withdraw')
print('3) Record a credit deposit')
print('4) exit')

user_action = int(input('Your choice? '))
exit = False
while exit == False:

    if user_action > 4:
        user_action = int(input(f'{user_action} is an invalid choice, try again. '))


    elif user_action == 1:
        with open('balance_storage_test.txt','r') as bs:
            for line in bs:
                last_line = line
            print(f'Your current balance is ${line}.')
            exit = True
            