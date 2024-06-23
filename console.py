#!/usr/bin/python3
"""
    This Module contains the entry point of the commnad interpreter
"""
import cmd
from models.base_model import Basemodel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        This Class is the entry point of the command
    """
    prompt = '(hbnb) '
    __classname = { "BaseModel": BaseModel }
    __filepath = "file.json"

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

    def do_create(self, arg):
        """
            Creates a new instance of a class and saves to a json file

            Arguments:
                arg: the classname

            Returns: nothing
        """
        if arg == None:
            print("** class name missing **")
            return

        for key, value in self.__classname.items():
            if key == arg:
                obj = self.__classname[key]()
                obj.save()
                print(obj.id)
                return

        print("** class doesn't exist **")

    def do_show(self, name, obj_id):
        """
            Prints the string representation of an instance based in
            the class name and id

            Arguments:
                name: the classname
                obj_id: the object id
        """
        if name == None:
            print("** class name missing **")
            return
        if obj_id == None:
            print("** instance id missing **")
            return
        for key, value in __classname.items():
            if key == name:
                objdict = storage.all()
                if "{}.{}".format(name, obj_id) not in objdict:
                    print("** no instance found **")
                    return
                print(objdict["{}.{}".format(name, obj_id)])
                return

        print("** class doesn't exists **")

    def do_destroy(self, name, obj_id):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file)

            Arguments:
                name: the class name
                obj_id: the object id
        """
        if name == None:
            print("** class name missing **")
            return
        if obj_id == None:
            print("** instance id missing **")
            return
        for key, value in __classname.items():
            if key == name:
                if "{}.{}".format(name, obj_id) not in storage.all():
                    print("** no instance found **")
                    return
                del storage.all()["{}.{}".format(name, obj_id)]
                storage.save()
                return
        print("** class doesn't exist **")

    def all(self, name):
        """
            Prints all string representation of all instances based
            or not on the class name

            Arguments:
                name: the class name
        """
        if name not in self.__classname.keys():
            print("** class doesn't exist **")

        obj_dict = storage.all()
        if name == None:
            for key, value in obj_dict:
                print('["[{}] ({})


if __name__ == "__main__":
    HBNBCommand().cmdloop()
