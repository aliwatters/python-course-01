import random
import string

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
length = 3

lst = ['', '', '']
msg = "What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any: "
for i in range(length):
    lst[i] = input(msg)


def generator():
    output = ""
    for i in range(length):
        if(lst[i] == 'v'):
            output += random.choice(vowels)
        elif(lst[i] == 'c'):
            output += random.choice(consonants)
        elif(lst[i] == 'l'):
            output += random.choice(string.ascii_lowercase)
        else:
            output += lst[i]

    return output

for i in range(20):
    print(generator())
