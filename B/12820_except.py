if 5 > 5:
    print('huh?')


while True:
    numstr = input("Enter a number: ")

    if len(numstr) != 1:
        print("YOU STINK")
        continue

    numord = ord(numstr)

    if numord < 48 or numord > 57:
        print("YOU SUCK")
    else:
        break

num = int(numstr)

if num > 5:
    print('too big')
elif num < 5:
    print('too small')
else:
    print('just right')





while True:
    numstr = input("Enter a number: ")
    try:
        num = int(numstr)
        break
    except:
        print("YOU STINKER")

if num > 5:
    print('too big')
elif num < 5:
    print('too small')
else:
    print('just right')

