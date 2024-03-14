def clear_screen():  # Function to clear screen
    print("\033[H\033[J", end="")

def display_menu():  # Function to display menu options
    print("""
    **Welcome to To-Do List!**

    Enter the corresponding number to perform an action:

    1. Add task
    2. Remove task
    3. Edit task
    4. View all tasks
    5. Exit
    """)

toDoList = []

while True:
    clear_screen()  # Clear screen for a cleaner UI
    display_menu()

    command = input("\nEnter your choice: ")

    if command == "1":
        task = input("Enter the task: ")
        toDoList.append(task)
        print("Task added successfully!")

    elif command == "2":
        task = input("Enter the task you want to remove: ")
        try:
            toDoList.remove(task)
            print("Task removed successfully!")
        except ValueError:
            print("Task not found in the list.")

    elif command == "3":
        task_to_edit = input("Enter the name of the task you want to edit: ")
        try:
            index = toDoList.index(task_to_edit)
            edited_task = input("Enter the new task: ")
            toDoList[index] = edited_task
            print("Task edited successfully!")
        except ValueError:
            print("Task not found in the list.")

    elif command == "4":
        if toDoList:  # Check if list is not empty
            for task in toDoList:
                print(task)
        else:
            print("List is empty.")

    elif command == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")
