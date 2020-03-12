import sys

def paul_print(text, end='\n'):
    sys.stdout.write(text + end) # stdout is file like, but NOT a real file on disk
    sys.stdout.flush()  # empties the output buffer

paul_print('Hello', ' ')
paul_print('World')
paul_print('Paul', ' ')
paul_print('wuz', ' ')
paul_print('here')

# Hello World
# Paul wuz here
