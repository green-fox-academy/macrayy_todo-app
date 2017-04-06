# TO DO APP
import sys
import os
os.system("cls" if os.name == "nt" else "clear")

def argument_reader():
    if len(sys.argv) == 1:
        help_text()
    else:
        if sys.argv[1] == "-l":
            list_todo()
        elif sys.argv[1] == "-a":
            if sys.argv[2:] == []:
                print("Unable to add: no task provided.")
            else:
                add_task()
                read_file()
                list_todo()

def help_text():
    return print("\n"
            "Python Todo application\n"
            "=======================\n"
            "\n"
            "Command line arguments:\n"
            "-l   Lists all the tasks\n"
            "-a   Adds a new task\n"
            "-r   Removes a task\n"
            "-c   Completes a task)\n")

def read_file():
    todo_file = open("todo.txt", "r")
    todo_lines = todo_file.readlines()
    todo_list = []
    for line in todo_lines:
        todo_list.append(line.split(";"))
    todo_file.close()
    return todo_list

def add_task():
    todo_file = open("todo.txt", "a")
    args = " ".join(sys.argv[2:])
    text =  "0;" + args + "\n"
    todo_file.writelines(text)
    todo_file.close()
    print("Task added.")

def list_todo():
    read_file()
    if read_file() == []:
        print("No todos for today! :)")
    else:
        nth = 0
        for element in read_file():
            nth += 1
            if element[0] == "0":
                print(nth, "[ ]", " - ", element[1])
            elif element[0] == "1":
                print(nth, "[*]", " - ", element[1])


argument_reader()
