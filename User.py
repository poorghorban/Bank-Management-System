from Account import Account 
from data import ListBanks , ListUsers

class User():

    def __init__(self , firstname , lastname , nationalCode):
        self.firstName = firstname 
        self.lastName = lastname
        self.nationalCode = nationalCode
        self.ListOfIdAccount = []

    def getNationalCode(self):
        return self.nationalCode

    def getFirstName(self):
        return self.firstName
        
    def getLastName(self):
        return self.lastName
    
    def add_idAccount(self , id):
        self.ListOfIdAccount.append(id)
    
    def delete_idAccount(self , id):
        self.ListOfIdAccount.remove(id)

    def create_account(self , nameBank , typeAccount , balance):

        # Check that the user has this type of account in this bank.
        # 1) convert nameBank and typeAccount to binary.
        # 2) exists this account to ListOfIdAccount.

        # If there are accounts in this bank and this type of account is True and if not False.
        Flag = False

        binaryBank , binaryAccount = Account.convert_to_Binary(nameBank , typeAccount)

        if len(self.ListOfIdAccount) != 0 :
            for account in self.ListOfIdAccount:
                if (binaryBank + binaryAccount) == account[1:7]:
                    Flag = True 
                    break
        
        if Flag:
            return False , 'This type of account exists'
        else:

            # Check that the bank has this type of account
            # If there is type of account in this bank create account and if not return error 

            bank = ListBanks[nameBank]
            Flag = bank.contain_typeAccount(typeAccount)

            if Flag:
                # create account
                account = Account(nameBank , typeAccount , self.nationalCode)

                # deposit balance to account
                account.deposit_to_account(balance)

                # add id new account to ListOfIdAccount
                self.add_idAccount(account.getId())

                # add account to ListOfAccounts bank
                bank.add_account(account)

                return True , account.getId()
            else:
                return False , 'The bank does not support this type of account.'

    def get_list_account(self):
        list_account = []

        for id in self.ListOfIdAccount:
            list_account.append(Account.get_account_by_id(id))
        
        return list_account
        
    @staticmethod 
    def delete_account(id):
        
        # Check that there is an account with this number.
        account = Account.get_account_by_id(id)

        if account != None:
            # Remove account number from user accounts list
            user = User.get_user_by_nationalCode(account.getNationalCodeUser())
            user.delete_idAccount(account.getId())


            # Remove Account from Bank
            bank = ListBanks[account.getNameBank()]
            bank.delete_account(account.getId() , account.getListOfIdTransactions())
            return True , 'Account deleted!!!'
        else:
            return False , 'There is no account with this number!!!'

    @staticmethod
    def get_user_by_nationalCode(nationalCode):
        user = None 
        if nationalCode in ListUsers.keys():
            user = ListUsers[nationalCode]

        return user