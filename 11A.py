class Account:
    def __init__(self):
        self._balance = 0.0

    def deposit(self, m):
        self._balance += m

    def withdraw(self, m):
        if m <= self._balance:
            self._balance -= m
        else:
            print("Insufficient fund")

    def getBalance(self):
        return round(self._balance, 2)

class SavingsAccount(Account):
    def __init__(self, r):
        super().__init__()
        self.rate = r

    def calculate_interest(self, days):
        self._balance = self.getBalance() * (1 + self.rate / 36500) ** days

class CurrentAccount(Account):
    def __init__(self, od_limit):
        super().__init__()
        self.limit = od_limit

    def withdraw(self, m):
        if m <= self._balance + self.limit:
            self._balance -= m
        else:
            print("Insufficient fund")
# Do not change the code below this line.
sa = SavingsAccount(float(input()))
sa.deposit(float(input()))
print(sa.getBalance())
sa.calculate_interest(int(input()))
print(sa.getBalance())

ca = CurrentAccount(float(input()))
ca.deposit(float(input()))
print(ca.getBalance())
ca.withdraw(float(input()))
print(ca.getBalance())
ca.withdraw(float(input()))

print("Done")