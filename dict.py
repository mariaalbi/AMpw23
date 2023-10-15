#wprowadzic imie i nazwisko
#wprowadzic numer tel
#i ma to robic w petli
#wyswietl slownik albo dodaj nowy kontakt

data = {}

while True:
    command = input("Pick an option: new_contact, show_contacts")
    if command == "new_contact":
        full_name = input(f"Wprowadz imie i nazwisko: ")
        number = input(f"Wprowadz numer: ")
        data[full_name] = number
    elif command == "show_contacts":
        print(data)
    # else:
    #     print("Unknown command")
    command = input("Do you wast to continue Y/N?")
    if command == "N":
        break