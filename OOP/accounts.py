import datetime
import pytz

class Account:
    """Simple account class with balance. """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction = [(Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction.append((Account._current_time(), -amount))
        else:
            print("Amount must be smaller")
            self.show_balance()

    def show_balance(self):
        print("Balance is: {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6}, {} on {} (localtime was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2007)

    tim.show_transactions()

    steph = Account("Steph", 800)

    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()