class Account(object):
    def __init__(self, id, name, balance=0):
        # id (number), a name (string), and a balance (integer; optional; 0 by default)
        self.id = id
        self.name = name
        self.balance = balance

    # -	credit(amount) - adds the amount to the balance and returns the new balance
    def credit(self, amount):
        self.balance += amount
        return self.balance

    # -	debit(amount) - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance. Otherwise, return "Amount exceeded balance"
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    # -	info() - returns "User {name} with account {id} has {balance} balance"
    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
