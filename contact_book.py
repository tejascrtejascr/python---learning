contacts = {
    "Tejas": "9876543210",
    "Rahul": "9876501234"
}

name = input("Enter name: ")

if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found")