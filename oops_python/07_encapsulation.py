# Encapsulation example

class Account:
    def __init__(self):
        self.__balance = 5000   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

acc = Account()
acc.show_balance()
