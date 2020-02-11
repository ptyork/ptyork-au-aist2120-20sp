# ITERATING OVER... WELL, ITERABLES

pets = ['dog', 'cat', 'bird']

# iterating over list using indexes
for i in range(len(pets)):
    print('I have a ' + pets[i])

# iterate over a list WITHOUT indexes
for item in pets:
    print('I have a ' + item)

string = "Python"

# iterate over a string and print each character
for ch in string:
    print(ch)

# How is iterating over a list of strings different from iterating over a single string?
#       iterating over list of strings iterates over each string as an item of the list
#       iterating over single string iterates over the characters of the string

nums = [5, 2, 3]

# iterate over list of nums and add them together
total = 0
for num in nums:
    total += num
print('TOTAL: ' + str(total))

# average of list of numbers function
def average(num_list):
    total = 0
    for num in num_list:
        total += num
    avg = total / len(num_list)
    return avg

nums = [2, 4, 6, 8, 10]

print(average(nums)) # use a variable representing a list of nums as argument
print(average([10, 2, 4, 4])) # use just a list of nums not assigned to a variable as argument

# OK BUT WHAT HAPPENS WITH AN EMPTY LIST??
def average2(num_list):
    total = 0
    try:
        for num in num_list:
            total += num
        avg = total / len(num_list)
        return avg
    except:
        print("Please use a non-empty list.")

print(average2([]))

# SLICING

# list_name[start, stop, step]
# How does this compare to the range function? SAME ARGUMENTS!!!

# slicing a string
name = 'Shelby Fink'

print(name[7])                         # First letter of last name
print(name[:6])                        # First name
print(name[7:11])                      # Last name
print(name[7:] + ', ' + name[0])       # Last, First initial
print(name[11:6:-1])                   # Last name but backwards

# slicing a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[0:10])
print(nums[:])       # same as above - THE WHOLE LIST
print(nums[0:4])     # first 4 numbers (index 0 to index 3)
print(nums[:8])      # first 8 numbers (index 0 to index 7)
print(nums[7:])      # last 3 numbers (index 7 to index 9)
print(nums[-3:])     # last 3 numbers also
print(nums[1::2])    # even numbers
print(nums[::2])     # odd numbers
print(nums[::-1])    # whole list in REVERSE
