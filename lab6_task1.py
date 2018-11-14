from PIL import Image
im = Image.open('cyber.jpg')

def negative_image(pixel):
	return tuple(map(lambda a : 255 - a, pixel))

negative_list = map(negative_image, im.getdata())
im.putdata(list(negative_list))
im.save('negative.jpg')

im = Image.open('negative.jpg')
negative_list = map(negative_image, im.getdata())
im.putdata(list(negative_list))
im.save('negative_negative.jpg')

im = Image.open('negative_negative.jpg')
im.show()