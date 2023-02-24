import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        # self.transaction_list.append((Account._current_time(), balance))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow(), amount))) Did not work

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Failed to withdraw - balance on your account must be more than the withdraw amount")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance} €")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':

    lasse = Account("Lasse",50)
    # lasse.show_balance()

    lasse.deposit(1000)
    lasse.withdraw(100)
    lasse.show_transactions()

    print("-" * 50)

    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
