data = {}

while True:
    command = input("Pick an option: new_contact, show_contacts")
    if command == "new_contact":
        fal_name = input("Podaj imię i nazwisko:")
        number = input("podaj numer telefonu:")
        data[fal_name] = number
    elif command == "show_contacts":
        print(number)
    # else:
    #     print("Unknown command")
    command = input("Do you want to continue Y/N?")
    if command == "N":
        break

