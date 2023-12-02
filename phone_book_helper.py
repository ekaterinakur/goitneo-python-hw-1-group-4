
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid contact. Contact should consist of name and phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid contact. Contact should consist of name and phone"
    name, phone = args
    if not name in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone_by_user(args, contacts):
    if len(args) == 0:
        return "Invalid input. Need a username to find a phone"
    name = args[0]
    if not name in contacts:
        return "No contacts found."
    return contacts[name]

def show_all(contacts):
    if not len(contacts):
        return '"No contacts found.'
    contacts_to_display = ''
    for name, phone in contacts.items():
        contacts_to_display += '{:<10}: {:}\n'.format(name, phone)
    return contacts_to_display.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone_by_user(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()