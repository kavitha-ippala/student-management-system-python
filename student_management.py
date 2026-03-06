print("------ Student Management Login ------")

correct_username = "admin"
correct_password = "1234"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username != correct_username or password != correct_password:
    print("Invalid Login! Access Denied.")
    exit()
else:
    print("Login Successful!\n")


import json

file_name = "students.json"

def load_data():
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f)

def add_student(data):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    data[roll] = {"name": name, "marks": marks}
    save_data(data)
    print("Student Added")

def view_students(data):
    for roll, details in data.items():
        print(f"Roll: {roll}, Name: {details['name']}, Marks: {details['marks']}")

def search_student(data):
    roll = input("Enter Roll Number: ")
    if roll in data:
        print(data[roll])
    else:
        print("Student not found")

def update_marks(data):
    roll = input("Enter Roll Number: ")
    if roll in data:
        new_marks = input("Enter New Marks: ")
        data[roll]["marks"] = new_marks
        save_data(data)
        print("Marks Updated")
    else:
        print("Student not found")

def delete_student(data):
    roll = input("Enter Roll Number: ")
    if roll in data:
        del data[roll]
        save_data(data)
        print("Student Deleted")
    else:
        print("Student not found")

data = load_data()

while True:
    print("\n1.Add Student\n2.View Students\n3.Search\n4.Update\n5.Delete\n6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student(data)
    elif choice == "2":
        view_students(data)
    elif choice == "3":
        search_student(data)
    elif choice == "4":
        update_marks(data)
    elif choice == "5":
        delete_student(data)
    elif choice == "6":
        break