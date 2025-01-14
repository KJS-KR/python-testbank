def calculate_change(money):
    coins = [500, 100, 50, 10]
    change = 0

    for coin in coins:
        change += money // coin
        money %= coin

    return change


money = 12320
print(calculate_change(money))
