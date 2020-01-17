'''
Booleans
  * True, False
Comparison
  >, <, ==, >=, <=, !=
Compound
  and, or
Truthy

BRANCHING:
C#
  if (x > 5) {
      DO STUFF
  }
  else
  {
      DO OTHER STUFF
  }
Python (see below)

CODE BLOCK:
  group of statements that can be expected to execute together
  or not at all

LOOPING:
C#
  while (x > 5)
  {
      DO STUFF
  }

INFINITE LOOP:
  Ctrl+C is your FRIEND

TERMINATION
  break, exit(), continue *
  * doesn't REALLY terminate...skips the rest and restarts


'''
x = 4
x = 10
if x > 5:
    print("It's big!")
    print("really big!")
else:
    print("It's small")
print("Done")


while x >= 5:
    print("It's Loopy big " + str(x))
    x -= 1


while True:
    print('HELLLLLLP. I\'m trapped')
    stop = input('Do you want my help? ')
    if stop == 'yes':
        break      # EXITS LOOP
        # exit()     EXITS SCRIPT
        # continue
    print("I cant' stop")

print("REALLY DONE")

# TRUTHINESS

print(len('big'))
print(len('small'))
print(len(''))

if 'hello':
    print('SAY Wha!?!')

if len('hello') > 0:
    print('SAME THING')


if '':
    print('SAY who?!?')


if 1:
    print('HUH??')

if 0:
    print("WHO??")

