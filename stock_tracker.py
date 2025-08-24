# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("📊 Welcome to the Stock Portfolio Tracker 📊")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' when you finish entering your stocks.\n")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(" Stock not found! Please enter a valid stock symbol.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print(" Invalid input! Quantity must be a number.")
        continue
    
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"Added {quantity} shares of {stock} worth ${investment}\n")

print("\n Your Portfolio Summary ")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save results in a text file (plain text, no emojis)
with open("portfolio_summary.txt", "w") as f:
    f.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
    f.write(f"\nTotal Investment Value: ${total_investment}\n")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")


