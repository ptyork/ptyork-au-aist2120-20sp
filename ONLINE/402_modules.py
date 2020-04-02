# import mod   # requires prefix!!! (e.g., mod.get_text() )
from mymodules.inputfuncs import get_text, get_int, default_prompt

print("Hi there, my name is Siry")
name = get_text("What is your name: ")
print(f"Oh, hi {name}. Very pleased to meet you.")
age =  get_int("How old are you: ")
siry_age = 3
diff = age - siry_age
if diff > 0:
    print(f"Ohhhh. You're so old. I'm {siry_age} years old. That's {diff} years younger than you're old butt.")
elif diff < 0:
    print("You're just baby!!")
else:
    print("Oh how special, we're the same age!!")

print(default_prompt)
