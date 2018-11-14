my_data = {
	"audio" : ["flac", "m4a", "mp3", "wav", "ogg", "aiff"],
	"image" : ["jpeg", "gif", "tiff", "png", "svf"]
}

for item in my_data:
	if(my_data[item][3] != "png"):
		print(my_data[item][3])