class BankAccount:
    def __init__(self, balance):
        self._balance = balance   #приватное поле благодаря _

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Должно быть положительным")
        self._balance += amount
        return self._balance

    def get_balance(self):
        return self._balance

money = BankAccount(100000)

print(money.get_balance())
print(money.deposit(500))

        