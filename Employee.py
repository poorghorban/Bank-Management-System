

class Employee():

    def __init__(self , firstname , lastname , nationalCode):
        self.firstName = firstname 
        self.lastName = lastname
        self.nationalCode = nationalCode

    def getNationalCode(self):
        return self.nationalCode

    def getLastName(self):
        return self.lastName
    