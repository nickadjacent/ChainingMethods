class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self

    def user_transfer_balance(self, amount, transferee):
        self.account_balance -= amount
        print(self.name)
        print(self.account_balance)
        transferee.account_balance += amount
        print(transferee.name)
        print(transferee.account_balance)
        return self


user1 = User('Matthew', 'matthew@gmail.com', 100)
user2 = User('Mark', 'mark@gmail.com', 500)
user3 = User('Luke', 'luke@gmail.com', 1000)


user1.make_deposit(100).make_deposit(50).make_deposit(
    25).make_withdrawal(75).display_user_balance()


user2.make_deposit(200).make_deposit(300).make_withdrawal(
    100).make_withdrawal(1000).display_user_balance()


user3.make_deposit(1000).make_withdrawal(100).make_withdrawal(
    200).make_withdrawal(300).display_user_balance()


user1.user_transfer_balance(100, user2)
