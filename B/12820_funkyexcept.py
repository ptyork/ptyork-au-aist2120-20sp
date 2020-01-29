def input_int(prompt):
    while True:
        numstr = input(prompt)
        try:
            num = int(numstr)
            return num
        except:
            print("YOU STINKER")

num = input_int("Enter a number: ")
print(num + 1)
