from sys import argv

script = argv
filename = raw_input('Here\'s your file : ')
txt = open(filename)
print txt.read()
txt.close()

