# ============================================================
# ABSTRACTION
# ============================================================
# 1. Abstract Class
# 2. Abstract Method
# 3. Concrete Method

from abc import ABC, abstractmethod


# ============================================================
# 1. BASIC ABSTRACTION EXAMPLE
# ============================================================

class Payment(ABC):

    def dashboard(self):
        print("Welcome to dashboard")

    @abstractmethod
    def login(self):
        pass


class User(Payment):

    def login(self):
        print("Login successful")


obj = User()

obj.login()
obj.dashboard()


# ============================================================
# 2. ABSTRACT CLASS WITH SENSITIVE INFORMATION
# ============================================================

class Account(ABC):

    def sensitive_information(self):
        print("Sensitive information")

    @abstractmethod
    def login(self):
        pass


class Verify(Account):

    def login(self):
        print("Login successful")


obj = Verify()

obj.login()
obj.sensitive_information()


# ============================================================
# 3. PAYMENT SYSTEM USING ABSTRACTION
# ============================================================

class Payment(ABC):

    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    @abstractmethod
    def process_payment(self, amount):
        pass

    def show_balance(self):
        print(f"Your balance is ₹{self.balance}")

    def show_history(self):
        print("Payment History:")

        for amount in self.history:
            print(f"₹{amount}")


# ============================================================
# 4. PHONEPE PAYMENT
# ============================================================

class PhonePe(Payment):

    def process_payment(self, amount):
        print("PhonePe payment processing...")

        if amount > 0:
            self.balance += amount
            self.history.append(amount)
            print("Payment successful")
        else:
            print("Invalid amount")


# ============================================================
# 5. GOOGLE PAY PAYMENT
# ============================================================

class GooglePay(Payment):

    def process_payment(self, amount):
        print("Google Pay payment processing...")

        if amount > 0:
            self.balance += amount
            self.history.append(amount)
            print("Payment successful")
        else:
            print("Invalid amount")


# ============================================================
# OBJECT CREATION
# ============================================================

google_pay = GooglePay()

google_pay.show_balance()
google_pay.process_payment(200)
google_pay.show_balance()
google_pay.show_history()