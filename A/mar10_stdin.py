import sys

def paul_input(prompt=''):
    if prompt:
        sys.stdout.write(prompt + ': ')
        sys.stdout.flush()
    
    intext = sys.stdin.readline()
    intext = intext.rstrip()
    return intext

txt = paul_input('Enter text')
print(f'You typed: {txt}')
