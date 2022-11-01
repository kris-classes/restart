#print("hello")

#print(1234)

#foo = 1234
#print(foo)
#name = "Hello"
#print(name)


#classes
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coords {self.x}, {self.y}"

    def __add__(self, other):
        x = point1.x + other.x
        y = point1.y + point2.y
        point3 = Point2D(x, y)
        return point3 
            

def point_adder(point1, point2):
    x = point1.x + point2.x
    y = point1.y + point2.y
    point3 = Point2D(x, y)
    return point3
    
#code creating 2D object
point1 = Point2D(1, 1)
print(point1)
str_point = str(point1)

point2 = Point2D(1, 1)
print(point2)
str_point = str(point2)

new_point = point_adder(point1, point2)
print(new_point)

new_point2 = point1 + point2
print(new_point2)


class Track():
 '''
This is a Track object
Required Properties
Title
Artist
Duration
'''
def __ini__(self, title, artist, duration):
    self.title = title
    self.artist =artist
    self.duration = duration

class Playlist():
 '''
 This is a playlist object
  Required propeerties:
    Tracks
    Title
    Creator
  '''

    def __init__(self, tracks, title, creator):
        self.tracks = tracks
        self.title = title
        self.creator = creator

 def add_track(self, track):
    self.tracks.append(track)
    print(f"Added track {track}")

top_100 = Playlist([], "Top 100", "Billboard")

top_20_pops = Playlist([], "Top of the Pops", "Billboard")

eurovision = Playlist([], "Eurovision", "The EU")
eurovision.add_track(Track(" Ievan Polkka", "loituma", "2.43"))
eurovision.add_track(Track("Husavik", "Will Ferrel", "My Marrianne", "3.22"))
eurovision.add_track(Track("Vitas", "The 7th Element", "4.08"))

playlist = [top_100, top_pops, eurovision]






