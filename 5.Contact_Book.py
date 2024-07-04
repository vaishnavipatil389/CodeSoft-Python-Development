import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
                print("--------------------")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, search_term, updated_contact):
        for i, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts[i] = updated_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for i, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def display_menu(self):
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        print("Welcome to the Contact Book App!")

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                name = input("Enter contact's name: ")
                phone = input("Enter contact's phone number: ")
                email = input("Enter contact's email address: ")
                address = input("Enter contact's address: ")
                new_contact = Contact(name, phone, email, address)
                self.add_contact(new_contact)

            elif choice == '2':
                self.view_contacts()

            elif choice == '3':
                search_term = input("Enter name or phone number to search: ")
                found_contacts = self.search_contact(search_term)
                if found_contacts:
                    print("\nSearch results:")
                    for contact in found_contacts:
                        print(contact)
                        print("--------------------")
                else:
                    print("No matching contacts found.")

            elif choice == '4':
                search_term = input("Enter name or phone number of contact to update: ")
                found_contacts = self.search_contact(search_term)
                if found_contacts:
                    if len(found_contacts) > 1:
                        print("Multiple contacts found. Please refine your search.")
                    else:
                        name = input("Enter updated name: ")
                        phone = input("Enter updated phone number: ")
                        email = input("Enter updated email address: ")
                        address = input("Enter updated address: ")
                        updated_contact = Contact(name, phone, email, address)
                        self.update_contact(search_term, updated_contact)
                else:
                    print("Contact not found.")

            elif choice == '5':
                search_term = input("Enter name or phone number of contact to delete: ")
                self.delete_contact(search_term)

            elif choice == '6':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
