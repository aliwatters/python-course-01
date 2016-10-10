# Lists

li = ["Today", "Tomorrow", 3]
print(li)

print(li[2], li[-1])
print(len(li))

del li[2]
print(li)

li.append(3)
print(li)

li.insert(1, 2)
print(li)

li.remove('Tomorrow')
print(li)

print(li[-1:])  # last item

# also has 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort'


def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

functions = [currency_converter(2, 5), currency_converter(1.3, 10)]
print(functions)

# Tuples -- immutable!

t=(1,2,3,4,5)
print(type(t))

print(t.count) # only has index and count
