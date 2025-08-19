# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 135,
    "MSFT": 320,
    "AMZN": 140
}

def stock_tracker():
    portfolio = {}
    total_investment = 0

    print("📊 Welcome to Simple Stock Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break
        elif stock not in stock_prices:
            print("❌ Stock not available. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Save to portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"✅ Added {quantity} shares of {stock}")

    print("\n----- Portfolio Summary -----")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_investment += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

    print("\n💰 Total Investment Value = $", total_investment)

    # Optional: Save results to file
    save = input("\nDo you want to save results to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
            f.write(f"Total Investment,,,{total_investment}\n")
        print("📁 Results saved to portfolio.csv")

# Run program
if __name__ == "__main__":
    stock_tracker()
