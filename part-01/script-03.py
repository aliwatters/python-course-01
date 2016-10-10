# numbers

print(type(1), 1)  # integers

print(type(1.102), 1.102)  # floats

print(type(56j), 56j)  # complex

a = float(8)  # int to float
print(type(a), a)

b = round(8.6)  # float to int
print(type(b), b)

# operators: +,-,%,/,*

# note - crappy accuracy on float (like js)
c = 0.1 * 0.2
print(type(c), c)

d = 0.1 + 0.2
print(type(d), d)

# >>> import math
# >>> dir(math)

import math
e = math.sqrt(100)  # math does float operations
print(type(e), e)

f = 2**4  # exponent (nice!)
print(type(f), f)
