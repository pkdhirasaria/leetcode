class Bank:

    def __init__(self, balance: List[int]):
        self.account = dict()
        for i,b in enumerate(balance):
            self.account[i+1] = b

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.account.get(account1,None) is None or self.account.get(account1,None) < money or self.account.get(account2,None) is None:
            return False
        self.account[account1] -= money
        self.account[account2] += money
        return True

    def deposit(self, account1: int, money: int) -> bool:
        if self.account.get(account1,None) is None:
            return False
        self.account[account1] += money
        return True
    def withdraw(self, account1: int, money: int) -> bool:
        
        if self.account.get(account1,None) is None  or self.account.get(account1,None) < money:
            return False
        self.account[account1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)