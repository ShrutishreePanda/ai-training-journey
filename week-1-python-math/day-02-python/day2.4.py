#polymorphism

class Payment:
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

method = input("Enter payment method (upi/card): ").lower()
amount = float(input("Enter amount: "))

if method == "upi":
    p = UPI()
elif method == "card":
    p = Card()
else:
    print("Invalid method")
    exit()

p.pay(amount)