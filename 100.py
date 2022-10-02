import sys
import os
import time
import random
import datetime
import getpass

class Bank:
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin
        self.balance = 1000

    def getbalance(self):
        print("Your balance is: ", self.balance)

    def withdraw(self):
        print("Your current balance is: ", self.balance)
        money = float(input("How much money would you like to withdraw? "))
        if money > self.balance:
            print("You do not have enough money.")
        else:
            self.balance -= money
            print("You withdrew: ", money)
            print("Your new balance is: ", self.balance)

    def deposit(self):
        print("Your current balance is: ", self.balance)
        money = float(input("How much money would you like to deposit? "))
        self.balance += money
        print("You deposited: ", money)
        print("Your new balance is: ", self.balance)

    def exit(self):
        print("Thank you for using our bank. Have a nice day!")
        sys.exit()

class ATM:
    def __init__(self):
        self.card = None
        self.pin = None
        self.balance = None
        self.bank = None

    def insertcard(self):
        self.card = input("Please enter your card number: ")
        self.pin = input("Please enter your pin: ")
        self.bank = Bank(self.card, self.pin)

    def menu(self):
        print("Welcome to the ATM. Please select an option.")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.bank.getbalance()
        elif choice == "2":
            self.bank.withdraw()
        elif choice == "3":
            self.bank.deposit()
        elif choice == "4":
            self.bank.exit()
        else:
            print("Invalid choice. Please try again.")
            self.menu()

    def run(self):
        self.insertcard()
        self.menu()

if __name__ == "__main__":
    atm = ATM()
    atm.run()