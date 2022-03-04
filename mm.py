class MoneyManager:
    def __init__(self):
        pass
    def MoneySplit(self,balance):
        self.pocket1 = (balance/3).__floor__()
        self.pocket2 = (balance/3).__floor__()
        self.pocket3 = (balance/3).__floor__()
        return self.pocket1, self.pocket2, self.pocket3

    def martingale():
        print("martingale")
        pass