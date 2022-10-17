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

playlists = [top_100, top_pops, eurovision]
