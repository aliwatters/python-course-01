
def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

amount = currency_converter(1.2, 10)
print(amount)
