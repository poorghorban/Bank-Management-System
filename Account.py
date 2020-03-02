from data import ListBanksName , ListAccountsType , ListBinaryAccountsType , ListBinaryBanksName , ListBanks
from Transaction import Transaction
import random 
from datetime import datetime

class Account():

    def __init__(self , nameBank , typeAccount , nationalCodeUser):
        self.nameBank = nameBank
        self.typeAccount = typeAccount
        self.nationalCodeUser = nationalCodeUser
        self.balance = 0.0
        self.ListOfIdTransactions = []

        self.id = self.setId(nameBank , typeAccount)

    def __str__(self):
        return (str(self.id) + '\t' + self.nameBank + '\t' + str(self.balance))

    def setId(self , nameBank , typeAccount):

        # Saved first digit
        id = '1'

        # 4 digits representing bank and 2 digits representing account type
        binaryBank , binaryAccount = self.convert_to_Binary(nameBank , typeAccount)

        # account number is 16 digits 
        # 1 digit saved 
        # 4 digits representing bank
        # 2 digits representing account type
        # 9 digits random 
        rand_9_digit = random.randint(100000000,1000000000-1)
        
        id = id + binaryBank + binaryAccount + str(rand_9_digit)

        return id

    def getId(self):
        return self.id

    def getNationalCodeUser(self):
        return self.nationalCodeUser

    def getNameBank(self):
        return self.nameBank

    def getBalance(self):
        return self.balance

    def getListOfIdTransactions(self):
        return self.ListOfIdTransactions

    def deposit_to_account(self,balance):
        self.balance += balance
        id_transaction = self.add_id_transaction('deposit' , balance , str(datetime.today()).split('.')[0] , self.id)
        return True , self.balance , id_transaction
    
    def withdraw_from_account(self,balance):
        # check balance
        if self.balance > balance:
            self.balance -= balance
            id_transaction = self.add_id_transaction('withdraw' , balance , str(datetime.today()).split('.')[0] , self.id)
            return True , self.balance , id_transaction
        else:
            return False , 'Your account balance is insufficient!!!' , 0

    def add_id_transaction(self , typeTransaction , balance , datetime , id):
        t = Transaction(typeTransaction , balance , datetime , id)
        ListBanks[self.nameBank].add_transaction(t)
        self.ListOfIdTransactions.append(t.getId())
        return t.getId()

    @staticmethod
    def get_transactions_by_date(nameBank, date):
        transactions_by_date = []

        for key , transaction  in ListBanks[nameBank].getListOfTransactions().items():
            if transaction.getDatetime().split(' ')[0] == date:
                transactions_by_date.append(transaction)

        return transactions_by_date

    @staticmethod
    def get_account_by_id(id):

        indexBankName = -1
        bankName = ''
        account = None
        # Check that there are 4 digits representing the bank in the binary tuple of the bank name
        for index , binaryBankName in enumerate(ListBinaryBanksName):
            if binaryBankName == id[1:5]:
                indexBankName = index
                break
                
        if indexBankName != -1:
            bankName = ListBanksName[indexBankName]
            bank = ListBanks[bankName]
            account = bank.get_account_by_id(id)  
        return account
        
    @staticmethod 
    def get_list_account_by_bankName_accountType(nameBank , typeAccount):
        binaryBank , binaryAccount = Account.convert_to_Binary(nameBank , typeAccount)

        list_account_by_bankName_accountType = []

        list_accounts = ListBanks[nameBank].getListOfAccounts()

        for account_number in list_accounts.keys():
            if binaryBank + binaryAccount == account_number[1:7]:
                list_account_by_bankName_accountType.append(list_accounts[account_number])

        return list_account_by_bankName_accountType

    @staticmethod 
    def convert_to_Binary(nameBank , typeAccount):

        binaryBank = ''
        binaryAccount = ''
        #convert binary bank
        for index , bank in enumerate(ListBanksName):
            if bank == nameBank:
                binaryBank = ListBinaryBanksName[index]
                break

        #convert binary account
        for index , account in enumerate(ListAccountsType):
            if account == typeAccount:
                binaryAccount = ListBinaryAccountsType[index]
                break

        return binaryBank , binaryAccount
