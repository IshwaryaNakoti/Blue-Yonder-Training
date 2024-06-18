from datetime import date
class Person:
    def __init__(self, name, dob, country) -> None:
        self.name = name
        self.dob = dob
        self.country = country

    def calculate_age(self):
        self.dob = self.dob.split('-')
        self.dob = [int(i) for i in self.dob]
        today = date.today()
        age = today.year - self.dob[0]
        if (today.month, today.day) < (self.dob[1], self.dob[2]):
            age -= 1
        return age 

class Bank:
    def __init__(self) -> None:
        self.name = ""
        self.balance = 0
        self.email = ""
        self.password = ""
    
    def create_account(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email address : ")
        self.password = input("Enter your password : ")
        print(f"Hey {self.name}! Your account has been created!")
    
    def make_deposit(self):
        if self.name and self.email and self.password:
            amount = int(input("Enter how much amount you want to deposit: "))
            self.balance = amount
            print(f"Hi {self.name},\n an amount of Rs. {self.balance} has been deposited into your account.\nEmail linked: {self.email}")
        else:
            print("Please create an account first\nPress 1 to create a user account")
    
    def make_withdrawal(self):
        if self.balance:
            amount = int(input("How much money would you like to withdraw ? : "))
            self.balance -= amount
        else:
            print(f"Hello {self.name},\nYour balance is Zero.\nPress 2 to make a deposit.")
    
    def check_balance(self):
        if self.name:
            print(f"Hi {self.name}!\nYour available balance is : Rs.{self.balance}")
        else:
            print("User account not found.\nPress 1 to create an account.")

class ShoppingCart:
    def __init__(self) -> None:
        self.cart = {}

    def add_items(self):
        name = input("Enter name of the item: ")
        price = int(input("Enter price: "))
        self.cart[name] = price
        print("Yay!\nItem added into yout cart!\n")
        print(self.cart)
    
    def remove_items(self):
        if self.cart:
            print(f"Your cart:\n{self.cart}")
            name = input("Enter the name of the item you want to delete: ")
            del self.cart[name]
            print("Item deleted from your dictionary")
            print(f"Cart items = {self.cart}")
        else:
            print("Your cart is emplty.\nPress 1 to add items inot your cart")
    
    def total_amount(self):
        if self.cart:
            total = 0
            for v in self.cart.values():
                total += v
            print(f"Total amount = {total}")
        else:
            print("No items in the cart!")

def one():
    name = input("Enter your name: ")
    dob = input("Enter dob in \'yyyy-mm-dd\' format : ")
    country = input("Enter country name: ")
    person = Person(name, dob, country)
    print(f"Name = {name}\nCountry = {country}\nDob = {dob}")
    print("Age = ",person.calculate_age())

def two():
    print("BY Bank")
    print("1. create account")
    print("2. Make deposite")
    print("3. Make withdrawal")
    print("4. Check balance")
    print("5. quit")
    opt = int(input("Enter your choice: "))
    B = Bank()
    while opt != 5:
        if opt == 1 : B.create_account()
        elif opt == 2 : B.make_deposit()
        elif opt == 3 : B.make_withdrawal()
        elif opt == 4 : B.check_balance()
        opt = int(input("Enter 5 to quit\nEnter your choice: "))

def three():
    cart  = ShoppingCart()
    print("BY Bazaar")
    print("1. Add items to your cart")
    print("2. Remove items from your cart")
    print("3. Check total price")
    print("4. quit")
    opt = int(input("Enter your choice: "))
    while opt != 4:
        if opt == 1 : cart.add_items()
        elif opt == 2 : cart.remove_items()
        elif opt == 3 : cart.total_amount()
        opt = int(input("Enter 4 to quit\nEnter your choice: "))

if __name__ == '__main__':
    print("14-06-2024 - Python Training - Blue Yonder Assignment 4:")
    print("Assignments On Classes and objects")
    print("\n1. Determine person's age")
    print("\n2. A class representing a bank - creating an account, make deposit, make withdrawal, check balance")
    print("\n3. Shopping cart")
    print("\n4. Method Overriding - single inheritance ")
    print("\n5. Default values in a constructor")
    print("\n6. Default params in child class")
    print("\n7. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 7:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3 : three()
        # elif n==4 : four()
        # elif n==5 : five()
        # elif n==6 : six()
        n = int(input("\n  Enter a choice: "))