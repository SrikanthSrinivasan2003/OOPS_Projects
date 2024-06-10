class BankAccount:
    def __init__(self,account_number):
        self.account_number = str(account_number)
        self.balance = 0
        
    def get_balance(self):
        return self.balance
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds!!")
            
    def deposit(self,amount):
        self.balance += amount
        
def transfer_amount(account_1,account_2,amount):
    try:
        account_1.withdraw(amount)
        account_2.deposit(amount)
        return True
    except ValueError as e:
        print(str(e))
        return False
        
user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(50)
user_2.deposit(100)
print("User 1  Balance : {}/-".format(user_1.get_balance()))
print("User 2  Balance : {}/-".format(user_2.get_balance()))
print("Transfering Money from user_1 to user_2")
transfer_status = transfer_amount(user_1,user_2,60)
if transfer_status:
    print("Transfering Money from user_1 to user_2")
else:
    print("Money Transfering Failed!!")
print("User 1  Balance : {}/-".format(user_1.get_balance()))
print("User 2  Balance : {}/-".format(user_2.get_balance()))
