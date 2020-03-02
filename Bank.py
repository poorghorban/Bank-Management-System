

class Bank():

    def __init__(self,nameBank , listOfTypeAccount ):
        self.nameBank = nameBank
        self.ListOfTypeAccount = listOfTypeAccount
        self.ListOfAccounts = {}
        self.ListOfTransactions = {}
        self.ListOfWinnersInDraw = []

    def getNameBank(self):
        return self.nameBank

    def getListOfAccounts(self):
        return self.ListOfAccounts
    
    def getListOfTransactions(self):
        return self.ListOfTransactions

    def getListOfTypeAccount(self):
        return self.ListOfTypeAccount
    
    def getListOfWinnersInDraw(self):
        return self.ListOfWinnersInDraw

    def contain_typeAccount(self , typeAccount):
        flag = False 

        if len(self.ListOfTypeAccount) != 0 :
            for ta in self.ListOfTypeAccount:
                if ta == typeAccount:
                    flag = True 
                    break 

        return flag

    def add_account(self, account):
        self.ListOfAccounts[account.getId()] = account

    def get_account_by_id(self , id):
        if id in self.ListOfAccounts.keys():
            return self.ListOfAccounts[id]
        else:
           return None

    def delete_account(self , id , list_transactions):
        for id_transactions in list_transactions:
            self.ListOfTransactions.pop(id_transactions)

        self.ListOfAccounts.pop(id)

    def add_transaction(self , transaction):
        self.ListOfTransactions[transaction.getId()] = transaction
    
    def add_Lottery(self , Lottery):
        self.ListOfWinnersInDraw.append(Lottery)
