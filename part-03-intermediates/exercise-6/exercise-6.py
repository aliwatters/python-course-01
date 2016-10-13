import datetime
import glob

files = glob.glob("*.txt")
files.sort()

filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
output = open(filename, 'w')

for filename in files:
    file = open(filename)
    output.write(file.read() + "\n")
    file.close()

output.close()
