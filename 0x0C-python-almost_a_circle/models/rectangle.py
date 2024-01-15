#!/usr/bin/python3
''' Class named Rectangle '''
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # id From Base

#####-----Width-----#####

    @property
    def width(self):
        ''' Returns width '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

#####-----Height-----#####

    @property
    def height(self):
        ''' Returns height '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

#####-----X-----#####

    @property
    def x(self):
        ''' Returns x '''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance (value, int):
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

#####-----Y-----#####

    @property
    def y(self):
        ''' It retuns y '''
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance (value, int):
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

#####-----Area-----#####

    def area(self):
        ''' Method returns area of a reactangle '''
        return(self.__width * self.__height)

#####-----Display-----#####

    def display(self):
        ''' Displays rectangle using "#" charactor '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        #[print("") for y in range(self.y)]
        #for h in range(self.height):
        #   [print(' ', end='') for x in range(self.x)]
        #    [print('#', end='') for w in range(self.width)]

        for i in range(self.__height):
            for j in range(self.__width):
               print("#", end="")
            print("$")

#####-----__str__-----#####

    def __str__(self):
        ''' '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height) 

#####-----update-----#####

    def update(self, *args):
        ''' Assigns an argument to each attribute. '''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x
                elif a == 4:
                    self.y = arg
                a = a + 1
        elif kwags and len(kwargs) != 0:
            for k, v in kwags.items():
                if k -- "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.witdth = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = x
                elif k == "y":
                    self.y
#####----Dictionary-----######

    def to_dictionary(self):
        return{
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

