import sys
# print(sys.argv)
# exit()

# filename = 'kennedy.txt'
if len(sys.argv) != 2:
    print('hey, I need a file name!!')
    exit()

filename = sys.argv[1]

f = open(filename)

# Read every character and print it vertically
# char = f.read(1)
# while char:
#     print(char)
#     char = f.read(1)

# Read every character and print it with a space in betwwen each char
# char = f.read(1)
# while char:
#     print(char + ' ', end='')
#     char = f.read(1)

# print with a line number before each line
lines = f.readlines()
f.close()

# print(lines)
linenum = 0
for line in lines:
    linenum += 1
    line = line.rstrip()
    print(f'{linenum:>3}: {line}')
