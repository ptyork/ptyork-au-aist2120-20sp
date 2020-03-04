import re

# compile an expression (the book way and thus our way)
# or JUST use the expression  (e.g., re.search(pattern, string))

msg = '''
My name is Paul York. Please contact me by email at 
paul.york@augusta.edu at your earliest convenience or 
twitter @ @ptyork or @@ tattoine or paul@yorkie. I 
collect corks. And I work. Mork from ork.
'''

patt = re.compile('\w?ork')   # 0 or 1 letter followed by "ork"
mat = patt.search(msg)
print(mat)
mat = patt.search(msg,21)
print(mat)
matches = patt.findall(msg)
print(matches)

for mat in patt.finditer(msg):
    print(mat)

phones = '''
7065551212
706-555-1313
706 555 1414
706.555.1515
(706) 555-1616
(706)555-1717
Bob-The-Best
706555667788
12345
'''

patt = re.compile('706')
print(patt.findall(phones))

'''
REGULAR EXPRESSION SYNTAX "RULES"
 - Custom character
   [abc] finds a or b or c
   [Yy] finds Y or y
   [0-6] finds 0,1,2,3,4,5 or 6
   [A-F] finds A,B,C,D,E,F
   [0-9A-Fa-f] finds a hex digit
 - Special characters
   \d  == numeric digit >> [0-9]
   \w  == "word" character >> [A-Za-z0-9]
   \s  == "space" character
   \S  == all but "space" character
   b{3} find exactly 3 b's ("bbb")
   x{6} find exactly 6 x's ("xxxxxx")
   v{2,5} finds 2, 3, 4 or 5 v's  ("vv", "vvv", "vvvv", "vvvvv")
   x{,6} find up to 6 x's
   x{6,} find at least 6 x's
   x? - find 0 or 1 x ==> {,1}
   x* - find 0 or many x's 
   x+ - find 1 or many x's ==> {1,}
'''

# pwnd_patt = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# pwnd_patt = re.compile(r'\d\d\d[- .]\d\d\d[- .]\d\d\d\d')
# pwnd_patt = re.compile(r'\d{3}[- .]\d{3}[- .]\d{4}')
pwnd_patt = re.compile(r'\(?\d{3}\)?[- .]?\d{3}[- .]?\d{4}')
print(pwnd_patt.findall(phones))

def is_phone(num):
    # pwnd_patt = re.compile(r'\(?\d{3}\)?[- .]?\d{3}[- .]?\d{4}')
    # pwnd_patt = re.compile(r'^\(?\d{3}\)?[- .]?\d{3}[- .]?\d{4}$')
    # pwnd_patt = re.compile(r'''
    #         ^       # Beginning Anchor
    #         \(?     # Optional Opening Paren
    #         (\d{3}) # Area Code (3 digits)
    #         \)?     # Optional Closing Paren
    #         [- .]?  # Optional ., - or space
    #         (\d{3}) # Exchange (3 digits)
    #         [- .]?  # Optional ., - or space
    #         (\d{4}) # Number (4 digits)
    #         $       # End of String Anchor
    #     ''', re.VERBOSE)
    pwnd_patt = re.compile(r'''
            ^       # Beginning Anchor
            \(?     # Optional Opening Paren
            (706|762|803) # Area Code (3 digits)
            \)?     # Optional Closing Paren
            [- .]?  # Optional ., - or space
            (\d{3}) # Exchange (3 digits)
            [- .]?  # Optional ., - or space
            ([0-9]{4}|[A-Z]{4}) # Number (4 digits)
            $       # End of String Anchor
        ''', re.VERBOSE)
    # if pwnd_patt.match(num) is not None:
    #     return True
    # else:
    #     return False
    return pwnd_patt.match(num) is not None

def get_phone_parts(num):  # return a tuple containing the three parts
    # pwnd_patt = re.compile(r'(\d{3})[- .]?(\d{3})[- .]?(\d{4})')
    pwnd_patt = re.compile(r'''
        (\d{3})     # Area Code Group
        [- .]?      # Optionally a ., - or space
        (\d{3})     # Exchange Group
        [- .]?      # Optionally a ., - or space
        (\d{4})     # Number Group
        \s*         # Ignore 0 or more spaces
        (.*)        # Capture whatever is left
    ''', re.VERBOSE)
    mat = pwnd_patt.match(num)
    if mat is not None:
        # return ('706','555','1212')
        # num = '7065551212'
        # return (num[:3], num[3:6], num[6:])
        return mat.groups()
    else:
        return None
    
parts = get_phone_parts('706-555-1212')
print(f'Area Code: {parts[0]}')
print(f'Exchange:  {parts[1]}')
print(f'Number:    {parts[2]}')

parts = get_phone_parts('706-555-Booger')
if parts:   # Truthy or Falsey
    print(f'Area Code: {parts[0]}')
    print(f'Exchange:  {parts[1]}')
    print(f'Number:    {parts[2]}')

parts = get_phone_parts('706-555-1818 x123')
if parts:   # Truthy or Falsey
    print(f'Area Code: {parts[0]}')
    print(f'Exchange:  {parts[1]}')
    print(f'Number:    {parts[2]}')
    print(f'Extension: {parts[3]}')

parts = get_phone_parts('762-867-5309 Jenny Don\'t Lose My Number')
if parts:   # Truthy or Falsey
    print(f'Area Code: {parts[0]}')
    print(f'Exchange:  {parts[1]}')
    print(f'Number:    {parts[2]}')
    print(f'Extension: {parts[3]}')


print(is_phone('7065551212'))
print(is_phone('706555181818'))
print(is_phone('762-111-2222'))
print(is_phone('770-123-4567'))

