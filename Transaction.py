import random

class Transaction():

    def __init__(self , typeTransaction , balance , datetime , idAccount):
        self.typeTransaction = typeTransaction
        self.balance = balance
        self.datetime = datetime
        self.id = self.setId()
        self.idAccount = idAccount

    def __str__(self):
        return  (str(self.id) +'\t' + self.typeTransaction +'\t'+ self.datetime + '\t'+ str(self.balance))

    def setId(self):
        return random.randint(10000,100000)
    def getDatetime(self):
        return self.datetime
    def getBalance(self):
        return self.balance
    def getTypeTransaction(self):
        return self.typeTransaction
    def getId(self):
        return self.id
    def getIdAccount(self):
        return self.idAccount