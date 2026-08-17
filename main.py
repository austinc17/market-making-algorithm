import pandas as pd

from simulations.simulator import Simulator
from tradingstrategy.basicmarketmaker import MarketMaker

prices = pd.read_csv("stockdata/prices.csv")
price_series = prices["price"].tolist()

capital_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
spreads = [0.0001,0.0002,0.0003,0.0004, 0.0005,0.0006,0.0007,0.0008, 0.0009, 0.001]

all_results = []

for spread in spreads:
    print("\n====================================")
    print(f"Testing spread: {spread}")
    print("====================================")

    for capital in capital_levels:
        print("\n------------------------------")
        print(f"Testing starting capital: ${capital}")
        print("------------------------------")

        mm = MarketMaker(spread=spread, starting_capital=capital)
        sim = Simulator(price_series, mm)

        final_value, profit, return_pct, trades = sim.run()

        all_results.append({
            "spread": spread,
            "capital": capital,
            "final_value": final_value,
            "profit": profit,
            "return_pct": return_pct,
            "trades": trades
        })

results_df = pd.DataFrame(all_results)

results_df["spread"] = results_df["spread"].round(4)
results_df["final_value"] = results_df["final_value"].round(2)
results_df["profit"] = results_df["profit"].round(2)
results_df["return_pct"] = results_df["return_pct"].round(2)

results_df.to_csv("results.csv", index=False)

print("\nFinal Results Table:")
print(results_df)
print("\nResults saved to results.csv")

