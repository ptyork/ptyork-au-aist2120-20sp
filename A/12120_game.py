from random import randint
answer = randint(1, 100)

#print(answer)

while True:
    guess = int(input('Enter your guess: '))
    if guess == answer:
        print("YOU WIN!!!!")
        break
    elif guess < answer:
        print("TOO LOW")
    elif guess > answer:
        print("TOO HIGH")
print('Bye Felicia')

