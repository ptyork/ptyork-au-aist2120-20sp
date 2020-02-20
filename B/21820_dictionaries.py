# SEQUENCES
#   - collection of values
#   - iterable
#   - ORDERED
#   - numerically / positionally indexable
seq = []
seq = [1,3,5]
tup = ()
tup = (3,)
tup = (3,5,7)
st = ''
st = 'ABC'

names = ['Paul','Bob','Sally']
ages = [29,55,12]

for idx in range(len(names)):
    name = names[idx]
    age = ages[idx]
    print(name + ' is ' + str(age))


name = 'Bob'
idx = names.index(name)
age = ages[idx]
print(f'yep, {name} is {age}')

# Dictionary
#   KEY - UNIQUE ID for values in a dictionary (can be ANY data type)
#         NO DUPLICATES
#   VALUE - ANY value associated with the element (can be ANY data type)
#           DUPLICATES ARE OKAY
ducks = {}
# { KEY : VALUE, KEY : VALUE, ... }
ducks = {"Huey":'White','Dewey':'Yellow','Louie':'Brown'}
ducks = {
    "Huey":'White',
    'Dewey':'Yellow',
    'Louie':'Brown',
    8: False,
    5.2: [1,2,3],
}

print(ducks)

# CRUD (create, read, update, delete)

# READ (access an element of a dictionary)
print(ducks['Huey'])
print(ducks[8])

# UPDATE
# ducks[2] = 'LOOEY'
ducks['Louie'] = 'Red'
print(ducks)

# CREATE (add new entries)
print('Scrooge' in ducks)
ducks['Scrooge'] = 'Gold'
print('Scrooge' in ducks)
print(ducks)

# DELETE
#ducks.pop()
ducks.pop(8)
del ducks[5.2]
print(ducks)
