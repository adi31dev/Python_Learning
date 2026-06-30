import json 


try:
    with open("contact.json", "r") as file:
        contact_lists = json.load(file)

except FileNotFoundError:
    contact_lists = []

def save_contact():
    with open("contact.json", "w") as file:
        json.dump(contact_lists, file)

def add_contacts():
    name = input("Put contact name: ")
    Phone = input("Put contact number: ")
    Address = input("Put contact address: ")

    contact = {
        "Name": name,
        "Phone": Phone,
        "Address": Address
    }
    contact_lists.append(contact)
    save_contact()
    print(f"{name} added succesfully!")

def view_contacts():
    for contact in contact_lists:
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"address: {contact['Address']}")
        

def search_contacts():
    name = input("Put contact name: ")
    for contact in contact_lists:
        if name == contact["Name"]:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"address: {contact['Address']}")
            break
    else:
            print("Contact not found!")
    
def delete_contacts():
    name = input("Put contact name: ")
    for contact in contact_lists:
        if name == contact["Name"]:
            contact_lists.remove(contact)
            save_contact()
            print(f"{name} deleted successfully!")
            break

    else:
            print("Contact not found")



while True:
         print("1. View contacts")
         print("2. Search_contacts")
         print("3. Add contacts")
         print("4. Delete contact")
         print("5. Exit")

         choice = input("Choose: ")
         if choice == "1":
              view_contacts()
         elif choice == "2":
              search_contacts()
         elif choice == "3":
              add_contacts()
         elif choice == "4":
              delete_contacts()
         elif choice == "5":
               print("Goodbye!")
               break

               

