from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Classes
class UPI(Payment):
    def pay(self, amount):
        upi_id = input("Enter UPI ID: ")
        print(f"Processing UPI payment of ₹{amount} from {upi_id}...")


class Card(Payment):
    def pay(self, amount):
        card_number = input("Enter Card Number: ")
        print(f"Processing Card payment of ₹{amount} using card {card_number[-4:]}...")


class Cash(Payment):
    def pay(self, amount):
        print(f"Processing Cash payment of ₹{amount}...")

def main():
    print("Select Payment Method:")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    choice = input("Enter choice: ")
    amount = float(input("Enter amount: "))

    if choice == "1":
        payment = UPI()
    elif choice == "2":
        payment = Card()
    elif choice == "3":
        payment = Cash()
    else:
        print("Invalid choice")
        return

    payment.pay(amount)

main()