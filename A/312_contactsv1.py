from pprint import pprint as pp

contacts = {}
    # 'Fred Flintstone': {
    #     'Name': 'Fred Flintstone',
    #     'Home Phone': '2221717',
    #     'Work Phone': '9999999',
    #     'Date of Birth': '4/20/-12120',
    #     'Spouse': 'Wilma',
    # },


def load_contacts():
    global contacts
    filename = 'friends.txt'
    with open(filename) as fi:
        line = fi.readline().strip()
        keys = line.split('|')
        print(keys)
        # lines = fi.readlines()
        # pp(lines)
        # for line in lines:
        for line in fi:
            line = line.strip()
            vals = line.split('|')
            # print(vals)
            name = vals[0].upper().strip()
            contacts[name] = {}
            contacts[name]['Name'] = vals[0].strip()
            contacts[name]['Phone'] = vals[1].strip()
            contacts[name]['Address'] = vals[2].strip()
            contacts[name]['City'] = vals[3].strip()
            contacts[name]['State'] = vals[4].strip()
            contacts[name]['Zip'] = vals[5].strip()
            contacts[name]['Email'] = vals[6].strip()
            # {
            #     'Chandler Bing' : {
            #         'Name': 'Chandler Bing',
            #         ...
            #     }
            # }
        pp(contacts)

def save_contacts():
    global contacts
    filename = 'friends.txt'
    with open(filename, 'w') as fi:
        fi.write('Name|Phone|Address|City|State|Zip|Email\n')
        for key in contacts:
            friend = contacts[key]
            # pp(friend)
            # pp(friend.values())
            friendstring = '|'.join(friend.values())
            print(friendstring)
            fi.write(friendstring + '\n')


def print_contacts():
    global contacts
    print("CONTACT LIST")
    print("=" * 12)
    for name in contacts.keys():   # same as for name in contacts
        print(name)

def print_home_phone_list():
    global contacts
    print("PHONE LIST".center(60))
    print(f"{'PHONE LIST':^60}")
    print("=" * 60)
    for name in contacts.keys():
        c = contacts[name]   # Entire dictionary of info about "name"
        if 'Phone' in c:
            phone = c['Phone']
            print(f"{name:<40}{phone:>20}")


def print_contact_info(name):
    global contacts
    name = name.upper()
    if name in contacts:
        cont = contacts[name]
        for attr_name in cont:
            # print(attr_name)
            val = cont[attr_name]
            if type(val) is not list:
                print(f"{attr_name:<30}{val:>30}")
            else:
                for kid in val:
                    print(f"{attr_name:<30}{kid:>30}")
    else:
        print('You ain\'t got a friend by that name')


def edit_contact_info(name):
    global contacts
    name = name.upper()
    if name in contacts:
        print_contact_info(name)
        cont = contacts[name]
        key = input('What do you want to change: ')
        value = input('What do you want to change it to: ')
        cont[key] = value
        print_contact_info(name)
    else:
        print('You ain\'t got a friend by that name')



while True:
    print()
    print('MENU')
    print('----')
    print('L) Load Contacts')
    print('1) Print All Contacts')
    print('2) Print Home Phone List')
    print('3) Print Contact Info')
    print('4) Edit Contact Info')
    print('S) Save Contacts')
    print('0) EXIT')

    choice = input('Selection: ')
    if choice.upper() == 'L':
        load_contacts()
    elif choice == '1':
        print_contacts()
    elif choice == '2':
        print_home_phone_list()
    elif choice == '3':
        name = input("FOR WHICH CONTACT: ")
        print_contact_info(name)
    elif choice == '4':
        name = input("FOR WHICH CONTACT: ")
        edit_contact_info(name)
    elif choice.upper() == 'S':
        save_contacts()
    elif choice == '0':
        break  # or exit()

