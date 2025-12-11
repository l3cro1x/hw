def calculate_profit(n):
    min_buy_price = n[0]
    max_profit = 0
    for price in n[1:]:
        curr_profit = price - min_buy_price
        if curr_profit > max_profit:
            max_profit = curr_profit
        if min_buy_price > price:
            min_buy_price = price
    return max_profit

print(calculate_profit([1,6,9,3,2,10]))
print(calculate_profit([20,19,10,8,3,4,2]))
print(calculate_profit([20,19,10,8,4,2]))