import json
import os

FILE_NAME = "students.json"

# Load Data 
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save Data 
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Roll Validation 
def get_valid_roll():
    while True:
        roll = input("Enter Roll No (numbers only): ")
        if roll.isdigit():
            return roll
        else:
            print("Error: Roll number must contain only digits!")

# Create 
def create_student(data):
    roll = get_valid_roll()

    if roll in data:
        print("Error: Roll number already exists!")
        return

    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()

    data[roll] = {"name": name, "department": dept}
    save_data(data)

    print("Student added successfully!")

# View
def view_students(data):
    if not data:
        print("No records found.")
        return

    print("\nRoll No    Name                 Department")
    print("-" * 45)

    for roll, info in data.items():
        print(f"{roll:<10}{info['name']:<20}{info['department']:<15}")

# Update 
def update_student(data):
    roll = get_valid_roll()

    if roll not in data:
        print("Error: Student not found!")
        return

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Department")

    choice = input("Enter choice: ").strip().lower()

    if choice in ["1", "name"]:
        data[roll]["name"] = input("Enter new Name: ").strip()
        print("Name updated successfully!")

    elif choice in ["2", "department"]:
        data[roll]["department"] = input("Enter new Department: ").strip()
        print("Department updated successfully!")

    else:
        print("Invalid choice!")
        return

    save_data(data)

# Delete 
def delete_student(data):
    roll = get_valid_roll()

    if roll not in data:
        print("Error: Student not found!")
        return

    del data[roll]
    save_data(data)

    print("Student deleted successfully!")

# Search 
def search_student(data):
    if not data:
        print("No records found.")
        return

    print("\nSearch by:")
    print("1. Roll No")
    print("2. Name")
    print("3. Department")

    choice = input("Enter choice: ").strip().lower()

    # Search by Roll
    if choice in ["1", "roll"]:
        roll = get_valid_roll()

        if roll in data:
            info = data[roll]
            print("\nRoll No    Name                 Department")
            print("-" * 45)
            print(f"{roll:<10}{info['name']:<20}{info['department']:<15}")
        else:
            print("Student not found!")

    # Search by Name 
    elif choice in ["2", "name"]:
        name = input("Enter name to search: ").strip().lower()
        found = False

        print("\nRoll No    Name                 Department")
        print("-" * 45)

        for roll, info in data.items():
            if name in info["name"].lower():
                print(f"{roll:<10}{info['name']:<20}{info['department']:<15}")
                found = True

        if not found:
            print("No matching students found!")

    # Search by Department 
    elif choice in ["3", "department"]:
        dept = input("Enter department to search: ").strip().lower()
        found = False

        print("\nRoll No    Name                 Department")
        print("-" * 45)

        for roll, info in data.items():
            if dept in info["department"].lower():
                print(f"{roll:<10}{info['name']:<20}{info['department']:<15}")
                found = True

        if not found:
            print("No matching students found!")

    else:
        print("Invalid choice!")

# Main Menu 
def main():
    data = load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Create Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            update_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            search_student(data)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

# Run
if __name__ == "__main__":
    main()
