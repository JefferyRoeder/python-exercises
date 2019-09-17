
def show_menu():
    print('~~~~ Welcome to your terminal checkbook! ~~~')
    print('\n'*2)
    print('What would you like to do?\n')
    print('1) View current balance')
    print('2) Record a debit withdraw')
    print('3) Record a credit deposit')
    print('4) exit')

#brings up menu options
user_input = '1'
while user_input != '4':
    show_menu()

    user_action = input('Your choice? ')
    if user_action == '4':
        print('Thanks, have a great day!')
        user_input = '4'
    elif user_action not in ['1','2','3']:
        input('Invalid choice, try again. ')
    elif user_action in ['1','2','3']:    


        # showing current balance
        if user_action == '1':
            with open('balance_storage_test.txt','r') as bs:
                transactions = bs.readlines()
                amt = 0
                for line in transactions:
                    line = float(line)
                    amt += line
                print('Your current balance is ${0:.2f}.'.format(amt))
                exit = True



        # recording a withdraw
        elif user_action == '2':
            user_input = input('How much would you like to withdraw? ')
            
            with open('balance_storage_test.txt','a') as bs:
                bs.write('\n')
                withdraw = '-' + user_input
                bs.write(withdraw)
                exit = True


        # recording a deposit
        elif user_action == '3':
            user_input = input('How much would you like to deposit? ')
            with open('balance_storage_test.txt','a') as bs:
                bs.write('\n')
                bs.write(user_input)
                exit = True
        elif user_action == '4':
            print('Thanks, have a great day!')
            exit = True