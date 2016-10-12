def celcius_to_farenheit(c):
    if c < -273.15:
        return "Minimum temperature is -273.15c"
    return 9 / 5 * c + 32

temperatures = [10, -20, -289, 100]

for temp in temperatures:
    print(celcius_to_farenheit(temp))
