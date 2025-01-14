import re
import json

# Global variable to store contacts
contacts = {}

# Regular expressions for input validation
phone_regex = re.compile(r'^\d{10}$')  # Matches a 10-digit phone number
email_regex = re.compile(r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$')  # Matches an email address

def display_menu():
    """Display the main menu for the Contact Management System."""
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file (BONUS)")
    print("8. Quit")

def validate_phone():
    """Prompt the user for a phone number and validate it."""
    phone = input("Enter phone number (10 digits): ")
    while not re.match(phone_regex, phone):
        print("Invalid phone number format! Please enter 10 digits.")
        phone = input("Enter phone number (10 digits): ")
    return phone

def validate_email():
    """Prompt the user for an email address and validate it."""
    email = input("Enter email address: ")
    while not re.match(email_regex, email):
        print("Invalid email format! Please enter a valid email address.")
        email = input("Enter email address: ")
    return email

def add_contact():
    """Add a new contact to the contacts list."""
    print("\nAdding a new contact:")
    name = input("Enter name: ")
    phone = validate_phone()
    email = validate_email()
    additional_info = input("Enter additional information (optional): ")
    contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'additional_info': additional_info}
    print(f"Contact added: {name} ({phone})")

def edit_contact():
    """Edit an existing contact."""
    print("\nEditing an existing contact:")
    phone = input("Enter phone number of the contact to edit: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Current details for {contact['name']}:")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Additional Info: {contact['additional_info']}")
        print("Enter new details (leave blank to keep current):")
        name = input(f"Enter name [{contact['name']}]: ") or contact['name']
        email = input(f"Enter email address [{contact['email']}]: ") or contact['email']
        additional_info = input(f"Enter additional information [{contact['additional_info']}]: ")
        contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'additional_info': additional_info}
        print(f"Contact updated: {name} ({phone})")
    else:
        print("Contact not found.")

def delete_contact():
    """Delete a contact from the contacts list."""
    print("\nDeleting a contact:")
    phone = input("Enter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print(f"Contact with phone number {phone} deleted.")
    else:
        print("Contact not found.")

def search_contact():
    """Search for a contact by phone number."""
    print("\nSearching for a contact:")
    phone = input("Enter phone number of the contact to search for: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Contact found: {contact['name']} ({phone})")
        print(f"Email: {contact['email']}")
        print(f"Additional Info: {contact['additional_info']}")
    else:
        print("Contact not found.")

def display_contacts():
    """Display all the contacts."""
    print("\nAll contacts:")
    if contacts:
        for phone, contact in contacts.items():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Additional Info: {contact['additional_info']}")
    else:
        print("No contacts available.")

def export_contacts():
    """Export contacts to a text file."""
    filename = input("Enter filename to export contacts (e.g., contacts.txt): ")
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
    print(f"Contacts exported to {filename}.")

def main():
    """Main function to run the program."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            print("Importing contacts from a text file (Bonus feature).")
            # Implement import_contacts function if you want to add this feature
        elif choice == '8':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()