class Account:
    def __init__(self, name, acno, balance=0):
        self.name = name
        self.acno = acno
        self.__balance = balance 
        print(f"Account created for {name} (Account No: {acno})")
    
    def __show_balance(self):
        print(f"Current balance: {self.__balance}")

class demo(Account):
    def ket(self):
        print("not")

account1 = Account("Shaheen", "23577", 1000)
account1._show_balance()




