# using ....
from random import randint

ans = randint(1,100)

while True:
    guss = int(input('Enter you guss: '))
    if guss == ans:
        print('YOU GOT IT!!')
        break
    elif guss > ans:
        print("GUESS LOWER")
    elif guss < ans:
        print('GUESS HIGHER')

print('buh bye')

