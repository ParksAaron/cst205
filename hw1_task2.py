# Aaron Parks
# CST205
# 9/16/18
# This program opens and unpickles a file which contains many rgb intensities. It then plots all of the intensities onto a histogram.
import hist_machine as hp
import pickle

with open(r"image_matrix.pickle", "rb") as input_file:
		rgb = pickle.load(input_file)

def task2(rgb):

	red = []
	green = []
	blue = []

	for x in range(256):
		red.append(0)
		green.append(0)
		blue.append(0)

	for x in rgb:
		for y in x:
			red[y[0]] = red[y[0]] + 1
			green[y[1]] = green[y[1]] + 1
			blue[y[2]] = blue[y[2]] + 1
	return [red, green, blue];
 
hp.hist_plotter(task2(rgb))



