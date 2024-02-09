#!/usr/bin/python3
"""
User class
"""


class User():
    """ Here is the class of my user """

    def __init__(self):
        """ The constructor """
        self.__email = None

    @property
    def email(self):
        """ Getter """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    # x = User()
    # x.email = 5 Here is gives a TypeError
    print(u.email)
