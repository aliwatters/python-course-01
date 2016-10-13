def celcius_to_farenheit(c):
    if c < -273.15:
        return "error"
    return (9 / 5) * c + 32

temperatures = [10, -20, -289, 100]

file = open("exercise-05.txt", 'w')

for temp in temperatures:
    t = celcius_to_farenheit(temp)
    if t != "error":
        file.write(str(t) + "\n")

file.close()
