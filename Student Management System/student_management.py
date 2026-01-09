import os
import json

FILE_NAME="students.json"

def load_students():
   if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0: 
       return {}
   with open(FILE_NAME,"r") as file:
           return json.load(file)
       
def save_students(students):
    with open(FILE_NAME,"w") as file:
        json.dump(students,file,indent=4)
        


def add_student():
    students=load_students()
    sid=input("Enter Student ID : ")

    if sid in students:
        print("Student already exists")
        return
    
    name=input("Enter name : ")
    age=input("Enter age : ")
    course=input("Enter course : ")

    students[sid]={
        "name":name,
        "age":age,
        "course":course
    }
    save_students(students)
    print("Student added successfully......")
    return


def view_students():
    students=load_students()
    if not students:
        print("No students found!")
        return
    print(f"SID    Name             Age       Course")

    for sid,data in students.items():
        print(f"{sid}    {data['name']}          {data['age']}       {data['course']}")

def delete_student():
    students = load_students()
    sid = input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def search_student():
    students=load_students()
    if not students:
        print("No student records...")
        return
    sid=input("Enter student id to search : ")
    if sid in students:
        data=students[sid]
        print(f"{sid}   {data['name']}        {data['age']}          {data['course']}")
    else:
        print("Student not exists...")

def update_student():
    students = load_students()
    sid = input("Enter Student ID to update: ")

    if sid not in students:
        print("Student not found!")
        return

    print("Leave blank to keep old value")

    name = input("Enter new name: ")
    age = input("Enter new age: ")
    course = input("Enter new course: ")

    if name:
        students[sid]["name"] = name
    if age:
        students[sid]["age"] = age
    if course:
        students[sid]["course"] = course

    save_students(students)
    print("Student updated successfully!")


def menu():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()