"""
Project #1     Fall 2019
Song.py - Song class
"""

class Song:

    """
    Constructor for Song object.
    parse a given songRecord string to song object.
    For an example songRecord such as "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    It contains attributes (ID, title, artist, duration, trackID)
    """
    def __init__(self, songRecord):
        attributes = songRecord.split(",")
        self.initialize(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])
        
    """
    Initialize method for Song object.
    Receives the attributes (ID, title, artist, duration, trackID) to assign them
    to the Song object
    """
    def initialize(self, ID, title, artist, duration, trackID):
        self.ID = ID
        self.title = title
        self.artist = artist
        self.duration = duration
        self.trackID = trackID

    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    sampleSongRecord = "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    sampleSong = Song(sampleSongRecord)
    print(sampleSong.toString())