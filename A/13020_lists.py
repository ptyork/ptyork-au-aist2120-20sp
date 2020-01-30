
names = []   # create an empty list
beatles = ['john','paul','george','george','george','george','ringo']  # pre-assign elements

'''
C => Create
R => Read
U => Update
D => Delete
'''
# READ (just reference the sucker)
print(beatles[2])
print(beatles[0])
print(beatles[6])
print(beatles[-1])

# UPDATE (assign to it)
beatles[1] = 'dead paul'

# CREATE
beatles.append('fake paul')   # adds to the END of the list
beatles.insert(0, 'pre-john')

print(beatles)

# DELETE
# beatles.clear()  # doh!!!
beatles.pop()   # delete last
print(beatles)
beatles.pop(0)  # delete first
print(beatles)
beatles.pop(2)  # delete element #3
print(beatles)
beatles.remove('george')   # remove a specific value
print(beatles)

# CHECK IF EXISTS
idx = beatles.index('george')
print(idx)
cnt = beatles.count('george')
print('there are ' + str(cnt) + ' georges')
if 'george' in beatles:
    print('yeah, george is here')
else:
    print('boo, george is dead')
beatles.pop(2)  # delete element #3
print(beatles)
beatles.remove('george')   # remove a specific value
print(beatles)
if 'george' in beatles:
    print('yeah, george is here')
else:
    print('boo, george is dead')

for i in range(len(beatles)):
    print(beatles[i] + ' is alive')


'''
IMMUTABLE COLLECTIONS
string
tuple
'''