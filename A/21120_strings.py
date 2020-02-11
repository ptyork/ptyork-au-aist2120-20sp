# Cool captialization string methods
#  upper, lower, title, capitalize

# Removing superfluous spaces
#  strip, lstrip, rstrip

# Find/Replace
#  find, index, replace
#  'substring' in 'mainstring' (BOOLEAN EXPRESSION)

# >>> name
# 'Paul York'
# >>> person
# 'York,Paul,47'
# >>> person.split(',')
# ['York', 'Paul', '47']
# >>> parts = person.split(',')
# >>> parts[1]
# 'Paul'
# >>> name.split(' ')
# ['Paul', 'York']
# >>> name.split()
# ['Paul', 'York']
# >>> name = '   paul     york    '
# >>> name.split()
# ['paul', 'york']
# >>> name = ',,,,paul,,,,york,,,,'
# >>> name.split()
# [',,,,paul,,,,york,,,,']
# >>> name.split(',')
# ['', '', '', '', 'paul', '', '', '', 'york', '', '', '', '']

# >>> beat = "John Lennon"
# >>> beat
# 'John Lennon'
# >>> beat.rjust(20)
# '         John Lennon'
# >>> beat = "Paul York"
# >>> beat.rjust(20)
# '           Paul York'
# >>> beat.ljust(20)
# 'Paul York           '
# >>> beat.center(20)
# '     Paul York      '


name = 'Paul'
name = "Paul"
name = '''Paul'''
name = r'Paul\York'
name = f'Paul'




# CHALLENGE

from datetime import date

def printbeat(beat):
    parts = beat.split(',')   # ['Lennon','John','1940','1980']
    #print(parts[1] + ' ' + parts[0])
    fullname = f'{parts[1]} {parts[0]}'
    # print(fullname)
    # print("Name:" + fullname.rjust(20))
    print(f"Name:{fullname:>20}")

    born = int(parts[2])
    try:
        died = int(parts[3])
        age = died - born
        agestring = f"{age} (dec.{died})"
    except:
        year = date.today().year
        age = year - born
        #agestring = f"{age}"
        agestring = str(age)

    print(f'Age: {agestring:>20}')

#beat = 'Lennon,John,1940,1980'

beats = [
  'Lennon,John,1940,1980',
  'McCartney,Paul,1942,',
  'Harrison,George,1943,2001',
  'Starkey,Richard,1940,',
]

for b in beats:
    printbeat(b)
    print()

