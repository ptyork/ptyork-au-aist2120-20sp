from pprint import pprint as pp
import shelve

##### We're replacing the Python dictionary with a shelf.
##### In theory, it is a "drop-in" replacement. And it
##### is in reality, unless you screw up. See below.
# contacts = {}
    #  'phoebe' : {
    #      'name': 'Phoebe',
    #      'home': '5551212',
    #      'work': '1212555',
    #      'age': 23,
    #      'email': 'smellycat@names.stink',
    #  },


##### Use the "with" command and indent the entire
##### script below to avoid the need to manually
##### close your shelf.

#contacts = shelve.open('contacts.db')
with shelve.open('contacts.db') as contacts:

    def add_contact():
        global contacts
        name = input('Enter a name:')
        #key = name.lower()
        key = name

        if key in contacts:
            print('ALREADY EXISTS YOU DOLT!!')
            return

        ##### THIS LINE IS WHERE IS SCREWED UP IN THE LECTURE.
        ##### YOU HAVE TO CREATE A DICTIONARY FOR THE CONTACT
        ##### BEFORE YOU CAN ACTUALLY START ADDING DATA TO IT.
        contacts[key] = {}

        ##### ALSO I CHANGED THE KEYS TO BE ALL UPPERCASE TO
        ##### MATCH WHAT I DID IN THE CODE BELOW. SO YEAH, THE
        ##### NAME KEY IS LOWERCASE BUT THE CONTACT DETAIL KEYS
        ##### ARE UPPER CASE...WHATEVER...
        contacts[key]['NAME'] = name
        phone_number = input('Enter Phone Number:')
        contacts[key]['PHONE'] = phone_number
        age = input('Enter Age:')
        contacts[key]['AGE'] = age
        email = input('Enter Email:')
        contacts[key]['EMAIL'] = email


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


    while True:
        print()
        print("MENU")
        print("====")
        print("1) Show Contacts")
        print("2) Show Home Phone List")
        print("3) Show Contact Details")
        print('4) Edit a Contact')
        print('5) Add a Contact')

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
        elif choice == '5':
            add_contact()
        elif choice =='0':
            break   # exit()
        else:
            print('DUMBASS!!')


#contacts.sync()     # save without closing

##### Don't need to close since we use the with block
#contacts.close()    # save and close

