#Aaron Parks
#Partner: Isaac
#10/29/18
#CST 205 HW 4
#Abstract: The main application file to run for a flask app that randomely generates images and provides information about them.
import sys
import random
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from PIL import Image
sys.path.insert(0, 'Desktop/cst205/')
from image_info import image_info

app = Flask(__name__, static_folder="images")
bootstrap = Bootstrap(app)

@app.route('/')
def home():
	choices = []
	for i in range(0, 3):
		random_image = (random.choice(image_info))
		if(i > 0):
			for choice in choices:
				if(choice['id'] == random_image['id']):
					while(choice['id'] == random_image['id']):
						random_image = (random.choice(image_info))
		choices.append(random_image)

	return render_template('hw4_home.html', images=choices)

@app.route("/pictures/")
@app.route("/pictures/<id>")
def pictures(id):
	title = request.args.get('title')
	user = request.args.get('user')
	source = "images/" + id + ".jpg"
	im = Image.open(source)
	mode = im.mode
	form = im.format
	width, height = im.size
	return render_template('hw4_pictures.html', id=id, title=title, user=user, mode=mode, form=form, width=width, height=height)