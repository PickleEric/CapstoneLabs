from dataclasses import dataclass

@dataclass
class Artist():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__ (self):
        about_artist = 'About the artist: \nName: ' + self.name + '\nEmail address: ' + self.email
        return about_artist

class Artwork():
    def __init__(self, artist_name, artwork, price, availability):
        self.artist_name = artist_name
        self.artwork = artwork
        self.price = price
        self.availability = availability
    
    def __str__(self):
        about_artwork =  'About the artwork: \nArtist Name: ' + self.artist_name + '\nArtwork: ' + self.artwork + '\nPrice: ' + self.price + 'Available?: ' + self.availability + '\n'
        return about_artwork