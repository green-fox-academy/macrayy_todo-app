# TO DO APP
import sys
import os
os.system("cls" if os.name == "nt" else "clear")

class Controller():

    def argument_reader(self):
        if len(sys.argv) == 1:
            help_display = Display()
            help_display.help_text()
        else:
            list_display = Display()
            if sys.argv[1] == "-l":
                list_display.list_todo()
            elif sys.argv[1] == "-a":
                if sys.argv[2:] == []:
                    print("Unable to add: no task provided.")
                else:
                    add_display = Model()
                    add_display.add_task()
                    list_display.list_todo()
            elif sys.argv[1] == "-r":
                remove_display = Model()
                remove_display.remove_task()
                list_display.list_todo()
            elif sys.argv[1] == "-c":
                check_task_display = Model()
                check_task_display.check_task()
                list_display.list_todo()

class Model():

    def read_file(self):
        todo_file = open("todo.txt", "r")
        todo_lines = todo_file.readlines()
        todo_list = []
        for line in todo_lines:
            todo_list.append(line.split(";"))
        todo_file.close()
        return todo_list

    def add_task(self):
        todo_file = open("todo.txt", "a")
        args = " ".join(sys.argv[2:])
        text =  "0;" + args + "\n"
        todo_file.writelines(text)
        todo_file.close()
        print("Task added.")

    def remove_task(self):
        todo_file = open("todo.txt", "r")
        todo_lines = todo_file.readlines()
        todo_file.close()
        new_todo_list = ""
        for list_element in range(len(todo_lines)):
            if list_element != int(sys.argv[2]) - 1:
                new_todo_list += (todo_lines[list_element])
        todo_file = open("todo.txt", "w")
        todo_file.write(new_todo_list)
        todo_file.close()

    def check_task(self):
        self.read_file()
        read_file = self.read_file()
        for list_element in range(len(read_file)):
            if list_element == int(sys.argv[2]) - 1:
                nth_element = read_file[list_element]
                if nth_element[0] == "0":
                    nth_element[0] = "1"
                elif nth_element[0] == "1":
                    nth_element[0] = "0"
        write_file = ""
        for list_element in read_file:
            write_file += ";".join(list_element)
        todo_file = open("todo.txt", "w")
        todo_file.write(write_file)
        todo_file.close()


class Display():

    def list_todo(self):
        read = Model()
        read.read_file()
        if read.read_file() == []:
            print("No todos for today! Good for you!")
        else:
            nth = 0
            for element in read.read_file():
                nth += 1
                if element[0] == "0":
                    print(nth, "[ ]", " - ", element[1][:-1])
                elif element[0] == "1":
                    print(nth, "[*]", " - ", element[1][:-1])

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


run = Controller()
run.argument_reader()
