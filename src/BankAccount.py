class BankAccount(object):
    __class_hiding_member = "I'm now hiding"
    total = 0

    def __init__(self):
        self.__amount = 0  # keep accessing from outside class
        self.sn = '0000-0000-0000'

    def deposit(self, money):
        # can access a hiding member within it's own class
        # provide getter, setter methods to interact hiding member from outside
        self.__amount += money

    def balance(self):
        return self.__amount

    def withdraw(self, money):
        # TODO: there might be a potential logic issue here try to fix it
        if self.balance() >= money:
            self.__amount -= money
            return money
        else:
            raise Exception("Not enough money!")

    def transfer(self):
        # implement this method
        pass

if __name__ == '__main__':
    acc1 = BankAccount()
    acc1.sn = '1234-5678-6666'
    # print acc1.__amount
    # acc1.__amount = 9999
    print "default balance: ", acc1.balance()
    acc1.deposit(100)
    print "deposit 100: ", "balance: ", acc1.balance()

    try:
        print "withdraw: ", acc1.withdraw(80), "balance: ", acc1.balance()
        print "withdraw: ", acc1.withdraw(15), "balance: ", acc1.balance()
        print "withdraw: ", acc1.withdraw(5), "balance: ", acc1.balance()
        print "withdraw: ", acc1.withdraw(-100), "balance: ", acc1.balance()
    except Exception as ex:
        print "[reason]", ex.message, "balance: ", acc1.balance()

    # can still access hiding member with vars()
    # print vars(acc1)
    # print vars(BankAccount)
    #
    # print acc1._DataHiding__amount
    # print acc1._DataHiding__class_hiding_member
