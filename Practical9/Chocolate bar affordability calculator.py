def chocolatebar_affordability(money, price_perbar):
    number_bars = money // price_perbar
    change_left = money % price_perbar
    return number_bars, change_left

# example
money = 199
price_perbar = 6
bars_bought, change = chocolatebar_affordability(money, price_perbar)
print(f"With ${money}, you can buy {bars_bought} chocolate bars and you will have ${change} left.")
