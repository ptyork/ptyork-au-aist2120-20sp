'''
scope: where / how long a variable exists / holds its value.

global scope (supports, but not by default)
function scope - variable is in function only
                 recreated each call
block scope - c#'s default...kinda sometimes in Python
sequential scope (paul's made up term)
'''

# print(a) # bad b/c a not yet defined
a = 5
print(a)

def test1():
    # print(a)
    # a = a + 2
    a = 7
    print(a)


def test2():
    global a
    a = a + 5
    print(a)

test1()
print(a)
test2()
test2()
print(a)


num = 3

def test3(num):
    print(num)

test3(6)
print(num)

def test4(num):
    num = num + 10
    print(num)

test4(10)
print(num)


