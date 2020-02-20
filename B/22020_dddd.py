# Deeper Dive into Data structures and Dictionaries

friends = [
    'phoebe',
    'chandler',
    'rachael',
    'monica',
    'joey',
    'ross',
]
phones = {
    # KEY : VALUE
    'phoebe' : '5551212',
    'chandler': '6661313',
    'rachael': '7771414',
    'monica': '8881515',
    'joey': '9991616',
    'ross': '2221717',
}
multiphones = {
    'phoebe' : ['5551212','1212555'],
    'chandler': ['6661313','1313666'],
    'rachael': ['7771414'],
    'monica': ['8881515'],
    'joey': ['9991616'],
    'ross': ['2221717'],
}

print(friends[1])

print(phones['chandler'])

print(multiphones['chandler'][1])   #phone
chandphones = multiphones['chandler']  #list
print(chandphones[1])   #phone

print("Phoebe Phones")
for phone in multiphones['phoebe']:
    print(phone)


contacts = {
     'phoebe' : {
         'home': '5551212',
         'work': '1212555',
         'age': 23,
         'email': 'smellycat@names.stink',
         'pets': ['smelly','stinky','ribbit']
     },
    'chandler': {
        'home': '6661313',
        'work': '1313666',
        'age': 31,
    },
    'rachael': {
        'home': '7771414'
    },
    'monica': {
        'home': '8881515'
    },
    'joey': {
        'home': '9991616'
    },
    'ross': {
        'work': '2221717'
    },
}

#import a library
import math
print(math.sqrt(5))
from math import sqrt, acos
print(sqrt(5))
from math import sqrt as rt
print(rt(5))
print(5**0.5)

from pprint import pprint as pp

pp(contacts)
pp(contacts['phoebe'])
print(contacts['phoebe']['email'])
phoebe = contacts['phoebe']
phoebes_email = phoebe['email']
print(phoebes_email)

print(contacts['phoebe']['pets'][2])


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
        #phone = contacts[key]['home']
        cont = contacts[key]    # { 'home': 'blah' }
        if 'home' in cont:
            phone = cont['home']   # 'blah'
        else:
            phone = 'N/A'
        print(f"{key:<40}{phone:>20}")


def show_contact_details(contact_name):
    global contacts
    if contact_name in contacts:
        cont = contacts[contact_name]
        print("CONTACT DETAILS".center(60))
        print("-" * 60)
        for attr_name in cont.keys():
            attr_val = cont[attr_name]
            if not type(attr_val) is list:
                print(f'{attr_name:<30}{attr_val:>30}')
            else:   # attr_val is a list
                for pet in attr_val:
                    print(f'{attr_name:<30}{pet:>30}')
    else:
        print("Ain't no contact by that name round here")


while True:
    print()
    print("MENU")
    print("====")
    print("1) Show Contacts")
    print("2) Show Home Phone List")
    print("3) Show Contact Details")

    print("0) Exit")    
    choice = input("Enter choice: ")
    if choice == '1':
        show_contacts()
    if choice == '2':
        show_home_phone_list()
    if choice == '3':
        name = input('Which contact: ')
        show_contact_details(name)
    elif choice =='0':
        break   # exit()


