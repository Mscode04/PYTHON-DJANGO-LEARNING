# . write program defines a BankAccount class with methods for deposit, withdrawal, and checking the account balance

class Accounts:
    def __init__(self,Acno,Name,balence=0):
        self.Acno=Acno
        self.Name=Name
        self.balence=balence
    def details(self):
        print(f'Account No is : {self.Acno} Banlence : {self.balence}')    
class Deposit(Accounts): 
    def  deposit(self,DpAmount):
        self.DpAmount=DpAmount
        self.balence=DpAmount
        print('Amount Deposited')
class Withdrawal(Deposit): 
    def  withdrawal(self,WdAmount):
        self.DpAmount=WdAmount
        self.balence=self.balence-WdAmount
        print('Amount withdrawed')
        
obj=Withdrawal('123','Shaheen',0)
obj.details()
obj.deposit(1000)
obj.details()
obj.withdrawal(500)
obj.details()

