#!/usr/bin/python3
"""
    This Module contains the entry point of the commnad interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
# from models.users import User


def parse(arg):
    cutly_braces = re.search(r"\{(.*?)\}", arg)
class HBNBCommand(cmd.Cmd):
    """
        This Class is the entry point of the command
    """
    prompt = '(hbnb) '
    __classname = {
            "BaseModel"
    }
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
            Usage: create <class> <key 1>=<value 1> <key 2>=<value 2>...
            Creates a new instance of a class and saves to a json file

            Arguments:
                arg: the classname

            Returns: nothing
        """
        try:
            if arg is None:
                raise SyntaxError()
            my_list = arg.split(' ')

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = my_list[i].split("=")
                if value[0] == '"':
                    value = value.strip('"').replace('_', " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, name=None, obj_id=None):
        """
            Usage: show <class> <id> or <class>.show(<id>)
            Prints the string representation of an instance based in
            the class name and id

            Arguments:
                name: the classname
                obj_id: the object id
        """
        obj_dict = storage.all()
        if name is None:
            print("** class name missing **")
            return None
        if name not in self.__classname:
            print("** class doesn't exist **")
            return None
        if obj_id is None:
            print("** instance id missing **")
            return None
        key = "{}.{}".format(name, obj_id)
        if key not in obj_dict.keys():
            print("** no instance found **")
        else:
            print(obj_dict[key])

    def do_destroy(self, name=None, obj_id=None):
        """
            Deletes an instance based on the class name and id
            and saves the change into the JSON file

            Arguments:
                name: the classname
                obj_id: the object id

            Returnns: Nothing
        """
        obj_dict = storage.all()
        if name is None:
            print("** class name missing **")
        elif name is not self.__classname:
            print("** class doesn't exist **")
        elif obj_id is None:
            print("** instance id missing **")
        elif "{}.{}".format(name, obj_id) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(name, obj_id)]
            storage.save()

    def do_all(self, name=None):
        """
            Usage: all or all <class> or <class>.all()

            Diplay string representations of all instances of a
            given class.If no class is specified, displays all
            instantiated objects.
            Arguments:
                name: classname

            Returns: None
        """
        my_dict = storage.all()
        if name is not None and name not in self.__classname:
            print("** class doesn't exists **")
        else:
            obj_arr = []
            for obj in my_dict.values():
                if name is not None and name == obj.__class__.__name__:
                    obj_arr.append(obj.__str__())
                elif name is None:
                    obj_arr.append(obj.__str__())
            print(obj_arr)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
            Retrieve the number of instances of a given class.

            Arguments:
                arg: the arguments
        """
        count = 0
        for obj in storage.all().values():
            if arg == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
            Usage: <class name> <id> <attribute name> "<attribute value>"
            Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).

            Arguments:
                arg: The values to be updated
        """
        arg_arr = parse(arg)
        obj_dict = storage.all()

        if len(arg_arr) == 0:
            print("** class name missing **")
            return False
        if arg_arr[0] not in self.__classname:
            print("** class doesn't exist **")
            return False
        if len(arg_arr) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_arr[0], arg_arr[1]) not in obj_dict:
            print("** no instance found **")
            return False
        if len(arg_arr) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_arr) == 3:
            try:
                type(eval(arg_arr[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_arr) == 4:
            obj = obj_dict["{}.{}".format(arg_arr[0], arg_arr[1])]
            if arg_arr[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_arr[2]])
                obj.__dict__[arg_arr[2]] = valtype(arg_arr[3])
            else:
                obj.__dict__[arg_arr[2]] = arg_arr[3]
        elif type(eval(arg_arr[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_arr[0], arg_arr[1])]
            for k, v in eval(arg_arr[2]):
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
