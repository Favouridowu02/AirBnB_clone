#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbtn) '

    def do_EOF(self, line):
        """This contains the End of File
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty file
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
