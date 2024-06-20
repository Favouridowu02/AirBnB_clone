#!/usr/bin/python3
import cmd


class Console(cmd.Cmd):
    prompt = '(hbtn) '

    def do_EOF(self, line):
        """
            This contains the End of File
        """
        return True

    def do_quit(self, arg):
        """
            This is the quit command
        """
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    Console().cmdloop()
