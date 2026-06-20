stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300,
    "AMZN": 130
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total += value
        print(stock, "value =", value)
    else:
        print("Stock not found")

print("Total Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))