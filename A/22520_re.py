import re

msg = 'The quick brown fox jumps over the lazy student.'
# msg = 'quick brown fox jumps over lazy student.'

the_ex = re.compile(r'[Tt]he')
match = the_ex.search(msg)
print(match)

if match is not None:
    print('FOUND IT')
else:
    print('NOT THERE')

if match:
    print('FOUND IT')
else:
    print('NOT THERE')

if the_ex.search(msg):
    print('FOUND IT')
else:
    print('NOT THERE')

for match in the_ex.finditer(msg):
    print(f"found {match}")



'''
Regular Expression Rules:
  - Matches left to right
  - Character by character match
  - \d match a digit
  - . match ANY character
       \d. => 3d  33  53  0 
  - \w match any letter
  - \d{3}    # match exactly 3 digits
  - \d{3,5}  # match 3, 4 or 5 digits
  - \d{,3}   # match 1, 2 or 3 digits
  - \d{3,}   # match 3 or more digits
  - ?   # match 0 or 1
  - *   # match 0 or many
  - +   # match 1 or many
'''

num = '706-555-1212'
#num = 'POO-555-1212'
# phone_ex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_ex = re.compile(r'\d{3}-\d{3}-\d{4}')
if phone_ex.search(num):
    print(num + ' is a phone')
else:
    print(num + " is NOT a phone")

def phone_check(num):
    # phone_ex = re.compile(r'\d{3}[- ]\d{3}[- ]\d{4}')
    # phone_ex = re.compile(r'\d{3}[- .]\d{3}[- .]\d{4}')
    phone_ex = re.compile(r'\d{3}[- .]?\d{3}[- .]?\d{4}')
    if phone_ex.search(num):
        print(num + ' is a phone')
    else:
        print(num + " is NOT a phone")

# should succeed
phone_check('706-555-1212')
phone_check('706 555 1212')
phone_check('706.555.1212')
phone_check('7065551212')
num4 = '(706) 555-1212'

# should fail
phone_check('POO-555-1212')
phone_check('706x555x1212')
