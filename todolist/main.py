toDoList = []

while True:
    command = input("""Welcome to todo list:\nEnter the corresponding number to do the specific action:
                    \n1- add task\n2- remove task \n3- edit task\n4- view all task\n5- exit\n""")
    if command == "1":
        task = input("enter the task: ")
        toDoList.append(task)
        print("Task added")
    elif command == "2":
        task = input("enter the task you want to remove: ")

        if task in toDoList:
            toDoList.remove(task)
            print("Task removed")
        else:
            print("task is not in list to begin with.")

    elif command == "3":
        task = input("enter the name of the task you want to edit: ")

        if task not in toDoList:
            print("task is not in list to begin with.")
            continue

        editedTask = input("enter the new task: ")
        toDoList[toDoList.index(task)] = editedTask
        print("Task edited")

    elif command == "4":
        if len(toDoList) > 0:
            for task in toDoList:
                print(task)
        else:
            print("list is empty")

    elif command == "5":
        break

    else:
        print("invalid command")
