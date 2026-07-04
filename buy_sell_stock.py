#Best time to buy and sell stock
#Brute force
def max_profit(prices: list[int]) -> int:
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

print(max_profit([7,1,5,3,6,4]))

#Optimized sol
def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

print(max_profit([7,1,5,3,6,4]))