'''
BOOLEAN:
  True, False

COMPARISON OPERATORS:
  ==, !=, >, >=, <, <=

BOOLEAN MOIFIER:
  not 

COMPOUND EXPRESSIONS:
  and (logical and)  && in C#
  or (logical or)    || in C#

BRANCHING LOGIC:
C#:
  if (CONDITION) 
  {
      DO SOMETHING IF TRUE;
      DO SOMETHING ELSE;
  }
  else
  {
      DO SOMETHING IF FALSE;
  }

CODE BLOCK:
  grouping of statements that all run or don't run


LOOPING:
C#:
  while *
  do/while
  for
  foreach *

GET OUT OF INFINITE LOOP:
  Ctrl+C
  break
  continue

'''

x = 5
if x > 5:
    print('x is big')
    print('yep, it\'s big alright')
print('DONE!!')


x = 10000
if x > 5:
    print('x is STILL big')
else:
    print('nope, x is SMALL')

print('STILL DONE!!')


y = 77
if y > 50 and y < 70:
    print('YEP')
else:
    print('NOPE')

if y < 50 or y > 70:
    print('YEP')
else:
    print('NOPE')



# LOOPING


x = 10
while x >= 5:
    print('I\'m at ' + str(x))
    x -= 1
print('DONE!!')


# TRUTHINESS
#   0        equivalent to False
#   not 0    equivalent to True
#   len == 0 equivalent to False
#   len != 0 equivalent to True

name = input('Enter your name')
if not name:
    print("I SAID ENTER YOUR NAME!!!")



while True:
    print('GET ME OUT OF HERE!!!')
    break
    #continue
    #exit()
    print("PLEASE")

while True:
    ans = input('What is the answer to life, the universe and everything? ')
    if ans == '42':
        break
    else:
        print("RONG!!!")

print("THANKS!!")
