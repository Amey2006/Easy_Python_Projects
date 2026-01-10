import os
import json


class Student_Management_System:
    def __init__(self,jsonfile):
        self.FILE_NAME=jsonfile

    def load_students(self):
        if not os.path.exists(self.FILE_NAME) or os.path.getsize(self.FILE_NAME) == 0: 
            return {}
        with open(self.FILE_NAME,"r") as file:
                return json.load(file)
        
    def save_students(self,students):
        students=dict(sorted(students.items(),key=lambda x:int(x[0]),reverse=False))
        with open(self.FILE_NAME,"w") as file:
            json.dump(students,file,indent=4)
            


    def add_student(self):
        students=self.load_students()
        sid=input("Enter Student ID : ")

        if not sid.isdigit():
            print("ID must be numeric")
            while(not sid.isdigit()):
                sid=input("Enter sid : ")

        if sid in students:
            print("Student already exists")
            return
        
        name=input("Enter name : ")
        age=input("Enter age : ")
        while(not age.isdigit()):
            age=input("Enter age : ")
        course=input("Enter course : ")

        students[sid]={
            "name":name,
            "age":age,
            "course":course
        }
        self.save_students(students)
        print("Student added successfully......")
        return


    def view_students(self):
        students=self.load_students()
        if not students:
            print("No students found!")
            return
        print(f"{"SID":<5}    {'name':<10}             {'age':<3}       Course")

        for sid,data in students.items():
            print(f"{sid:<5}    {data['name']:<10}          {data['age']:<3}       {data['course']}")

    def delete_student(self):
        students = self.load_students()
        sid = input("Enter Student ID to delete: ")
        if not sid.isdigit():
            print("ID must be numeric ")
            while(not sid.isdigit()):
                sid=input("Enter sid : ")

        if sid in students:
            del students[sid]
            self.save_students(students)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def search_student(self):
        students=self.load_students()
        if not students:
            print("No student records...")
            return
        sid=input("Enter student id to search : ")
        if not sid.isdigit():
            print("ID must be numeric")
            while(not sid.isdigit()):
                sid=input("Enter sid : ")
        if sid in students:
            data=students[sid]
            print(f"{sid}   {data['name']}        {data['age']}          {data['course']}")
        else:
            print("Student not exists...")

    def update_student(self):
        students = self.load_students()
        sid = input("Enter Student ID to update: ")
        if not sid.isdigit():
            print("ID must be numeric")
            while(not sid.isdigit()):
                sid=input("Enter sid : ")
        if sid not in students:
            print("Student not found!")
            return

        print("Leave blank to keep old value")
        sid2=input("Enter Student ID : ")

        if not sid2.isdigit():
            print("ID must be numeric")
            while(not sid2.isdigit()):
                sid2=input("Enter sid : ")

        if sid2 in students:
            print("Student already exists")
            return
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")
        if sid2:
            students[sid2]=students[sid]
        if name:
            students[sid2]["name"] = name
        if age:
            students[sid2]["age"] = age
        if course:
            students[sid2]["course"] = course

        del students[sid]
        self.save_students(students)
        print("Student updated successfully!")


    def menu(self):
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
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Exiting program...")
                break
            else:
                print("Invalid choice!")

    def start(self):
        while True:
            user = input("Username: ")
            password = input("Password: ")

            if user == "admin" and password == "1234":
                print("Login successful!")
                self.menu()
                break
            else:
                print("Invalid credentials. Try again.")

System=Student_Management_System("students.json")
System.start()