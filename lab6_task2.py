from PIL import Image

im = Image.open('drive.jpg')

def map_green_blue(pixel):
	return (pixel[0], int(pixel[1]*.7), int(pixel[2]*.7))

new_list = map(map_green_blue, im.getdata())

im.putdata(list(new_list))

im.save('driveSunset.jpg')
im.show()