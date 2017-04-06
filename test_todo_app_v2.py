# TO DO APP
import sys

def argument_reader():
    if len(sys.argv) == 1:
        help_text()
    else:
        if sys.argv[1] == "-l":



def read_file():
    todo_file = open("todo.txt", "r")
    todo_lines = todo_file.readlines()
    todo_list = []
    for line in todo_lines:
        todo_list.append(line.split(";"))
    todo_file.close()
    return todo_list


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

def list_todo():
    output_list = OpenFile()
    output_list.read_file()
    for element in output_list.read_file():
        if output_list.read_file()[0] == "0":
            print("[ ]" + " - " + output_list.read_file()[1])
        elif output_list.read_file()[0] == "1":
            print("[x]" + " - " + output_list.read_file()[1])


arguments = ArgumentReader()
arguments.argument_reader()
