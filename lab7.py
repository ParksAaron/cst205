from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color
from PIL import Image


def chromakey(source, bg):
	for x in range(source.width):
		for y in range(source.height):

			cur_pixel = source.getpixel((x, y))
			green = sRGBColor(0, 190, 60)
			cur_pixel_rgb = sRGBColor(cur_pixel[0], cur_pixel[1], cur_pixel[2])
			cur_pixel_lab = convert_color(cur_pixel_rgb, LabColor)
			green_lab = convert_color(green, LabColor)

			if delta_e_cie2000(cur_pixel_lab, green_lab) < 10:
				source.putpixel((x, y), bg.getpixel((x, y)))

	source.save("chromakeyed.png")

main = Image.open("green.jpg")
background = Image.open("background.jpg")

chromakey(main, background)


