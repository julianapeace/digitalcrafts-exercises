import pickle

def phonebookapp():
    phonebook = {}
    try:
        menu = int(input("""Electronic Phone Book
    =====================
    0. Load saved entries
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save Entries.
    6. Quit
    What do you want to do (0-6)?
    """))
    except ValueError:
        print("Oops!  That is not an option.  Try again...")
        phonebookapp()
    else:
        while menu != 6:
            if menu == 1:
                try:
                    name = str(input("What is the name?"))
                    print("Found entry for",name, ":",phonebook[name])
                except KeyError:
                    print("No entry found")
                    phonebookapp()
            elif menu == 2:
                name = str(input("Name:"))
                number = input("Phone Number:")
                email = input("Email address:")
                website = input("Website:")
                phonebook[name] = {'Name': name, 'Phone number': number, 'Email': email, 'Website': website}
                print("Entry stored for", name)
            elif menu == 3:
                try:
                    name = str(input("Name?"))
                    del phonebook[name]
                    print("Deleted entry for", name)
                except KeyError:
                    print("No entry found")
                    phonebookapp()
            elif menu == 4:
                for i in phonebook:
                    print("Found entry for", i, ":", phonebook[i])
            elif menu == 5:
                fh = open('phonebook.pickle', 'wb')
                pickle.dump(phonebook, fh)
                fh.close()
            elif menu == 0:
                fh = open('phonebook.pickle', 'rb')
                phonebook = pickle.load(fh)
            menu = int(input("""Electronic Phone Book
            =====================
            0. Load saved entries
            1. Look up an entry
            2. Set an entry
            3. Delete an entry
            4. List all entries
            5. Save Entries.
            6. Quit
            What do you want to do (0-6)?
            """))
        print("Bye!")

phonebookapp()
