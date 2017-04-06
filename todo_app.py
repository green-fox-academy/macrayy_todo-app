# TO DO APP
import sys
sys.argv


def argument_reader():
    if len(sys.argv) == 1:
        return help_text()
    else:
        return sys.argv[1:]

def help_text():
    return print("Python Todo application\n"
            "=======================\n"
            "Command line arguments:\n"
            "-l   Lists all the tasks\n"
            "-a   Adds a new task\n"
            "-r   Removes an task\n"
            "-c   Completes an task)\n")

arguments = argument_reader()

# arguments = arg_reader()
#
# if len(arguments) == 0:
# 	print('help text')
# else:
# 	if( arguments[0] == '-l' ):
# 		print('Addolunk ilyet', arguments[1])
