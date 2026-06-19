import json
try:
    with open("contacts.json", "r") as file:
        contact_lists = json.load(file)
except FileNotFoundError:
    contact_lists = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contact_lists, file)

def add_contacts():
    name = input("Put contact name: ")
    Contact_number = input("Put contact number: ")
    Address = input("Put contact address: ")

    contact = {
        "name" : name,
        "phone" : Contact_number,
        "address" : Address
    }

    contact_lists.append(contact)
    save_contacts()
    print(f"{name} added successfully!")
    

def view_contacts():
    for contact in contact_lists:
        print("=" * 20)
        print(f"Name: {contact["name"]}")
        print(f"Phone: {contact["phone"]}")
        print(f"Address: {contact["address"]}")
    print("=" * 20)

def search_contact():
    name = input("Put contact name")
    for contact in contact_lists:
       

       if name == contact["name"]:
           print(f"Name: {contact["name"]}")
           print(f"Phone: {contact["phone"]}")
           print(f"Address: {contact["address"]}")
           break
    else:
         print("Contact not found")
        


def delete_contact():
    name = input("Put contact name")
    for contact in contact_lists:
     if name == contact["name"]:
         contact_lists.remove(contact)
         save_contacts()
         print(f"{name} Deleted successfully!")
         break
     else:
         print("Contact not found")




while True:
    print("=====CONTACT BOOK")
    print("1. ADD CONTACT")
    print("2. VIEW CONTACT")
    print("3. SEARCH CONTACT")
    print("4. DELETE CONTACT")
    print("5. EXIT")

    choice = input("Choose: ")

    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break