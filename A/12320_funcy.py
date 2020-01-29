'''
In C#:

public Class something
{
    public void PrintMe(string stuff)
    {
        ....;
    }

    public double Sum(double a, double b)
    {
        .....;
        return ...;
    }
}

'''
from random import randint

def prit(stuff):
    print(stuff, end='')

def test():
    num = randint(1,2)
    if num == 2:
        return
    print('goodbye')

def sum(a, b):
    s = a + b
    return s

# return    ONLY USE IN A FUNCTION DEFINITION

prit('H')
prit('e')
print('llo')

prit(12.5)
prit(True)
prit(5>6)
prit('A'+"B")

# test()

# def test():    # BETTER TO DEFINE UP TOP
#     print('goodbye')

t = sum(5,6)
prit(t)

test()


