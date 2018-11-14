#Name: Aaron Parks
#Partner: Isaac
#Date: September 29, 2018
#Course: CST 205
#Description This code takes in multiple images and combines them in order to remove unwanted elements using a median filter.

from PIL import Image
import glob

#This function makes a new image named median using the median pixel of all images from each coordinate
def median_image(images):
	new_image = Image.new('RGB', (images[0].width, images[0].height))
	#The nested for loops create a new image by finding the median pixel value and then putting it into a blank image
	for x in range (images[0].width):
		for y in range (images[0].height):
			pixels = []
			#This for loop puts the pixel at (x, y) from each image into an array
			for z in range(len(images)):
				pixels.append(images[z].getpixel((x, y)))
			red_pixels = sorted(pixels, key=lambda tup: tup[0])
			green_pixels = sorted(pixels, key=lambda tup: tup[1])
			blue_pixels = sorted(pixels, key=lambda tup: tup[2])
			median = int((len(pixels) + 1) / 2) - 1
			new_image.putpixel((x, y), (red_pixels[median][0], green_pixels[median][1], blue_pixels[median][2]))
	new_image.save("median.png")


images = []

#This for loop uses the glob function to open all images in the hw2_images directory, and then it puts the images into the images list.
for filename in glob.glob("hw2_images/*.png"):
	im = Image.open(filename)
	images.append(im)
median_image(images)


