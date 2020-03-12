contacts = {}
    #  'phoebe' : {
    #      'home': '5551212',
    #      'work': '1212555',
    #      'age': 23,
    #      'email': 'smellycat@names.stink',
    #  },

from pprint import pprint as pp

def load_contacts():
    global contacts
    filename = 'friends.txt'
    with open(filename) as fi:
        fi.readline()  # ignore the first line
        # lines = fi.readlines()
        # for line in lines:
        for line in fi: # read line by line to the end
            line = line.strip()
            if not line:  # ship blank lines
                continue
            details = line.split('|')
            # pp(details)
            friendname = details[0].upper()
            contacts[friendname] = {}
            contacts[friendname]['NAME'] = details[0]
            contacts[friendname]['PHONE'] = details[1]
            contacts[friendname]['ADDRESS'] = details[2]
            contacts[friendname]['CITY'] = details[3]
            contacts[friendname]['STATE'] = details[4]
            contacts[friendname]['ZIP'] = details[5]
            contacts[friendname]['EMAIL'] = details[6]
        # pp(contacts)


def show_contacts():
    global contacts
    print("CONTACT LIST".center(60))
    print(f"{'CONTACT LIST':^60}")
    print("-" * 60)
    #for key in contacts:
    for key in contacts.keys():  # contacts.values()
        print(key)

def show_home_phone_list():
    global contacts
    print("PHONE LIST".center(60))
    print("-" * 60)
    for key in contacts:
        #phone = contacts[key]['PHONE']
        cont = contacts[key]    # { 'PHONE': 'blah' }
        if 'PHONE' in cont:
            phone = cont['PHONE']   # 'blah'
        else:
            phone = 'N/A'
        print(f"{key:<40}{phone:>20}")


def show_contact_details(contact_name):
    global contacts
    contact_name = contact_name.upper()
    if contact_name in contacts:
        cont = contacts[contact_name]
        print("CONTACT DETAILS".center(60))
        print("-" * 60)
        for attr_name in cont.keys():
            attr_val = cont[attr_name]
            print(f'{attr_name.title():<30}{attr_val:>30}')
    else:
        print("Ain't no contact by that name round here")


def edit_contact(contact_name):
    global contacts
    contact_name = contact_name.upper()
    if contact_name in contacts:
        cont = contacts[contact_name]
        show_contact_details(contact_name)
        key = input("Edit what: ").upper()

        if key not in cont:
            print('NO KEY WITH THAT NAME')
            return

        value = input("Change to what: ")
        # contacts[contact_name][key] = value
        cont[key] = value
        show_contact_details(contact_name)
    else:
        print("Ain't no contact by that name round here")


def save_contacts():
    global contacts
    filename = 'friends.txt'
    with open(filename, 'w') as fi:
        # print('Name|Phone|Address|City|State|Zip|Email', file=fi)
        fi.write('Name|Phone|Address|City|State|Zip|Email\n')
        # for key in contacts:
        #     cont = contacts[key]
        for cont in contacts.values():
            # pp(cont)
            line = cont['NAME']
            line += '|' + cont['PHONE']
            line += '|' + cont['ADDRESS']
            line += '|' + cont['CITY']
            line += '|' + cont['STATE']
            line += '|' + cont['ZIP']
            line += '|' + cont['EMAIL']
            # attributes = cont.values()
            # pp(attributes)
            # line = '|'.join(attributes)
            # print(line)
            fi.write(line + '\n')

while True:
    print()
    print("MENU")
    print("====")
    print('L) Load Contacts')
    print("1) Show Contacts")
    print("2) Show Home Phone List")
    print("3) Show Contact Details")
    print('4) Edit a Contact')
    print('S) Save Contacts')

    print("0) Exit")    
    choice = input("Enter choice: ")
    if choice == '1':
        show_contacts()
    elif choice == '2':
        show_home_phone_list()
    elif choice == '3':
        name = input('Which contact: ')
        show_contact_details(name)
    elif choice == '4':
        name = input('Which contact: ')
        edit_contact(name)
    elif choice.casefold() == 'L'.casefold():
        load_contacts()
    elif choice.lower() == 's':
        save_contacts()
    elif choice =='0':
        break   # exit()
    else:
        print('DUMBASS!!')


