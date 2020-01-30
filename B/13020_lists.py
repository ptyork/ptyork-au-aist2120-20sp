'''
C => Create
R => Read
U => Update
D => Delete
'''

nums = []
nums = [0]
nums = [7,5,3]

print(nums[1])
print(nums[0])
#print(nums[3]) index out of bounds

names = ['john','paul','george','george','george','george','george','bob']

# READ
print(names)
aname = names[1]
print(aname)

# UPDATE
names[1] = 'fake paul'
print(names)
# names[0] = 13
# print(names)
# names[2] = print
# names[2]('hello world')

# CREATE
names.append('ringo')
print(names)
names.insert(0, 'paul\'s mom')
print(names)

# DELETE
names.pop(0)  # remove paul's sad little mom
aname = names.pop()   # remove ringo
print(aname)
print(names)
# names.remove('ringo')
# print(names)
names.remove('george')
print(names)

# LOOKUP / QUERY

print(len(names))
georges = names.count('george')
print(georges)


#while names.count('george') > 0:
while 'george' in names:
    names.remove('george')
print(names)


'''
MUTABLE == Changeable
list

IMMUTABLE == Read-Only
string
tuple

'''

names_ro = ('john','paul','george')   #  NOT [] but ()

print(names_ro[1])

names_ro[1] = 'goat'

