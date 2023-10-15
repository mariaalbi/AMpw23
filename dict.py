#wprowadzic imie i nazwisko
#wprowadzic numer tel
#i ma to robic w petli
#wyswietl slownik albo dodaj nowy kontakt

data = {}
commands = ["new_contact","show_contacts"]
while True:
    command = input(f"Pick an option: {commands}")
    while command not in commands:
        print("Unknown command, try again")
        command = input(f"Pick an option: {commands}")

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