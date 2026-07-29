stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

print("Welcome to Stock Portfolio Tracker")

stock = input("Enter stock name (AAPL/TSLA/GOOG/MSFT): ").upper()

if stock in stock_prices:
    quantity = int(input("Enter quantity: "))
    total = stock_prices[stock] * quantity

    print("\nStock:", stock)
    print("Price per share: $", stock_prices[stock])
    print("Quantity:", quantity)
    print("Total Investment: $", total)
else:
    print("Stock not found!")