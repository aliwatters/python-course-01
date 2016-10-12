# 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode',
# 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines',
# 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines'


file = open("./example.txt", 'r')

content = file.readlines()
print(content)

file.seek(0)  # reset pointer

content = file.readlines()
content = [i.rstrip("\n") for i in content] # do something on each element
print(content)

file.close()  # removes lock
