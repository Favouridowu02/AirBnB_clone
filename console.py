#!/usr/bin/python3
"""
    This Module contains the entry point of the commnad interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        This Class is the entry point of the command
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
