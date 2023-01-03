import datetime
import random


class BankAccount:
    index = 1

    def __init__(self, account_client,client_name):
        self.id = BankAccount.index
        BankAccount.index += 1
        self.account_number = random.randint(10000, 99999)
        self.account_client = account_client
        self.balance = 0
        self.transactions_list = []


class SavingAccount(BankAccount):

    def __init__(self, account_client,client_name):
        super().__init__(account_client,client_name)
        self.limit = 20000


class DepositAccount(BankAccount):
    def __init__(self, account_client,client_name):
        super().__init__(account_client,client_name)
        self.expire_date = datetime.datetime.now() + datetime.timedelta(days=365)


deposit_account = DepositAccount("123456","Mohanad")
print(deposit_account.expire_date)


# bank_account =BankAccount("Mohanad")
# print(bank_account.account_number)
#
# saving_account = SavingAccount("Ali")
# print(saving_account.limit)