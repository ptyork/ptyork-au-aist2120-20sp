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
  - (....) is a "group"
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
    # phone_ex = re.compile(r'\d{3}[- .]?\d{3}[- .]?\d{4}')
    # phone_ex = re.compile(
    #     r'''
    #     \(?       # Optionally an open parenthesis
    #     (\d{3})   # A group with just the area code
    #     \)?       # Optionall a closing parenthesis
    #     [- .]?    # Optionally a -, space or .
    #     (\d{3})   # A group with just the exchange
    #     [- .]?    # Optionally a -, space or .
    #     (\d{4})   # A group with just the 4 digits
    #     ''',
    #     re.VERBOSE
    phone_ex = re.compile(
        r'''
        \(?       # Optionally an open parenthesis
        (706|762|678|404)   # A with 4 options for area code
        \)?       # Optionall a closing parenthesis
        [- .]?    # Optionally a -, space or .
        (\d{3})   # A group with just the exchange
        [- .]?    # Optionally a -, space or .
        (\d{4})   # A group with just the 4 digits
        ''',
        re.VERBOSE
    )
    if phone_ex.search(num):
        print(num + ' is a phone')
    else:
        print(num + " is NOT a phone")

def get_phone_bits(num):
    # phone_ex = re.compile(r'(\d{3})[- .]?(\d{3})[- .]?(\d{4})\s*(.*)')
    phone_ex = re.compile(
        r'''
        (\d{3})   # A group with just the area code
        [- .]?    # Optionally a -, space or .
        (\d{3})   # A group with just the exchange
        [- .]?    # Optionally a -, space or .
        (\d{4})   # A group with just the 4 digits
        \s*       # Zero or more spaces
        (.*)      # Zero or more "anythings"
        ''',
        re.VERBOSE
    )
    res = phone_ex.search(num)
    if res:
        bits = res.groups()
        # print(f"the area code is {bits[0]}")
        return bits
    else:
        print(num + " is NOT a phone")
        return


# should succeed
phone_check('706-555-1212')
phone_check('706 555 1212')
phone_check('706.555.1212')
phone_check('7065551212')
phone_check('(706) 555-1212')

# should fail
phone_check('803-555-1212')
phone_check('(706555-1212')
phone_check('706)-555-1212')
phone_check('POO-555-1212')
phone_check('706x555x1212')
phone_check('706555121212')
phone_check('70655512')

get_phone_bits('706-555-1212')
get_phone_bits('706 555 1212')
get_phone_bits('706.555.1212')
bits = get_phone_bits('7065551212')
print(f"Area Code: {bits[0]}")
print(f"Exchange: {bits[1]}")
print(f"Number: {bits[2]}")
print(f"Extension: {bits[3]}")

bits = get_phone_bits('706.555 1212 x702')
print(f"Area Code: {bits[0]}")
print(f"Exchange: {bits[1]}")
print(f"Number: {bits[2]}")
print(f"Extension: {bits[3]}")

