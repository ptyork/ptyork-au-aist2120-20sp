import sys
print(sys.argv)
# exit()

#f = open('kennedy.txt')
#f = open('emails.txt')

if len(sys.argv) != 2:
    print('ERROR: give me a file name, dang it!!')
    exit()

filename = sys.argv[1]  # [0] is always the name of the script...others are arguments
f = open(filename)

lines = f.readlines()
# print(lines)
# exit()
f.close()

linenum = 0
for line in lines:
    linenum += 1
    line = line.rstrip()
    print(f"{linenum:3}: {line}")
    #print(line, end='')

