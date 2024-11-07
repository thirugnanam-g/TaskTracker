"""
The code defines a TaskTracker class with methods to add, update, delete, and list tasks, and a main function to interact with the TaskTracker.
"""
from datetime import datetime
from abc import ABC



# id:
# description:
# status:
# createdAt:
# updatedAt:

class Task(ABC):

    def __init__(self,id:int,description:str, status:str):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__createdAt = datetime.now().strftime("Date: %d-%m-%Y and Time: %H:%M:%S")
        self.__updatesAt = self.__createdAt

    def dict_task(self)->dict[str,str]:
        return {
            "Task id": self.__id,
            "Description": self.__description,
            "Status": self.__status,
            "Created At": self.__createdAt,
            "Updated At": self.__updatesAt
        }


class TaskTracker:
    tasks:list[dict] = []
    status_categories = ["ALL","TODO",'IN-PROGRESS','DONE']
    id = 0

    @classmethod
    def id_counter(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def add_tasks(cls):
        print("Add your task")
        description = input("Enter short description of task: ")
        for i,_ in enumerate(cls.status_categories[1:], start = 1):
            print(f"{i}. {_}")
        choose = int(input("Enter the status progress: "))
        while choose not in [1,2,3]:
            print("Enter the number only between (1-3)")
            choose = int(input("Enter the status progress: "))
        status = cls.status_categories[choose]
        task = Task(cls.id_counter(),description,status)
        cls.tasks.append(task.dict_task())

    @classmethod
    def update_tasks(cls):
        try:
            task_id = int(input("Enter the tsk id you would like to update: "))
            for task in cls.tasks:
                if task_id == task["Task id"]:
                    for i, _ in enumerate(cls.status_categories[1:], start=1):
                        print(f"{i}. {_}")
                    update_status = int(input("Enter the status progress: "))
                    while update_status not in [1, 2, 3]:
                        print("Enter the number only between (1-3)")
                        update_status = int(input("Enter the status progress: "))
                    task['Status'] = cls.status_categories[update_status]
                    task['Updated At'] = datetime.now().strftime("Date: %d-%m-%Y and time: %H:%M:%S")
                    print("Task Successfully updated")
                else:
                    print("Task id not found")
        except Exception as e:
            print("Invalid input")
            print(e)
            print()

    @classmethod
    def list_tasks(cls):
        for i,_ in enumerate(TaskTracker.status_categories, start = 1):
            print(f"{i}. {_}")
        choose = int(input("Enter the status progress to filter the status: "))
        while choose not in [1,2,3,4]:
            print("Enter the number only between (1-4)")
            choose = int(input("Enter the status progress to filter the status: "))
        filter_status = cls.status_categories[choose-1]
        print(f"Task list of {filter_status}")
        print("----------------------------------------------")
        if filter_status == 'ALL':
            for task in cls.tasks:
                for k,v in task.items():
                    print(f"{k} : {v}")
                print("----------------------------------------------")
        else:
            for task in cls.tasks:
                if task['Status'] == filter_status:
                    for k, v in task.items():
                        print(f"{k} : {v}")
                    print("----------------------------------------------")

    @classmethod
    def delete_tasks(cls):
        try:
            task_found = False
            task_id = int(input("Enter the id of task you like to delete: "))
            for task in cls.tasks:
                if task['Task id'] == task_id:
                    cls.tasks = [task for task in cls.tasks if task['Task id'] != task_id]
                    print(f"The task {task_id} has been deleted")
                    task_found = True
                    break
            if not task_found:
                print(f'The task {task_id} not found')
        except Exception as e:
            print(f'Invalid input \nDetails -> {e}')



def main():
    tasktracker = TaskTracker()
    print("Welcome To Task Tracker")
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Delete Task\n4. Update Task\n5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    tasktracker.add_tasks()
                case 2:
                    tasktracker.list_tasks()
                case 3:
                    tasktracker.delete_tasks()
                case 4:
                    tasktracker.update_tasks()
                case 5:
                    break
                case _:
                    print("Invalid input, Please Enter valid input(1-5)")
        except Exception as e:
            print(f"Invalid input \nDetails -> {e}")
            print("Enter valid input (1-4)")
            print()

if __name__ == '__main__':
    main()

