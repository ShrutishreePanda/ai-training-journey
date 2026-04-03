#Encapsulation

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.name}'s Balance: {self.__balance}")

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

acc = BankAccount(name, balance)

choice = input("Enter operation (deposit/withdraw): ")
amount = float(input("Enter amount: "))

if choice == "deposit":
    acc.deposit(amount)
elif choice == "withdraw":
    acc.withdraw(amount)

acc.show_balance()