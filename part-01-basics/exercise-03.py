def celcius_to_farenheit(c):
    if c < -273.15:
        return "Minimum temperature is -273.15c"
    return 9 / 5 * c + 32

print(100, celcius_to_farenheit(100))
print(0, celcius_to_farenheit(0))
print(20, celcius_to_farenheit(20))
print(-32, celcius_to_farenheit(-32))
print(-300, celcius_to_farenheit(-300))
