class Simulator:
    def __init__(self, prices, market_maker):
        self.prices = prices
        self.mm = market_maker

    def run(self):
        trade_count = 0

        for i in range(len(self.prices) - 1):
            current_price = self.prices[i]
            next_price = self.prices[i + 1]

            bid, ask = self.mm.quote(current_price)

            if next_price <= bid and self.mm.can_buy(bid):
                self.mm.inventory += 1
                self.mm.cash -= bid
                trade_count += 1

            elif next_price >= ask and self.mm.can_sell():
                self.mm.inventory -= 1
                self.mm.cash += ask
                trade_count += 1

        final_price = self.prices[-1]
        final_portfolio_value = self.mm.cash + (self.mm.inventory * final_price)
        profit = final_portfolio_value - self.mm.starting_capital
        return_pct = (profit / self.mm.starting_capital) * 100

        print("Starting capital:", self.mm.starting_capital)
        print("Final cash:", round(self.mm.cash, 2))
        print("Final inventory:", self.mm.inventory)
        print("Final stock price:", round(final_price, 2))
        print("Final portfolio value:", round(final_portfolio_value, 2))
        print("Profit / Loss:", round(profit, 2))
        print("Return (%):", round(return_pct, 2))
        print("Total trades executed:", trade_count)

        return final_portfolio_value, profit, return_pct, trade_count