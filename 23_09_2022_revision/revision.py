# Output
# print("Hello")
# print(1234)

# Variables
# Assigning the value 1234 to the variable foo and then printing the value of foo.
# foo = 1234
# print(foo)

# Assigning the value "Hello" to the variable name and then printing the value of name.
# name = "Hello"
# print(name)

# Classes

# The class Point2D is a blueprint for creating objects that represent a point in 2D space
class Point2D:
    def __init__(self, x, y):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object
        of a class is instantiated. The method is useful to do any initialization you want to do with
        your object

        :param x: The x coordinate of the point
        :param y: The target variable
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        The __str__ function is a special function that is called when you use the print() function on
        an object
        :return: The string "Coords {self.x}, {self.y}"
        """
        return f"Coords {self.x}, {self.y}"

    def __add__(self, other):
        """
        The function takes two Point2D objects as arguments, adds their x and y attributes, and returns
        a new Point2D object with the sum of the x and y attributes

        :param other: The other object that is being added to the current object
        :return: The result of the addition of the two points.
        """
        x = self.x + other.x
        y = self.y + other.y
        result = Point2D(x, y)
        return result


def point_adder(point1, point2):
    """
    It takes two Point2D objects as input, adds their x and y coordinates, and returns a new Point2D
    object with the sum of the x and y coordinates

    :param point1: A Point2D object
    :param point2: Point2D
    :return: A new Point2D object with the sum of the x and y coordinates of the two points.
    """
    x = point1.x + point2.x
    y = point1.y + point2.y
    result = Point2D(x, y)
    return result


# The code is creating a Point2D object with the coordinates (-5, 10) and then printing it.
point1 = Point2D(1, 1)
print(point1)
str_point = str(point1)

# Creating a Point2D object with the coordinates (1, 1) and then printing it.
point2 = Point2D(1, 1)
print(point2)
str_point = str(point2)

# Calling the function point_adder() with the arguments point1 and point2. The function
# returns a new Point2D object with the sum of the x and y coordinates of the two points. The function
#
# then prints the new Point2D object.
new_point = point_adder(point1, point2)
print(new_point)

# Calling the __add__ function on the Point2D class.
new_point2 = point1 + point2
print(new_point2)


class Track:
    """
    This is a Track object
    Required Properties:
      Title
      Artist
      Duration
    """

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    """
    This is a Playlist object
    Required Properties:
      Tracks
      Title
      Creator
    """

    def __init__(self, tracks, title, creator):
        self.tracks = tracks
        self.title = title
        self.creator = creator

    def add_track(self, track):
        self.tracks.append(track)
        print(f"Added track {track}")


top_100 = Playlist([], "Top 100", "Billboard")

top_pops = Playlist([], "Top of the Pops", "Billboard")

eurovision = Playlist([], "Eurovision", "The EU")
eurovision.add_track(Track("Ievan Polkka", "Loituma", "2:43"))
eurovision.add_track(Track("Husavik", "Will Ferrell, My Marrianne", "3:22"))
eurovision.add_track(Track("Vitas", "The 7th Element", "4:09"))
