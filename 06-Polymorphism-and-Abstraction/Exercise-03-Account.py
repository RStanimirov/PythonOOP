# 100/100 in judge:
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __add__(self, other):
        new_acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ne__(self, other):
        return self.balance != other.balance


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(acc2)
print(repr(acc))
print(repr(acc2))
acc.add_transaction(20)
# acc.validate_transaction(acc, 20)
acc.add_transaction(-20)
# acc.validate_transaction(acc, -20)
acc.add_transaction(30)
# acc.validate_transaction(acc, 30)
print(acc._transactions)
print(acc.balance)
print(len(acc))
for x in acc:
    print(x)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
