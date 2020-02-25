x = 'now is the time for all good students to pay attention.'

'boba fett' in x   # boolean expression
'time' in x

x.find('time')    # location or -1
x.index('time')   # location or BOOOOOOMMMM


x = 'Please contact me by email at paul.york@augusta.edu at your earliest convenience or twitter @ @ptyork or @@ tattoine or paul@yorkie'

for word in x.split():
    if '@' in word:
        # print(word) # potential email address
        
        parts = word.split('@')
        # print(parts)
        # has right number of @'s
        if len(parts) != 2:
            print(f'{word} has too many @s')
            continue
        
        # each part is not empty
        if len(parts[0]) == 0 or len(parts[1]) == 0:
            print(f'{word} has too few parts')
            continue
        
        # domain name is valid
        domain = parts[1]
        dparts = domain.split('.')
        if len(dparts) < 2:
            print(f"{word} has a bad domain name")
            continue
        
        # Assume all is good
        print(f'{word} is an email address')


