from PIL import Image

source = Image.open("lab7img.jpg")
pixels = source.load()
greatest = pixels[0, 0]
greatest_coord = [0, 0]

for x in range(source.width):
	for y in range(source.height):
		if pixels[x, y][0] > greatest[0]:
			greatest = pixels[x, y]
			greatest_coord[0] = x
			greatest_coord[1] = y


print(greatest_coord)
