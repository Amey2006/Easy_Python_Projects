import os
import msvcrt
class Task:
    def __init__(self,name,description,status,priority):
        self.name=name
        self.description=description
        self.status=status
        self.priority=priority
    
    def __repr__(self):
        return f"(\n Name : {self.name} \n Description : {self.description} \n Status : {self.status} \n Priority : {self.priority} \n)"

    def get_info(self):
        self.name=input("Enter task name : ")
        self.description=input("Write description : ")
        self.status=input("Tell status : ")
        self.priority=input(" 1.High \n 2.Medium \n 3.Low \n Give priority : ")
      
task_list=[]  
def add_task(newtask):
    task_list.append(newtask)

def display_tasks():
    no=1
    for i in task_list:
        print(f"Task {no} ")
        print(repr(i),"\n")
        no+=1
while(1):
    
    print("1 Display Tasks")
    print("2 Add Tasks")
    print("3 Edit Tasks")
    print("4 Delete Tasks")
    print("5 Exit")
    print("6 Create")

    ch=int(input("Enter your choice : "))
    if ch == 1 :
        if not task_list:
            print("No tasks in list")
            continue
        display_tasks()

    elif ch==2 :
        t=Task()
        t.get_info()
        add_task(t)
        print("Task added successfully")

    elif ch==3:
        if not task_list:
            print("No tasks in list")
            continue
        print("Choose task number to edit ")
        for i,task in enumerate(task_list,start=1):
            print(f"{i}. {task.name}")
        ch=int(input())-1
        t=Task()
        t.get_info()
        del task_list[ch]
        task_list[ch]=t
        print("Task edited successfully")


    elif ch==4:
        if not task_list:
            print("No tasks in list")
        else:
            print("Choose task number to delete ")
            for i,task in enumerate(task_list,start=1):
                print(f"{i}. {task.name}")
            ch=int(input())
            task_list.pop(ch-1)
            print("Task deleted successfully")

    elif ch==6:
        t1=Task("Complete Homework","Write 1 to 20 tables","Pending","Medium")
        add_task(t1)
        display_tasks() 

    else: 
        exit()
    print("\n\n\nPress any key to continue....")
    msvcrt.getch()
    os.system('cls')
