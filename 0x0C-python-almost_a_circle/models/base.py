#!/usr/bin/python3
''' Class named Base '''
import json
import csv
import turtle

class Base:
    """Base class for managing id attribute in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#####-----JSON-----#####
    @staticmethod
    def to_json_string(list_dictionaries):
        '''  '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    #--------------------------------------

    @staticmethod
    def from_json_string(json_string):
        '''   '''
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        '''  '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    #---------------------------------------
