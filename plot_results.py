import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

# -------- Graph 1: Return vs Capital --------
plt.figure()

for spread in sorted(df["spread"].unique()):
    subset = df[df["spread"] == spread]
    plt.plot(subset["capital"], subset["return_pct"], marker="o", label=f"Spread {spread}")

plt.xlabel("Starting Capital ($)")
plt.ylabel("Return (%)")
plt.title("Return (%) vs Starting Capital for Different Spreads")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("return_vs_capital.png")
print("Saved: return_vs_capital.png")
plt.show()


# -------- Graph 2: Trades vs Capital --------
plt.figure()

for spread in sorted(df["spread"].unique()):
    subset = df[df["spread"] == spread]
    plt.plot(subset["capital"], subset["trades"], marker="o", label=f"Spread {spread}")

plt.xlabel("Starting Capital ($)")
plt.ylabel("Number of Trades")
plt.title("Trades vs Starting Capital for Different Spreads")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("trades_vs_capital.png")
print("Saved: trades_vs_capital.png")
plt.show()