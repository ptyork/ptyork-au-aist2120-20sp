'''
OLD C# WAY:

int cnt = 0;
while (cnt < 10)
{
    ......;
    cnt++;
}

for (int cnt = 0; cnt < 10; cnt++)
{
    ......;
}

int[] nums = [1,2,3];
foreach (int num in nums)
{
    Console.Writeln(num);
}


'''

while True:
    print("="*20)
    print(" "*8 + "MENU")
    print('-'*20)
    print('1) Do nothing')
    print('2) Count to 10')
    print('3) Count to N')
    print("4) Blastoff")
    print('5) Horizontal to Vertical')
    print("6) Count to 10 (for)")
    print("7) Count evens to 20")
    print("8) Blastoff (for)")
    print('0) Exit')
    print('-'*20)
    choice = input('Enter choice: ')

    if choice == "1":
        pass
    elif choice == "2":
        counter = 0
        while counter < 10:
            print(counter + 1)
            counter += 1
    elif choice == "3":
        n = int(input("enter n: "))
        counter = 0
        while counter < n:
            print(counter + 1)
            counter += 1
    elif choice == "4":
        counter = 10
        while counter > 0:
            print(counter)
            counter -= 1
        print('Blastoff!!!')
    elif choice == "5":
        word = input('input word: ')
        for ch in word:
            print(ch) # defAult = print(ch, end='\n')
            # print(ch, end='')
            # print(ch, end='-')
        print()
    elif choice == "6":
        nums = range(1, 11)  # range(low, high) --- start is INCLUSIVE, end is EXCLUSIVE
        #for num in nums:
        for num in range(1,11):
            print(num)
    elif choice == "7":
        for num in range(2,21,2):
            print(num)
    elif choice == "8":
        for num in range(10,0,-1):
            print(num)
        print('blastoff!!!')
    elif choice == "0":
        break
    else:
        print('Invalid choice!!!')
    

