'''
in C#

int counter = 0;
while (counter < 10)
{
    ....;
    counter++;
}

for (int counter = 0; counter < 10; counter ++)
{
    ....;
}

NOT HOW WE DO IT IN PYTHON

Python uses a "foreach" concept.

in C#:
int[] numbers....
foreach (int value in numbers)
{
    Console.Writeln(value);
}

in Python:
numbers = []
for value in numbers:
    print(value)

for char in 'hello':
    print(char)

'''

while True:
    print('='*20)
    print(' '*8 + 'MENU')
    print('-'*20)
    print('1) Do nothing')
    print('2) Count to 10')
    print('3) Count down from 10')
    print('4) Horizontal to Vertical')
    print('5) Count to 10 (for version)')
    print('6) Blastoff (for version)')
    print('0) Exit')
    print('-'*20)
    choice = input('Choice: ')
    if choice == '1':
        pass    # DO NOTHING
    elif choice == '2':
        counter = 0
        while counter < 10:
            print(counter+1)
            counter += 1
    elif choice == '3':
        counter = 10
        while counter > 0:
            print(counter)
            counter -= 1
        print('BLASTOFF!!!')
    elif choice == '4':
        word = input('Enter a word: ')
        for letter in word:
            #print(letter)
            #print(letter,end='')
            print(letter,end='-')
        print()
    elif choice == '5':
        # range(low,high) -- low is INCLUSIVE, high is EXCLUSIVE
        for num in range(1, 11):
            print(num)
    elif choice == '6':
        for num in range(10, 0, -1):
            print(num)
        print('BLASTOFF!!')
    elif choice == '0':
        break   # EXIT while True
    else:
        print('INVALID CHOICE!!!!!')

