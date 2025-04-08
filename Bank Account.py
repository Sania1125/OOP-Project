Renamed file to .py extension for correct code view
# Step 1–3: BankAccount class with encapsulation

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    def __lt__(self, other):  # Step 6: Operator overloading
        return self.get_balance() < other.get_balance()

# Step 4: Inheritance - SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest applied: {interest}")

# Step 5: Polymorphism - CheckingAccount with limited withdraw
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 500:
            print("Cannot withdraw more than 500 at a time")
        else:
            super().withdraw(amount)

# Step 7: Composition - Bank has multiple accounts
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

# Example usage
if __name__ == "__main__":
    # Bank account operations
    acc1 = BankAccount("Alice", 1000)
    acc1.deposit(200)
    acc1.withdraw(150)
    print("Final balance (Alice):", acc1.get_balance())

    # Savings account with interest
    savings = SavingsAccount("Bob", 2000, 0.05)
    savings.apply_interest()

    # Checking account with withdrawal limit
    checking = CheckingAccount("Charlie", 1500)
    checking.withdraw(600)  # Should print error
    checking.withdraw(300)  # Should work

    # Operator overloading
    acc2 = BankAccount("David", 3000)
    print("Is Alice's account less than David's?", acc1 < acc2)

    # Bank composition
    bank = Bank()
    bank.add_account(acc1)
    bank.add_account(acc2)

