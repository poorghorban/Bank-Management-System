import os , time
from data import ListUsers , ListEmployees , ListBanks , ListAccountsType , ListBanksName
from Employee import Employee 
from User import User 
from Account import Account
from Lottery import Lottery
from datetime import datetime
from colorama import init
from termcolor import colored


# Main Menu
def main_menu():
    #clear screen
    os.system('cls')

    #title menu 
    print(colored('\t\t************************************************', 'white'))
    print(colored('\t\t************************************************', 'white'))
    print(colored('\t\t************************************************', 'white'))
    print(colored('\t\t************','white'),colored('BANK MANAGEMENT SYSTEM' , 'green'),colored('************', 'white'))
    print(colored('\t\t**','white'),colored('OPERATIONS MANAGEMENT OF ALL IRANIAN BANKS','green'),colored('**', 'white'))
    print(colored('\t\t************************************************', 'white'))
    print(colored('\t\t************************************************', 'white'))
    print(colored('\t\t************************************************', 'white'))

    print('\n\n')
    print('1)Login User')
    print('2)Login Employee')
    print(colored('e)Exit' ,'magenta'))
    print('\n')

# Login User 
def login_user():
    #clear screen
    os.system('cls')

    # title Login page
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t*****************','white'),colored('LOGIN USER','green'),colored('*******************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    NC = input('Please,Enter your national code:').strip()
    user = None

    # check exists User with national code 
    if NC in ListUsers.keys():
        user = ListUsers[NC]

    return user

# Login Employee 
def login_employee():
    #clear screen
    os.system('cls')

    # title Login page
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t***************','white'),colored('LOGIN EMPLOYEE','green'),colored('*****************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    NC = input('Please,Enter your national code:').strip()
    employee = None
    # check exists employee with national code 
    if NC in ListEmployees.keys():
        employee = ListEmployees[NC]

    return employee

# Menu User Panel 
def user_panel_menu(userName):
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t*****************','white'),colored('USER PANEL','green'),colored('*******************','white'))
    print(colored('\t\t************','white'),colored('WELCOME '+ userName.upper(),'green'),colored('**************','white'))
    print(colored('\t\t************************************************','white'))
        
    print('\n\n')
    print(colored('LIST OF BANKING OPERATIONS:', 'yellow'))
    print('1)Deposit To Account')
    print('2)Withdraw From  Account')
    print('3)Balance Account')
    print('4)Show List Of Accounts')
    print('5)Show Account Transactions')
    print(colored('b)back','magenta'))
    print('\n')

# Menu Employee Bank Panel 
def employee_panel_menu(employeeName):
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t***************','white'),colored('EMPLOYEE PANEL','green'),colored('*****************','white'))
    print(colored('\t\t************','white'),colored('WELCOME '+employeeName.upper(),'green'),colored('**************','white'))
    print(colored('\t\t************************************************','white'))
        
    print('\n\n')
    print(colored('LIST OF BANKING OPERATIONS:','yellow'))
    print('1)Create Account')
    print('2)Delete Account')
    print('3)Show User Accounts')
    print('4)Show Bank Turnover')
    print('5)Lottery')
    print(colored('b)back','magenta'))
    print('\n')

# Create Account
def create_account():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t***************','white'),colored('CREATE ACCOUNT','green'),colored('*****************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    NC = input('Please, Enter the national user code:').strip()

    # Check that the entered national code is 10 digits
    if len(NC) != 10 :
        # Error
        print('\n') 
        print(colored('ERROR:This is not a 10-digit deduction','red'))
        print('\n') 
        return 
    
    # check exists user with national code (Already had an account at this bank)
    user = User.get_user_by_nationalCode(NC)

    # If there is no user create new user
    if user == None:
        # get user profile
        print('\n')
        print(colored('User Information:','yellow'))
        firstname = input("Please, Enter your user'sfirstname:")
        lastname = input("Please, Enter your user's lastname:")

        # create user 
        user = User(firstname , lastname , NC)
        # add user to ListUsers

        ListUsers[user.getNationalCode()] = user

    
    # show list banks 
    print('\n')
    print(colored('Bank Account Information','yellow'))
    print(colored('Banks:','yellow'))
    for index_bank , bank in enumerate(ListBanksName):
        print(colored(str(index_bank+1) + '-' + bank +' ', 'cyan') , end = '')
    print('\n')
        
    print(colored('Accounts Type:' , 'yellow'))
    for index_account , type_acc in enumerate(ListAccountsType , start=0):
        print(colored(str(index_account+1) + '-' + type_acc+' ','cyan'), end='')
    print('\n')

    # get number of bank
    n_bank = int(input('Please, Enter your desired bank number from the list above:').strip())

    # get number of account type
    n_t_account = int(input('Please, Enter your account type number from the list above:').strip())

    #get balance for account
    balance = float(input('Please, Enter the amount you wish to deposit into your account:').strip())

    # create new account 
    flag , info = user.create_account(ListBanksName[n_bank-1] , ListAccountsType[n_t_account-1] , float(balance))

    if flag:
        # message 
        print('\n')
        print(colored('Account Number : ' + str(info),'green'))
        print(colored('SUCCESS:Account creation successful!!!','green'))
        print('\n')
    else:
        # Error 
        print('\n')
        print(colored('ERROR:' + info,'red'))
        print('\n')

# Delete Account
def delete_account():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t****************','white'),colored('DELETE ACCOUNT','green'),colored('****************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    account_number = input("Please,Enter the user's account number:").strip()

    # check the account number is 16 digits
    if len(account_number) != 16:
        # Error 
        print('\n')
        print(colored('ERROR:This is not a 16-digit deduction','red'))
        print('\n')
        return

    flag , info = User.delete_account(account_number)

    if flag : 
        print('\n')
        print(colored('SUCCESS:' + info , 'green'))
        print('\n')
    else:
        # Error
        print('\n') 
        print(colored('ERROR:' + info,'red'))
        print('\n')

# Deposit To Account
def deposit_to_account():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************' , 'white'))
    print(colored('\t\t*************','white'),colored('DEPOSIT TO ACCOUNT','green'),colored('***************','white'))
    print(colored('\t\t************************************************' , 'white'))

    print('\n\n')
    account_number = input("Please,Enter the  account number:").strip()
    balance = float(input('Please, Enter the amount you wish to deposit into your account:').strip())

    # check the account number is 16 digits
    if len(account_number) != 16:
        # Error 
        print('\n')
        print(colored('ERROR:This is not a 16-digit deduction','red'))
        print('\n')
        return

    account = Account.get_account_by_id(account_number)

    # check that there is an account with this number.
    if account != None:
        flag , sum_balance , id_transaction = account.deposit_to_account(balance)
        
        # message 
        print('\n')
        print(colored('Transaction number:' + str(id_transaction),'green'))
        print(colored('Balance : ' + str(sum_balance),'green'))
        print(colored('SUCCESS:Deposit to account successful!!!','green'))
        print('\n')
    else:
        # Error 
        print('\n')
        print(colored('ERROR:There is no account with this number!!!','red'))
        print('\n')
        
# Withdraw From Account
def withdraw_from_account():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t************','white'),colored('WITHDRAW FROM ACCOUNT','green'),colored('*************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    account_number = input("Please,Enter the account number:").strip()
    balance = float(input('Please, Enter the amount you wish to withdraw from your account:').strip())

    # check the account number is 16 digits
    if len(account_number) != 16:
        # Error 
        print('\n')
        print(colored('ERROR:This is not a 16-digit deduction','red'))
        print('\n') 
        return

    account = Account.get_account_by_id(account_number)

    # check that there is an account with this number.
    if account != None:
        flag , info , id_transaction = account.withdraw_from_account(balance)

        if flag :
            # message 
            print('\n')
            print(colored('Transaction number:' + str(id_transaction),'green'))
            print(colored('Balance : ' + str(info),'green'))
            print(colored('SUCCESS:Withdraw from account successful!!!','green'))
            print('\n')
        else:
            # Error 
            print('\n')
            print(colored('ERROR:' + info,'red'))
            print('\n')
    else:
        # Error
        print('\n') 
        print(colored('ERROR:There is no account with this number!!!','red'))
        print('\n')

# Show Balance Account 
def show_balance_account():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t*************','white'),colored('SHOW BALANCE ACCOUNT','green'),colored('*************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    account_number = input("Please,Enter the  account number:").strip()

    # check the account number is 16 digits
    if len(account_number) != 16:
        # Error 
        print('\n')
        print(colored('ERROR:This is not a 16-digit deduction','red'))
        print('\n') 
        return
    
    account = Account.get_account_by_id(account_number)

    # check that there is an account with this number.
    if account != None:
        print('\n')
        print('Balance Account With Number' + str(account.getId()) + ': ' + str(account.getBalance()))
        print('\n')
    else:
        # Error 
        print('\n')
        print(colored('ERROR:There is no account with this number!!!','red'))
        print('\n')

# Show List Account for User
def show_list_account_user(user):
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t***********','white'),colored('SHOW LIST ACCOUNTS USER','green'),colored('************' , 'white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    
    # get list account user 
    list_account = user.get_list_account()

    if len(list_account) == 0 :
        # Error 
        print('\n')
        print(colored('ERROR:There is no accounts !!!','red'))
        print('\n')
        return 
    else:
        print('\n')
        for account in list_account:
            print(account)
        print('\n')

# Show List Transactions For Account By Date Transaction
def show_list_transactions_by_date_user():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t************','white'),colored('SHOW LIST TRANSACTIONS','green'),colored('************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    account_number = input("Please,Enter the  account number:").strip()
    date = input('Please,Enter date with format YYYY-MM-DD:')

    # check the account number is 16 digits
    if len(account_number) != 16:
        # Error 
        print('\n')
        print(colored('ERROR:This is not a 16-digit deduction','red'))
        print('\n')
        return

    account = Account.get_account_by_id(account_number)
    if account != None:
        print('\n')
        list_transactions_by_date = Account.get_transactions_by_date(account.getNameBank() , date)
        if len(list_transactions_by_date) != 0:
            for transaction in list_transactions_by_date:
                if transaction.getIdAccount() == account_number:
                    print(transaction)
        else:
            # Error
            print('\n')
            print(colored('ERROR:There is no transaction for this date!!!','red'))
            print('\n')
    else:
        # Error 
        print('\n')
        print(colored('ERROR:There is no account for this account number!!!','red'))
        print('\n')

# Show Information User By Account Type
def show_information_user_by_account_type():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t****','white'),colored('SHOW INFORMATION USER BY ACCOUNT TYPE','green'),colored('*****','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    # show list banks 
    print(colored('Bank Account Information','yellow'))
    print(colored('Banks:','yellow'))
    for index_bank , bank in enumerate(ListBanksName):
        print(colored(str(index_bank+1) + '-' + bank+' ','cyan'), end='')
    print('\n')

    # get number of bank
    n_bank = int(input('Please, Enter your desired bank number from the list above:').strip())

    # get list account type bank
    list_typeAccount = ListBanks[ListBanksName[n_bank-1]].getListOfTypeAccount()

    print('\n')
    for typeAccount in list_typeAccount:
        # get list account by account type
        list_account_by_bankName_accountType = Account.get_list_account_by_bankName_accountType(ListBanksName[n_bank-1] , typeAccount)

        if len(list_account_by_bankName_accountType) != 0:
            print(typeAccount + ':')
            for account in list_account_by_bankName_accountType:
                print(account)
            print('\n')
 
# Show All Transactions By Date 
def show_all_transactions_by_date_employee():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t************','white'),colored('SHOW All TRANSACTIONS','green'),colored('*************','white'))
    print(colored('\t\t************************************************','white'))

    print('\n\n')
    print(colored('Banks:','yellow'))
    for index_bank , bank in enumerate(ListBanksName):
        print(colored(str(index_bank+1) + '-' + bank+' ','cyan'), end='')
    print('\n')

    # get number of bank
    n_bank = int(input('Please, Enter your desired bank number from the list above:').strip())
    date = input('Please,Enter date with format YYYY-MM-DD:')

    list_transactions = Account.get_transactions_by_date(ListBanksName[n_bank -1] , date)

    if len(list_transactions) != 0 :
        print('\n')
        for transaction in list_transactions:
            print(transaction.getIdAccount() , transaction)
        print('\n')
    else:
        # Error 
        print('\n')
        print(colored('ERROR:There is no transactions!!!','red'))
        print('\n')
     
# Draw between accounts by account type and bank
def draw_accounts_by_account_type_and_bank():
    # clear screen
    os.system('cls')

    # title menu user panel 
    print(colored('\t\t************************************************','white'))
    print(colored('\t\t*******************','white'),colored('LOTTERY','green'),colored('********************','white'))
    print(colored('\t\t************************************************','white')) 

    # show list banks 
    print('\n\n')
    print(colored('Banks:','yellow'))
    for index_bank , bank in enumerate(ListBanksName):
        print(colored(str(index_bank+1) + '-' + bank +' ','cyan') , end='')
    print('\n')
        
    print(colored('Accounts Type:','yellow'))
    for index_account , type_acc in enumerate(ListAccountsType , start=0):
        print(colored(str(index_account+1) + '-' + type_acc+' ','cyan') , end='')
    print('\n')

    # get number of bank
    n_bank = int(input('Please, Enter your desired bank number from the list above:').strip())

    # get number of account type
    n_t_account = int(input('Please, Enter your account type number from the list above:').strip())

    # get prize
    prize = float(input('Please,Enter the prize(amount of money):'))

    # get number of lottery
    n_lottery =int(input('Please Enter the lottery number:'))
    print('\n')
    nameBank = ListBanksName[n_bank-1]
    typeAccount = ListAccountsType[n_t_account-1]

    # create lottery (instance of class lottery)
    lottery = Lottery(nameBank , n_lottery , typeAccount , prize , str(datetime.today()))

    # add lottery to list bank
    ListBanks[nameBank].add_Lottery(lottery)

    # get list accounts with this bank and this account type
    list_accounts_by_nameBank_and_typeAccount = Account.get_list_account_by_bankName_accountType(nameBank , typeAccount)

    if len(list_accounts_by_nameBank_and_typeAccount) != 0 :
        if n_lottery < len(list_accounts_by_nameBank_and_typeAccount):
            # Error 
            print('\n')
            print(colored('ERROR:The number of accounts is less than the number of draws!!!','red'))
            print('\n')
        else:
            # get list account winner
            list_accounts_winner= lottery.get_list_winners_in_draw(list_accounts_by_nameBank_and_typeAccount)

            # deposit prize to balance account 
            for account in list_accounts_winner:
                account.deposit_to_account(prize)

            # Show the winner's name and account number
            for index , account in enumerate(list_accounts_winner):
                user = User.get_user_by_nationalCode(account.getNationalCodeUser())
                print((index+1), ':', user.getFirstName() , user.getLastName() , '\t' , account.getId() )
    else:
        # Error 
        print('\n')
        print(colored('ERROR:There is no acounts!!!','red'))
        print('\n')


if __name__ == "__main__":

    ## add data to lists for run 
    import file

    # run color text 
    init()

    # choice option menu
    choice_option_main_menu = ''

    while True:
        #show main menu 
        main_menu()
        
        #get the selected option from the menu 
        choice_option_main_menu = input('Please,Enter your choice or exit:')

        if choice_option_main_menu == '1':
            while True:
                user = login_user()
                #check exist user 
                if user != None:

                    # choice option from menu user panel
                    choice_option_banking_operations_user = ''

                    while True:
                        user_panel_menu(user.getLastName())

                        #get the selected option from menu user panel 
                        choice_option_banking_operations_user  = input('Please,Enter your choice or back:')

                        if choice_option_banking_operations_user == '1':
                            while True:
                                deposit_to_account()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '2':
                            while True:
                                withdraw_from_account()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '3':
                            while True:
                                show_balance_account()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '4':
                            while True:
                                show_list_account_user(user)
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '5':
                            while True:
                                show_list_transactions_by_date_user()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == 'b' or choice_option_banking_operations_user == 'B':
                            break
                        else:
                            # Error 
                            print('\n')
                            print(colored('ERROR:The number entered does not belong to a menu option!!!','red'))
                            print('\n')
                            time.sleep(5)
                                
                    # for back to main menu, no show login page
                    break
                else:
                    # Error 
                    print('\n')
                    print(colored('ERROR:There is no user with the national code!!!','red'))
                    print('\n')
                    
                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                c = input()
                if c == 'b' or c == 'B':
                    break

        elif choice_option_main_menu == '2':
            while True:
                employee = login_employee()
                #check exist employee 
                if employee != None:

                    # choice option from menu user panel
                    choice_option_banking_operations_employee = ''

                    while True:
                        employee_panel_menu(employee.getLastName())

                        #get the selected option from menu user panel 
                        choice_option_banking_operations_user  = input('Please,Enter your choice or back:')

                        if choice_option_banking_operations_user == '1':
                            while True:
                                create_account()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break 
                        elif choice_option_banking_operations_user == '2':
                            while True:
                                delete_account()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '3':
                            while True:
                                show_information_user_by_account_type()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '4':
                            while True:
                                show_all_transactions_by_date_employee()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == '5':
                            while True:
                                draw_accounts_by_account_type_and_bank()
                                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                                c = input()
                                if c == 'b' or c == 'B':
                                    break
                        elif choice_option_banking_operations_user == 'b' or choice_option_banking_operations_user == 'B':
                            break
                        else:
                            # Error 
                            print('\n')
                            print(colored('ERROR:The number entered does not belong to a menu option!!!','red'))
                            print('\n')
                            time.sleep(5)

                    # for back to main menu, no show login page
                    break
                else:
                    # Error 
                    print('\n')
                    print(colored('ERROR:There is no employee with the national code!!!','red'))
                    print('\n')
                    
                print(colored("Enter 'b' to back previous page or 'r' to refresh page:",'magenta'),end='')
                c = input()
                if c == 'b' or c == 'B':
                    break

        elif choice_option_main_menu == 'e':
            exit()
        else:
            # Error 
            print('\n')
            print(colored('ERROR:The number entered does not belong to a menu option!!!','red'))
            print('\n')
            time.sleep(5)
