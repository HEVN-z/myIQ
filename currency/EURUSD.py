class EURUSD:
    def __init__(self, bot):
        self.bot = bot
        self.goal = "EURUSD"
        self.amount = 0.1
        self.Action = "call"
        self.expirations_mode = 1
        self.target_time = 30
        self.id = 0
        self.check = False
        self.win = 0
        self.win_amount = 0
        self.profit = 0
        self.profit_amount = 0
        self.loss = 0
        self.loss_amount = 0
        self.balance = 0