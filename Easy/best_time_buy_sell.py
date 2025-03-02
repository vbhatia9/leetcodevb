def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
            print(f"Min Price {min_price}") #Min Price 7 Min Price 1
        elif price - min_price > max_profit:
            max_profit = price - min_price  #Max Profit 5-1 = 4 and then 6-1 = 5
            print(f"Max Profit {max_profit}") #Max Profit 0 Max Profit 5

    return max_profit

#Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5