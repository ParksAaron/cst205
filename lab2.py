import math

red = int(input("Red Channel: "))
green = int(input("Green Channel: "))
blue = int(input("Blue Channel: "))
rgb = (red, green, blue)
if (rgb[0] == rgb[1]):
	print("The color is a shade of yellow.")
elif (rgb[0] == rgb[2]):
	print("The color is a shade of magenta.")
elif (rgb[1] == rgb[2]):
	print("The color is a shade of cyan.")
elif (rgb[0] > rgb[1]) and (rgb[0] > rgb[2]):
	print("The color is reddish.")
elif (rgb[1] > rgb[0]) and (rgb[1] > rgb[2]):
	print("The color is greenish.")
elif (rgb[2] > rgb[0]) and (rgb[2] > rgb[1]):
	print("The color is bluish.")

hexadecimal = input("Enter a hexadecimal color value: #")
hex_rgb = [0, 0, 0]
x = 0
while x < 3:
	if hexadecimal[0].isdigit() == True:
		hex_rgb[x] = int(hexadecimal[0]) * 16
	else:
		if hexadecimal[0] == 'A':
			hex_rgb[x] = 10 * 16
		elif hexadecimal[0] == 'B':
			hex_rgb[x] = 11 * 16
		elif hexadecimal[0] == 'C':
			hex_rgb[x] = 12 * 16
		elif hexadecimal[0] == 'D':
			hex_rgb[x] = 13 * 16
		elif hexadecimal[0] == 'E':
			hex_rgb[x] = 14 * 16
		elif hexadecimal[0] == 'F':
			hex_rgb[x] = 15 * 16
	if hexadecimal[1].isdigit() == True:
		hex_rgb[x] = hex_rgb[x] + int(hexadecimal[1])
	else:
		if hexadecimal[1] == 'A':
			hex_rgb[x] = hex_rgb[x] + 10
		elif hexadecimal[1] == 'B':
			hex_rgb[x] = hex_rgb[x] + 11
		elif hexadecimal[1] == 'C':
			hex_rgb[x] = hex_rgb[x] + 12
		elif hexadecimal[1] == 'D':
			hex_rgb[x] = hex_rgb[x] + 13
		elif hexadecimal[1] == 'E':
			hex_rgb[x] = hex_rgb[x] + 14
		elif hexadecimal[1] == 'F':
			hex_rgb[x] = hex_rgb[x] + 15
	x = x + 1
	hexadecimal = hexadecimal[1:]
	hexadecimal = hexadecimal[1:]
rgb2 = (hex_rgb[0], hex_rgb[1], hex_rgb[2])
print("(", rgb2[0], ", ", rgb2[1], ", ", rgb2[2], ")")

red2 = int(input("Red Channel: "))
green2 = int(input("Green Channel: "))
blue2 = int(input("Blue Channel: "))
rgb3 = [red2, green2, blue2]
hex_from_rgb = "#"
y = 0
while y < 3:
	var = rgb3[y] % 16
	if var == 0:
		rgb3[y] = rgb3[y] / 16
		if rgb[y] == 10:
			hex_from_rgb = hex_from_rgb + 'A' + "0"
		elif rgb3[y] == 11:
			hex_from_rgb = hex_from_rgb + 'B' + "0"
		elif rgb3[y] == 12:
			hex_from_rgb = hex_from_rgb + 'C' + "0"
		elif rgb3[y] == 13:
			hex_from_rgb = hex_from_rgb + "D" + "0"
		elif rgb3[y] == 14:
			hex_from_rgb = hex_from_rgb + "E" + "0"
		elif rgb3[y] == 15:
			hex_from_rgb = hex_from_rgb + "F" + "0"
		else:
			hex_from_rgb = hex_from_rgb + (str(rgb3[y]) + "0")
	else:
		temp = (math.floor(rgb3[y] / 16)) % 16
		if temp == 10:
			hextemp = 'A'
		elif temp == 11:
			hextemp = 'B'
		elif temp == 12:
			hextemp = 'C'
		elif temp == 13:
			hextemp = 'D'
		elif temp == 14:
			hextemp = 'E'
		elif temp == 15:
			hextemp = 'F'
		else:
			hextemp = str(temp)
		if var == 10:
			hex_from_rgb = hex_from_rgb + hextemp + 'A'
		elif var == 11:
			hex_from_rgb = hex_from_rgb + hextemp + 'B'
		elif var == 12:
			hex_from_rgb = hex_from_rgb + hextemp + 'C'
		elif var == 13:
			hex_from_rgb = hex_from_rgb + hextemp + 'D'
		elif var == 14:
			hex_from_rgb = hex_from_rgb + hextemp + 'E'
		elif var == 15:
			hex_from_rgb = hex_from_rgb + hextemp + 'F'
		else:
			hex_from_rgb = hex_from_rgb + hextemp + str(var)
	y = y + 1
print(hex_from_rgb)



		

