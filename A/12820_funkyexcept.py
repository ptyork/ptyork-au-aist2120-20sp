def input_int(prompt):
    while True:
        inp = input(prompt)
        try:
            int_inp = int(inp)
            return int_inp
        except:
            print("NOT AN INTEGER")


x = input_int("ENTER A NUM: ")
print(x)
y = input_int("")
print(y)
