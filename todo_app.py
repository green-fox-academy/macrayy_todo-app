# TO DO APP
import sys
sys.argv

class ArgumentReader():
    def argument_reader(self):
        print_help_text = View()
        if len(sys.argv) == 1:
            return print_help_text.help_text()
        else:
            return sys.argv[1:]

class View():
    def help_text(self):
        return print("Python Todo application\n"
                "=======================\n"
                "Command line arguments:\n"
                "-l   Lists all the tasks\n"
                "-a   Adds a new task\n"
                "-r   Removes an task\n"
                "-c   Completes an task)\n")

arguments = ArgumentReader()
arguments.argument_reader()


# arguments = arg_reader()
#
# if len(arguments) == 0:
# 	print('help text')
# else:
# 	if( arguments[0] == '-l' ):
# 		print('Addolunk ilyet', arguments[1])
