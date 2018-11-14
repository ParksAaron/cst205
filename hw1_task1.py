# Aaron Parks
# 9/16/18
# CST 205
# This program opens and unpickles a pickled file that contains rgb intensities, and then it prints out rgb bin pixel itensities for the entire file using a dictionary.
import pickle

color_bins = {
	'red': [0, 0, 0, 0],
	'green': [0,0, 0, 0],
	'blue': [0, 0, 0, 0]
}

with open(r"image_matrix.pickle", "rb") as input_file:
	rgb = pickle.load(input_file)
for x in rgb:
	for y in x:
		if y[0] <= 63:
			color_bins['red'][0] = color_bins['red'][0] + 1
		elif 64 <= y[0] <= 127 :
			color_bins['red'][1] = color_bins['red'][1] + 1
		elif 128 <= y[0] <= 191 :
			color_bins['red'][2] = color_bins['red'][2] + 1
		elif 192 <= y[0] <= 255 :
			color_bins['red'][3] = color_bins['red'][3] + 1
		if y[1] <= 63:
			color_bins['green'][0] = color_bins['green'][0] + 1
		elif 64 <= y[1] <= 127 :
			color_bins['green'][1] = color_bins['green'][1] + 1
		elif 128 <= y[1] <= 191 :
			color_bins['green'][2] = color_bins['green'][2] + 1
		elif 192 <= y[1] <= 255 :
			color_bins['green'][3] = color_bins['green'][3] + 1
		if y[2] <= 63:
			color_bins['blue'][0] = color_bins['blue'][0] + 1
		elif 64 <= y[2] <= 127 :
			color_bins['blue'][1] = color_bins['blue'][1] + 1
		elif 128 <= y[2] <= 191 :
			color_bins['blue'][2] = color_bins['blue'][2] + 1
		elif 192 <= y[2] <= 255 :
			color_bins['blue'][3] = color_bins['blue'][3] + 1
print(color_bins)


