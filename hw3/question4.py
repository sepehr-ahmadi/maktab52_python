class BankAccount:

    def __init__(self, name, res_account, min_res_account):
        self.name = name
        self.res_account = res_account
        self.min_res_account = min_res_account

    def deposit(self, depostion_amount):
        self.res_account = depostion_amount + self.res_account
        print(f'{self.name} account residual is {self.res_account}')

    def withdrawal(self, withdrawal_amount):
        if self.__withdrawal_limitaion(withdrawal_amount):
            self.res_account = self.res_account - withdrawal_amount
            print(f'{self.name} account residual is {self.res_account}')
        else:
            print(f"{self.name} account residual is not enough try again with another amount")

    def transfer(self, transfer_amount, reciever_account):
        if self.__withdrawal_limitaion(transfer_amount) == True:
            self.res_account = self.res_account - transfer_amount
            reciever_account.res_account=reciever_account.res_account+transfer_amount
            print(f'{self.name} account residual is {self.res_account}')
        else:
            print(f"{self.name} account residual is not enough try again with another amount")

    def __withdrawal_limitaion(self, amount_input):
        if self.res_account - amount_input > self.min_res_account:
            return True
        else:
            return False


myaccount= BankAccount("sepehr",1000,100)
anotheraccount= BankAccount("soheil",2000,200)
myaccount.deposit(100)
myaccount.transfer(100,anotheraccount)
g=BankAccount(5,1,3)