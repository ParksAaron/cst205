from PIL import Image

class Song:
	"""A class that contains all information regarding a song"""
	def __init__(self, artist, genre, length, album):
		self.artist = artist
		self.genre = genre
		self.length = length
		self.album = album

im = Image.open("0.jpg")
print(dir(im))

elizabeth = Song("Elizabeth", "Westside Gunn", "Rap", 248, "Supreme Blientele")
noBystanders = Song("No Bystanders", "Travis Scott", "Rap", 218, "Astroworld")