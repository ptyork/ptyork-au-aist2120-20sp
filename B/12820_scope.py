'''
scope: when, where and how a variable is accessed in code

global scope: access from everywhere
function (local) scope: variables/parameters defined in a
  function are ONLY accessable inside a function
block scope: C# available inside of curly braces (blocks)
sequence scope: BS word

'''

# print(a)   BAD (must declare first for it to be in scope)
a = 5
print(a)

def test1():
    print(a)    # read a from global scope

test1()

def test2():
    a = 2
    a = a + 5
    print(a)

test2()
print(a)

balance = 100.0

def deposit(amt):
    global balance
    balance += amt

def withdraw(amt):
    global balance
    balance -= amt

def showbal(balance):
    print(balance)

showbal(42)

print(balance)
deposit(50)
withdraw(25)
print(balance)



name = input("Enter name: ")

if name.upper() < "M":
    advisor = "Joe"
else:
    advisor = "Jill"

print(advisor)



