class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    def set_balance(self,newbalance):
        self.__balance=newbalance


acc1=BankAccount("Rahul Kumar singh",20_000)
print(acc1.name ,acc1._BankAccount__balance)