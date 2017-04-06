# TO DO APP
import sys

class ArgumentReader():
    def argument_reader(self):
        print_help_text = View()
        if len(sys.argv) == 1:
            print_help_text.help_text()
        else:
            if sys.argv[1] == "-l":
                output_list = View()
                output_list.list_todo()

class OpenFile():

    def read_file(self):
        todo_file = open("todo.txt", "r")
        todo_lines = todo_file.readlines()
        todo_list = []
        for line in todo_lines:
            todo_list.append(line.split(";"))
        todo_file.close()
        return todo_list

class View():
    def help_text(self):
        return print("\n"
                "Python Todo application\n"
                "=======================\n"
                "\n"
                "Command line arguments:\n"
                "-l   Lists all the tasks\n"
                "-a   Adds a new task\n"
                "-r   Removes a task\n"
                "-c   Completes a task)\n")

    def list_todo(self):
        output_list = OpenFile()
        output_list.read_file()
        for element in output_list.read_file():
            if output_list.read_file()[0] == "0":
                print("[ ]" + " - " + output_list.read_file()[1])
            elif output_list.read_file()[0] == "1":
                print("[x]" + " - " + output_list.read_file()[1])


arguments = ArgumentReader()
arguments.argument_reader()
