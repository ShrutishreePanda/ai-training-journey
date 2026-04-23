import math
import random
from datetime import datetime

def math_operations():
    num = float(input("\nEnter a number: "))
    print("Square root:", math.sqrt(num))


def random_operation():
    print("Random number:", random.randint(1, 100))


def statistics_operation():
    numbers = list(map(int, input("\nEnter numbers (space-separated): ").split()))
    
    if len(numbers) == 0:
        print("No numbers entered")
        return
    
    mean = sum(numbers) / len(numbers)
    print("Mean:", mean)


def probability_operation():
    total = int(input("\nEnter total outcomes: "))
    favorable = int(input("Enter favorable outcomes: "))
    
    if total == 0:
        print("Total outcomes cannot be zero")
        return
    
    prob = favorable / total
    print("Probability:", prob)


def show_time():
    print("\nCurrent time:", datetime.now())


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Square Root (Math)")
        print("2. Random Number")
        print("3. Mean (Statistics)")
        print("4. Probability")
        print("5. Current Time")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            math_operations()
        elif choice == "2":
            random_operation()
        elif choice == "3":
            statistics_operation()
        elif choice == "4":
            probability_operation()
        elif choice == "5":
            show_time()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()