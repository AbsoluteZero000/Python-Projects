toDoList = []

while True:
    command = input("""Welcome to todo list:\nEnter the corresponding number to do the specific action:
                    \n1- add task\n2- remove task \n3- edit task\n4- view all task\n5- exit\n""")
    if command == "1":
        task = input("enter the task: ")
        toDoList.append(task)
    elif command == "2":
        task = input("enter the task you want to remove: ")
        toDoList.remove(task)
    elif command == "3":
        task = input("enter the name of the task you want to edit: ")
        editedTask = input("enter the new task: ")
        toDoList[toDoList.index(task)] = editedTask
    elif command == "4":
        
        print(toDoList if len(toDoList) > 0 else "list is empty")
    elif command == "5":
        break
