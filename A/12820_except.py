while True:
    guess = input("Enter a number: ")
    if len(guess) != 1:
        print("A SINGLE DIGIT NUMBER!!!")
        continue

    ord_guess = ord(guess)

    if ord_guess < 48 or ord_guess > 57:
        print('A NUMBER!!!!')
    else:
        break

number_guess = int(guess)

if number_guess == 7:
    print("yep")
elif number_guess < 7:
    print('low')
else:
    print('high')


while True:
    guess = input("Enter a number: ")
    try:
        number_guess = int(guess)
        break
    except:
        print("A NUMBER!!!!")

if number_guess == 7:
    print("yep")
elif number_guess < 7:
    print('low')
else:
    print('high')
