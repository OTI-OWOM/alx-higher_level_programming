#!/usr/bin/python3
"""Student Module"""


class Student:
    """Defines a student class."""

    def  __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


        def to_json(self, attrs=None):
            """Return the dictionary representation of a student instance."""   
            if isinstance(attrs, list) and \
                    (all(isinstance(s, str) for s in attrs)):
                return {k: v for k, v in dict(self._dict_).items() if k in attrs}

            return self.__dict__
