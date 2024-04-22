#!/usr/bin/python3
"""Module for class Base"""
import json
import csv


class Base:
    """Represents the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an object
        Args:
            id: None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        jsondump = json.dumps(list_dictionaries)
        return jsondump

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a JSON string to a file
        Args:
            list_objs: object to get JSON string
        """
        name = "{}.json".format(cls.__name__)

        with open(name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = []
                for i in list_objs:
                    dict_list.append(i.to_dictionary())
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation
        Args:
            json_string: string rep a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set
        Args:
            dictionary: a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dum = cls(1, 1)
            else:
                dum = cls(1)
            dum.update(**dictionary)

            return dum

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        name = "{}.json".format(cls.__name__)

        try:
            with open(name, "r") as f:
                dict_list = Base.from_json_string(f.read())

                instance_list = []

                for i in dict_list:
                    instance_list.append(cls.create(**i))
                return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes to CSV file"""
        name = "{}.csv".format(cls.__name__)

        with open(name, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fname = ["id", "width", "height", "x", "y"]
                else:
                    fname = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fname)

            for i in list_objs:
                writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of csv file"""
        name = "{}.csv".format(cls.__name__)

        try:
            with open(name, "r") as f:
                if cls.__name__ == "Rectangle":
                    fname = ["id", "width", "height", "x", "y"]
                else:
                    fname = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(f, fieldnames=fname)

                new_list_dict = []
                convert_dict = {}

                for i in dict_list:
                    for key, value in i.items():
                        convert_dict[key] = int(value)

                    new_list_dict.append(convert_dict)
                dict_list = new_list_dict

                instance_list = []
                for j in dict_list:
                    instance_list.append(cls.create(**j))

                return instance_list
        except FileNotFoundError:
            return []
