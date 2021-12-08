from objects import Tasks, Task

def main():
    print("COMMAND MENU")
    print(f"list\t\t - Lists all tasks")
    print(f"add\t\t\t - Add a task")
    print(f"complete\t - Complete a task")
    print(f"delete\t\t - Delete a task")
    print(f"exit\t\t - Exit program")

    task_Lists = []
    personal = Tasks("Personal")
    business = Tasks("Business")
    task_Lists.append(personal)
    task_Lists.append(business)

    num_list = []
    for i in range(len(task_Lists)):
        num_list.append(i + 1)
        print(f"{i + 1}. {task_Lists[i].get_title()}")
    cont = False
    choice = 0
    while not cont:
        x = input("Enter number to select task list: ")
        for i in num_list:
            if i == int(x):
                choice = i - 1
                print(f"{task_Lists[i-1].get_title()} task list was selected.")
                cont = True


    task_list = task_Lists[choice]
    while cont:
        command = input("Command: ")
        if command.lower() == "list":
            task_list.list()
        elif command.lower() == "add":
            task_list.add(input("Description: "))
        elif command.lower() == "complete":
            task_list.complete(int(input("Number: ")))
        elif command.lower() == "delete":
            task_list.delete(int(input("Number: ")))
        elif command.lower() == "exit":
            break
        else:
            print("invalid Command. Please make another choice")





if __name__ == "__main__":
    main()
