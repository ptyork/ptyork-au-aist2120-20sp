x = 'Paul York'
if x == 'Paul York':
    print('yep')

if 'York' in x:
    print('yep')

msg = 'Please contact me at paul@awesome.dude immediately.'
addr = 'paul@awesome.dude'
addr = 'paul.york@augusta.edu'

addr = input('enter email address: ')

# does it have an @
parts = addr.split('@')
if len(parts) != 2:
    print('NO @')
    exit()

username = parts[0]
if len(username) < 1:
    print('NO user')
    exit()

if ' ' in username or '\\' in username:
    print('invalid username')
    exit()

domain = parts[1]
if '.' not in domain:
    print('invalid domain')
    exit()

print(addr + ' is a valid email address')
