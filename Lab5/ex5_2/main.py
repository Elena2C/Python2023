class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.04):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} added to the account. New balance: ${self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, negative_limit=200):
        super().__init__(account_number, balance)
        self.negative_limit = negative_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.negative_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or negative limit exceeded.")


# Example usage:
savings_account = SavingsAccount("SA123", 1000)
savings_account.deposit(500)
savings_account.calculate_interest()
savings_account.withdraw(300)

checking_account = CheckingAccount("CA456", 500, 200)
checking_account.deposit(200)
checking_account.withdraw(700)
checking_account.withdraw(200)
checking_account.withdraw(100)
