from datetime import date

class Bank:
    def __init__(self) -> None:
        self.__bank_balance = 0
        self.users = []
        self.__loan_amount = 0
        self.__loan_feature = True

    def create_account(self, user):
        if user in self.users:
            print("Already has an account with this username.")
        else:
            self.users.append(user)
            self.__bank_balance += user.balance
            print(f"Account for {user.name} created with initial balance {user.balance} taka.")

    def admin_check_balance(self):
        return self.__bank_balance
    
    def admin_check_loan_amount(self):
        return self.__loan_amount

    def admin_loan_feature(self, on):
        self.__loan_feature = on

    def loan_status(self):
        return self.__loan_feature

    def add_to_bank_balance(self, amount):
        self.__bank_balance += amount

    def remove_from_bank_balance(self, amount):
        self.__bank_balance += amount

    def add_to_loan_amount(self, amount):
        self.__loan_amount += amount

class User:
    def __init__(self, name, bank:object, phone_no, email, account_type, initial_balance) -> None:
        self.bank = bank
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.account_type = account_type
        self.balance = initial_balance
        self.history = ""
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} taka deposited.")
        self.bank.add_to_bank_balance(amount)
        self.history += str(date.today()) + "\n" + f"Amount deposited: {amount} taka.\n"

    def withdrawal(self, amount):
        if amount > self.balance:
            print("You don't have enough money in your account.")
        else:
            self.balance -= amount
            print(f"{amount} taka withdrawed.")
            self.bank.remove_from_bank_balance(amount)
            self.history += str(date.today()) + "\n" + f"Amount withdrawn: {amount} taka.\n"

    def check_balance(self):
        print(f"You have {self.balance} taka in your account.")

    def transfer(self, recipient, amount):
        if recipient in self.bank.users:
            if amount > self.balance:
                print("You don't have enough money in your account.")
            else:
                recipient.balance += amount
                self.balance -= amount
                print(f"{amount} taka transferred.")
                self.history += str(date.today()) + "\n" + f"Amount transferred to {recipient.name}'s account: {amount} taka.\n"
        else:
            print("Recipient doesn't exist.")

    def check_transaction_history(self):
        print(self.history)

    def loan(self, amount):
        if not self.bank.loan_status():
            print("Sorry, bank loans are disabled right now.")    
        elif amount > 2*self.balance:
            print(f"You can take maximum {2*self.balance} taka loan from the bank.")
        elif amount > self.balance:
            print("Sorry, the bank is bankrupt.")
        else:
            self.bank.remove_from_bank_balance(amount)
            self.bank.add_to_loan_amount(amount)
            print(f"{amount} taka loan taken.")


#for_example
bank = Bank()
user1 = User("Maxwell", bank, "01626374656", "maxwell12@gmail.com", "deposit", 1000)
bank.create_account(user1)
user2 = User("Klaseen", bank, "01626356656", "klaseen32@gmail.com", "savings", 5000)
bank.create_account(user2)
user3 = User("Butler", bank, "01626377856", "butler45@gmail.com", "deposit", 1500)
bank.create_account(user3)
user4 = User("Mahmudullah", bank, "01626374690", "riad3745@gmail.com", "deposit", 500)
bank.create_account(user4)
user5 = User("Rohit", bank, "01626374454", "rohit243@gmail.com", "savings", 3000)
bank.create_account(user5)

user1.deposit(2000)
user1.withdrawal(500)
user1.deposit(2000)
user1.transfer(user5, 500)
user1.check_balance()
user5.check_balance()
user1.check_transaction_history()

print(bank.admin_check_balance())
user2.loan(5000)
print(bank.admin_check_balance())
print(bank.admin_check_loan_amount())

bank.admin_loan_feature(False)
user1.loan(1000)