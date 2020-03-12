import sys

def paul_print(text, end='\n'):
    sys.stdout.write(text + end)

paul_print('hello', ' ')
paul_print('world')
paul_print('Paul wuz here')
