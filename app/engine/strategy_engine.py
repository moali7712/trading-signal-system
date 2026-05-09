class StrategyEngine:

    def __init__(self):

        self.strategies = []

    def add_strategy(self, strategy):

        self.strategies.append(strategy)

    def process(self, price):

        for strategy in self.strategies:

            strategy.check_signal(price)