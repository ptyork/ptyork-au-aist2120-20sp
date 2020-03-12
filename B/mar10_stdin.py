import sys

def paul_input(prompt=''):
    if prompt:  # len(prompt) > 0
        sys.stdout.write(prompt)
        sys.stdout.flush()
    
    text = sys.stdin.readline() # stdin is file like, but doesn't actually read from disk, only from keyboard
    text = text.rstrip()
    return text

# paultext = input('Enter some text: ')
paultext = paul_input('Enter some text: ')
print(f"You typed: {paultext}.")

