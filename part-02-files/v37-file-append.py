file = open("./example-2.txt", 'w')  # creates empty file
file.write("line 0\n")
file.write("line 1\n")
file.write("line 2\n")
file.close()

file = open("./example-2.txt", 'a')
file.write("line 3\n")
file.close()
