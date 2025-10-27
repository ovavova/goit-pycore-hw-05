def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give a name and a phone please"
        except KeyError:
            return "No such contact"
        except IndexError:
            return "Please provide a name"
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list, contacts: dict) -> None:         # Args as name + number, store to dictionary 
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def all(contacts:dict) -> None:                              # Print all contacts in dict
    for name, phone_num in contacts.items():
        print(f"Contact Name:{name}; Phone Number: {phone_num}")

@input_error
def change_phone(args:list, contacts: dict) -> None:
    if args[0] in contacts:
        contacts[args[0]] = args[1]                              # Updating existing name with new number
        return f"Number for contact {args[0]} is updated"
    else:
        return(f"No such contact - {args[0]}")

@input_error
def phone_u(args:list, contacts:dict) -> None:               # Return phone number for given name
    return contacts[args[0]]


def main():
    contacts = {}                          # Dictionary to store contacts

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
        elif command == "all":
            all(contacts)
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(phone_u(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()