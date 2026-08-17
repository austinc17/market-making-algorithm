class MarketMaker:
    def __init__(self, spread=0.0005, starting_capital=1000):
        self.spread = spread
        self.starting_capital = starting_capital
        self.cash = starting_capital
        self.inventory = 0

    def quote(self, mid_price):
        """
    Inventory-aware quoting.
    If we hold too much stock, we lower our ask to sell faster.
    If we are short, we raise our bid to buy faster.
    """
        inventory_skew = 0.0002 * self.inventory
        bid = mid_price * (1 - self.spread) - inventory_skew
        ask = mid_price * (1 + self.spread) - inventory_skew
        
        return bid, ask

    def can_buy(self, bid_price):
        return self.cash >= bid_price

    def can_sell(self):
        return self.inventory > 0