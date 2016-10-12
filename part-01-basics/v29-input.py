
def curreny_converter(rate, euros):
    return rate * euros

r = input("Enter Rate: ")
e = input("Enter Euros: ")

print("You have: $", curreny_converter(float(r), float(e)), " dollars")
