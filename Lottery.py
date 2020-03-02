import random 


class Lottery():
    def __init__(self ,nameBank ,  numberWinner , typeAccount ,Prize ,  datetime):
        self.nameBank = nameBank
        self.numberWinner = numberWinner 
        self.typeAccount = typeAccount
        self.Prize = Prize
        self.datetime = datetime 
        self.ListOfWinners = []

    def get_list_winners_in_draw(self , listAccounts):
        len_list_account = len(listAccounts)

        for i in range(self.numberWinner):
            rand_number = random.randint(0,len_list_account-1)
            nationalCodeWinner = listAccounts[rand_number]
            self.ListOfWinners.append(nationalCodeWinner)

        return self.ListOfWinners

    