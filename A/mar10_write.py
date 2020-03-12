import sys

if len(sys.argv) != 2:
    print('hey, I need a file name!!')
    exit()

filename = sys.argv[1]

# f = open(filename, 'w')  # 'w' overWrite, 'a' Append
with open(filename, 'w') as f:
    f.write('Paul wuz here\n')
    f.write('Paul rulez\n')

# here I've left the with block so f is implicitly closed
