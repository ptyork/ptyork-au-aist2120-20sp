# Deeper Dive into Dictionaries

friends = [
    'Barney',
    'Dora',
    'Mr. Rogers',
    'Dory',
    'Mickey Mouse',
    'Fred Flintstone',
]
phones = [
    '5551212',
    '6661313',
]
phonebook = {
    'Barney': '5551212',
    'Dora': '6661313',
    'Mr. Rogers': '7771414',
    'Dory': '8881515',
    'Mickey Mouse': '9991616',
    'Fred Flintstone': '2221717',
}
wishlist = {
    'Barney': [],
    'Dora': [],
    'Mr. Rogers': [],
    'Dory': [],
    'Mickey Mouse': [],
    'Fred Flintstone': [
        'New Gown',
        'New Tie',
        'Rock Wheels',
        'Calous Scraper',
    ],
}

print(friends[5])                     # print a value from a list
print(phonebook['Fred Flintstone'])   # print a value from a dictionary

print(wishlist['Fred Flintstone'])
print(wishlist['Fred Flintstone'][0])
freds_list = wishlist['Fred Flintstone']
print(freds_list[0])

print('All of Fred\'s Wishlist Items')
for item in wishlist['Fred Flintstone']:
    print(item)

contacts = {
    'Barney': {
        'Home Phone': '5551212'
    },
    'Dora': {
        'Home Phone': '6661313'
    },
    'Mr. Rogers': {},
    'Dory': {},
    'Mickey Mouse': {},
    'Fred Flintstone': {
        'Home Phone': '2221717',
        'Work Phone': '9999999',
        'Date of Birth': '4/20/-12120',
        'Spouse': 'Wilma',
        'Kids': [
            'Pebbles',
            'Stoner',
        ],
    },
}

# import pprint
# pprint.pprint(...)
# from math import sqrt
# sqrt(4)
# from pprint import pprint
# pprint(...)
from pprint import pprint as pp

pp(contacts['Fred Flintstone'])
print(contacts['Fred Flintstone']['Work Phone'])
fred = contacts['Fred Flintstone']
print(fred['Work Phone'])
for kid in fred['Kids']:
    print(kid)
for kid in contacts['Fred Flintstone']['Kids']:
    print(kid)
print(contacts['Fred Flintstone']['Kids'][1])


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
        if 'Home Phone' in c:
            phone = c['Home Phone']
            print(f"{name:<40}{phone:>20}")


def print_contact_info(name):
    global contacts
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


while True:
    print()
    print('MENU')
    print('----')
    print('1) Print All Contacts')
    print('2) Print Home Phone List')
    print('3) Print Contact Info')
    print('0) EXIT')

    choice = input('Selection: ')
    if choice == '1':
        print_contacts()
    elif choice == '2':
        print_home_phone_list()
    elif choice == '3':
        name = input("FOR WHICH CONTACT: ")
        print_contact_info(name)
    elif choice == '0':
        break  # or exit()

