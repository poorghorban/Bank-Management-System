from Employee import Employee 
from User import User 
from Bank import Bank
from data import ListEmployees , ListUsers , ListBanks

# create banks and add to List bank
b1 = Bank('Melli' , ['Savings' , 'Current','Long Term Investments' , 'Short Term Investments'])
b2 = Bank('Mellat' , ['Savings' , 'Current'])
b3 = Bank('Sepah' , ['Savings' , 'Current','Long Term Investments' , 'Short Term Investments'])
b4 = Bank('Industry and Mine' , ['Savings' , 'Current','Long Term Investments' ])
b5 = Bank('Tosee Taavon' , ['Savings' , 'Current','Long Term Investments' , 'Short Term Investments'])
b6 = Bank('Saderat' , ['Savings' , 'Current','Long Term Investments' , 'Short Term Investments'])
b7 = Bank('Keshavarzi' , ['Savings' , 'Current', 'Short Term Investments'])
b8 = Bank('Maskan' , ['Savings' , 'Current','Long Term Investments' , 'Short Term Investments'])
b9 = Bank('Post Bank' , ['Current','Long Term Investments' , 'Short Term Investments'])

ListBanks[b1.getNameBank()] = b1
ListBanks[b2.getNameBank()] = b2
ListBanks[b3.getNameBank()] = b3
ListBanks[b4.getNameBank()] = b4
ListBanks[b5.getNameBank()] = b5
ListBanks[b6.getNameBank()] = b6
ListBanks[b7.getNameBank()] = b7
ListBanks[b8.getNameBank()] = b8
ListBanks[b9.getNameBank()] = b9

# create employees and add to List employees
e1 = Employee('Ali' , 'Mousavi' , '0123456789')
ListEmployees[e1.getNationalCode()] = e1

# create users and add to List users
u1 = User('Ali' , 'Tavakoli' , '9876543210')
u2 = User('Mohammad' , 'Mohammadi' , '9516203847')
u3 = User('Maryam' , 'َlizadeh' , '9638520741')

ListUsers[u1.getNationalCode()] = u1
ListUsers[u2.getNationalCode()] = u2
ListUsers[u3.getNationalCode()] = u3






