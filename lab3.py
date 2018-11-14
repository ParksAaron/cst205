color_dictionary = {
	"red": (255, 0, 0),
	"green": (0, 255, 0),
	"blue": (0, 0, 255),
	"magenta": (255, 0, 255),
	"cyan": (0, 255, 255),
	"yellow": (255, 255, 0)
}

print("The blue channel of magenta has value " + str(color_dictionary["magenta"][2]))
print("The green channel of yellow has value " + str(color_dictionary["yellow"][1]))
print("The red channel of cyan has value " + str(color_dictionary["cyan"][0]))
for key, value in color_dictionary.items():
	if key.find('e') == 1:
		print(value)

tineye_sample = {
    "status": "ok",
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141, 125, 83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35, 22, 19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

print(tineye_sample["result"][0]["color"][0])
print(tineye_sample["result"][1]["color"][2])