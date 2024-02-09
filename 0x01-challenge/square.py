#!/usr/bin/python3
"""My square class"""


class Square():
    """Here is the class"""
    side = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def PermiterOfMySquare(self):
        return self.side * 4

    def __str__(self):
        return "A square with a side length of {}".format(self.side)


if __name__ == "__main__":
    """The height should be the same as the width"""
    # s = Square(width=12, height=9)
    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
