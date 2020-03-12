import sys

if len(sys.argv) != 2:
    print('ERROR: give me a file name, dang it!!')
    exit()

# python mar10_filewrite.py out.txt
# argv = ['mar10_filewrite.py','out.txt']

filename = sys.argv[1]  # [0] is always the name of the script...others are arguments

# f = open(filename, 'w') # COULD be 'a' to append
# DO STUFF WITH F
# f.close()

with open(filename, 'w') as f:
    # DO STUFF WITH F
    f.write('hello\n')
    f.write('world\n')
    f.write('Paul wuz here\n')

# AUTO CLOSED F