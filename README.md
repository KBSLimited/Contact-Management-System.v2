# Contact Management System.v2
 
Contact Management System This is a simple Contact Management System implemented in Python. It allows you to manage contacts with basic functionalities such as adding, editing, deleting, searching, displaying all contacts, and exporting contacts to a text file.

Features

-Add a New Contact: Enter details like name, phone number, email, and additional information for a new contact.
-Edit an Existing Contact: Modify details of an existing contact based on their phone number.
-Delete a Contact: Remove a contact from the system using their phone number.
-Search for a Contact: Find and display details of a contact based on their phone number.
-Display All Contacts: View all contacts stored in the system.
-Export Contacts: Save all contacts to a JSON format text file.
-Bonus Feature (Option 7): Import contacts from a text file (not fully implemented in this version).

Usage Clone the Repository

bash Copy code git clone https://github.com/yourusername/contacts-manager.git cd contacts-manager Run the Application

bash Copy code python contacts_manager.py Follow the On-screen Menu

Enter a number from 1 to 8 based on the action you want to perform. For example, to add a new contact, enter 1, and follow the prompts. Input Validation

The system validates input for phone numbers and email addresses. Phone numbers must be exactly 10 digits. Email addresses must follow a standard format (user@example.com). Exporting Contacts

When prompted to export contacts (6), enter a filename (e.g., contacts.json). Contacts will be exported in JSON format. Exiting the Program

Choose option 8 to exit the Contact Management System. Requirements Python 3.x No additional libraries are required beyond the standard Python library. Notes This system does not currently implement importing contacts from a text file (Option 7). Ensure that all input data is entered correctly to avoid validation errors. This README provides a brief overview of the application, its features, usage instructions, and some additional notes. You can expand on it further based on your specific needs or add more details about the implementation if necessary.