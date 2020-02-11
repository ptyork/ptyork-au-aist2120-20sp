# Case Methods
# upper(), lower(), capitalize(), title()

# Space Removal
# strip(), lstrip(), rstrip()

# Also a bunch of isXXX() methods....don't ferget about 'em

# Word Proc stuff

# >>> name
# '   pAUl yorK    '
# >>> 'york' in name
# False
# >>> 'york' in name.lower()
# True
# >>> name.find('york')
# -1
# >>> name.find('yorK')
# 8
# >>> name.lower().find('york')
# 8
# >>> name.find(' ')
# 0
# >>> sname = name.strip().lower()
# >>> sname
# 'paul york'
# >>> sname.find('aul')
# 1
# >>> sname.find('Yor')
# -1
# >>> sname.index('Yor')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found
# >>> help(sname.replace)
# Help on built-in function replace:

# replace(old, new, count=-1, /) method of builtins.str instance
#     Return a copy with all occurrences of substring old replaced by new.

#       count
#         Maximum number of occurrences to replace.
#         -1 (the default value) means replace all occurrences.

#     If the optional argument count is given, only the first count occurrences are
#     replaced.

# >>> sname.replace(' ','--')
# 'paul--york'
# >>> sname.replace('Paul','Super')
# 'paul york'
# >>> sname.replace('paul','Super')
# 'Super york'
# >>> sname.lower().replace('paul','Super')
# 'Super york'
# >>> sname.lower().replace('paul','Super').title()
# 'Super York'



# >>> name = 'Paul York'
# >>> Name:           Paul York
#   File "<stdin>", line 1
#     Name:           Paul York
#                             ^
# SyntaxError: invalid syntax
# >>> name = "Jerry Garcia"
# >>> Name:        Jerry Garcia
#   File "<stdin>", line 1
#     Name:        Jerry Garcia
#                             ^
# SyntaxError: invalid syntax
# >>> name.ljust(20)
# 'Jerry Garcia        '
# >>> name.rjust(20)
# '        Jerry Garcia'
# >>> name.center(20)
# '    Jerry Garcia    '


# name = 'Paul York'
# name = "Paul York"
# naem = '''Paul York'''
# name = r'Paul\nYork'
# name = f'Paul York'

# >>> beat = 'Lennon,John,1940,1980'
# >>> beat.split(',')
# ['Lennon', 'John', '1940', '1980']
# >>> name = "Super Paul"
# >>> name.split(' ')
# ['Super', 'Paul']
# >>> name.split()
# ['Super', 'Paul']
# >>> name = "   SUPER    DUPER    PAUL    AWESOME   "
# >>> name.split()
# ['SUPER', 'DUPER', 'PAUL', 'AWESOME']
# >>> name.split(' ')
# ['', '', '', 'SUPER', '', '', '', 'DUPER', '', '', '', 'PAUL', '', '', '', 'AWESOME', '', '', '']
# >>> name = ",,,SUPER,,,DUPER,,,PAUL,,"
# >>> name.split()
# [',,,SUPER,,,DUPER,,,PAUL,,']
# >>> name.split(',')
# ['', '', '', 'SUPER', '', '', 'DUPER', '', '', 'PAUL', '', '']

from datetime import date

def printbeat(beat):
    parts = beat.split(',')    # ['Lennon','John','1940','1980']
    #print(parts[1] + ' ' + parts[0])
    fname = parts[1]
    lname = parts[0]
    fullname = f"{fname} {lname}"
    print(f"Name:{fullname:>20}")

    dob = int(parts[2])
    try:
        dod = int(parts[3])
        age = dod - dob
        fullage = f"{age} (dec.{dod})"
    except:
        # fullage = 2020 - dob
        fullage = date.today().year - dob

    #print(fullage)
    print(f"Age: {fullage:>20}")

beats = [
  'Lennon,John,1940,1980',
  'McCartney,Paul,1942,',
  'Harrison,George,1943,2001',
  'Starkey,Richard,1940,',
]

# printbeat(beats[0])
# printbeat(beats[1])
# printbeat(beats[2])
# printbeat(beats[3])

for b in beats:
    printbeat(b)
    print()

