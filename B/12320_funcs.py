'''
How we did it in C#:

public class Printer
{
    public void PrintSomething(string text)
    {
        .....;
    }

    public double Add(double a, double b)
    {
        .....;
        return a + b;
    }
}
'''
from random import randint

def write(text):
    print(text, end='')

def test():
    num = randint(1,2)
    if num == 1:
        return
    print("Paul wuz here")

def add(a,b):
    sum = a + b
    return sum

write('H')
write('e')
print('llo')

write(12)
write(132.7)
write(True)
write(5>6)
write(12==6+2+4 and 5==6-1)
write('I'+' am '+' not '+'bored')

bogus = test()

x = add(5,6)
y = add(x,2)
print(y)

a = add(1,2)

print(bogus)

# print(add(1,1))
# print(add)
# add = 3
# print(add)
# print(add(1,1))
# print = 1

# def test():   # DEFINE FUNCS AT THE TOP IS BEST PRACTICE
#     print("Paul wuz here")


