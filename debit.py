class UserAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def add_balance(self, amount):

        self.balance += amount
        print(f"{amount} added to {self.name}'s account. New balance: {self.balance}")

    def debit_balance(self, amount):

        if amount <= self.balance:

            self.balance -= amount
            print(f"{amount} debited from {self.name}'s account.New balance: {self.balance}")
        else:
            print(f"Insufficient balance in {self.name}'s account.")

    def delete_account(self):

        print(f"{self.name}'s account has been deleted.")
        del self
user1 = UserAccount("Adama", 3000)
user2 = UserAccount("Umaru", 900)

user1.add_balance(2500)  # adds 2500 to Adama's account
user2.debit_balance(700)  # debits 700 from Umaru's account
user1.delete_account()  # deletes Adama's account