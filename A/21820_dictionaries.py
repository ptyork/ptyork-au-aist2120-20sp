ls = []
ls = [1,2,3]
tup = ()
tup = (1,2,3)
st = ''
st = '123'


ducks = ['Huey','Dewey','Louie']
colors = ['White','Yellow','Green']


# for duck in ducks:
#     print(duck + ' is ' + color)

for idx in range(len(ducks)):
    print(ducks[idx] + ' is ' + colors[idx])


d = {'Huey': 'White', 'Dewey': 'Yellow', 'Louie': 'Green'}

d = {
    'Huey': 'White',
    'Dewey': 'Yellow',
    'Louie': 'Green',
    7: 9
}

# reference a value (READ)
print('Dewey is coloured ' + d['Dewey'])

# change a value (UPDATE)
print(d)
d['Louie'] = 'Brown'
print(d)

# add a value to the dictionary (CREATE)
# d.dontuseafunction()
d['Scrooge'] = 'Gold'
print(d)

#d.pop()
d.pop('Louie')
del d[7]
print(d)

# iterate of a dictionary keys + values
for key in d:
    #print(key)
    val = d[key]
    print(key + ' is ' + val)

print(d.keys())

for key in d:
    d[key] = 'blue'
    print(d)

