# 设计一个 Account 类表示账户，自行设计该类中的属性和方法，
# 并利用这个类创 建一个账号为 998866，余额为 2000，
# 年利率为 4.5%的账户，然后从该账户中存 入 150，
# 取出 1500。打印出帐号、余额、年利率、月利率、月息。

class Account:
    def __init__(self, account, balance):
        self.account = account

        self.balance = balance
        self.year_Rate = 0.045

    def save_money(self, money):
        self.balance += money

    def out_money(self,money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("余额不足")


    def check_balance(self):
        print("账号：{}  余额：{}  年利率：{}  月利率：{}   月息：{}".format(self.account,  self.balance,self.year_Rate,self.year_Rate / 12,self.year_Rate / 12*self.balance ))


account = Account("998866",2000)
account.out_money(150)
account.check_balance()
