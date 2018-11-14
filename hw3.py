"""
Name: Aaron Parks
Date: 10/12/18
Course: CST 205
Abstract: This program creates a GUI where a user can search for an image and apply a chosen filter to the given image.

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PIL import Image

#Creates a list of the given photos' information
image_info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]

#A list of the different filters that can be applied
manipulations = ["Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

#Used to create a new window
class NewWindow(QWidget):
  def __init__(self):
    super().__init__()

#Creates main window
class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.search = QLineEdit(self)

    #creates combo box and adds filter list into the options to be chosen from
    self.manipCombo = QComboBox()
    self.manipCombo.addItems(manipulations)

    self.searchBtn = QPushButton('Search')

    #sets the layout and adds in the created search bar, combo box, and button
    vbox = QVBoxLayout()
    vbox.addWidget(self.search)
    vbox.addWidget(self.manipCombo)
    vbox.addWidget(self.searchBtn)
    self.setLayout(vbox)
    self.searchBtn.clicked.connect(self.open_window)
    self.setWindowTitle("Homework 3")

  #Checks to see if a substirng is in a larger string (used in image search)
  def isInString(self, substring, originalString):
    if substring.lower() in originalString.lower():
        return True
    else:
        return False

  #Turns every pixel into grayscale (used in grayscale function)
  def lum_image(self, p):
      new_red = int(p[0] * 0.299)
      new_green = int(p[1] * 0.587)
      new_blue = int(p[2] * 0.114)
      luminance = new_red + new_green + new_blue
      return (luminance,) * 3

  #Turns an image into grayscale
  def grayscale(self, path):
    im = Image.open(path)

    new_list = map( self.lum_image, im.getdata() )
    im.putdata(list(new_list))
    im.save('images/gray.jpg')

  #Applies a sepia filter to an image
  def sepia(self, path):
    im = Image.open(path)

    new_list = []
    for i in im.getdata():
      new_val = (0.3 * i[0] + 0.59 * i[1] + 0.11 * i[2])

      new_red = int(new_val * 2)
      if new_red > 255:
        new_red = 255
      new_green = int(new_val * 1.5)
      if new_green > 255:
          new_green = 255
      new_blue = int(new_val)
      if new_blue > 255:
        new_blue = 255

      new_list.append((new_red, new_green, new_blue))
    im.putdata(new_list)
    im.save('images/sepia.jpg')

  #Applies a negative filter to an image
  def negative(self, path):
    im = Image.open(path)

    negative_list = map( self.negative_image, im.getdata() )
    im.putdata(list(negative_list))
    im.save('images/negative.jpg')

  #Applies a negative filter to a pixel (used in negative function)
  def negative_image(self, pixel):
    return tuple(map(lambda a : 255 - a, pixel))

  #Decreases the size of an image by 1/2
  def thumbnail(self, path):
    im = Image.open(path)
    width, height = im.size
    im = im.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
    im.save('images/thumbnail.jpg')

  #Is called when the search button is pressed and is used to open a new window with an image (all search logic is also done here)
  @pyqtSlot()
  def open_window(self):
      count = []
      #Puts all information for all given images into a new list of dictionaries that includes a counter
      for info in image_info:
        data = {
          "id" : info['id'],
          "count" : 0,
          "title" : info['title']
        }
        count.append(data)

      #reads in the user input from the search bar and splits it into an array of strings
      searched = self.search.text()
      searchedList = searched.split()

      #The nested for loops search the every images title and tags for the searched words and adds 1 to the images counter whenever a match is found
      for word in searchedList:
        for x in range(0, len(image_info)):
          if(self.isInString(word, image_info[x]['title'])):
            count[x]['count'] = count[x]['count'] + 1
          for tag in image_info[x]['tags']:
            if(self.isInString(word, tag)):
              count[x]['count'] = count[x]['count'] + 1
      
      #Sorts the list of image information by each image's counter
      sortedCount = sorted(count, key=lambda k: k['count'], reverse=True)
      tied = []
      isTied = False

      #Checks for "ties" in the images' counters, and if any are found puts their information into a new list
      for x in range(0, (len(count))):
        if(sortedCount[0]['count'] == sortedCount[x]['count']):
            if (x == 0):
              dataZero = {
              "id" : sortedCount[x]['id'],
              "count" : sortedCount[x]['count'],
              "title" : sortedCount[x]['title']
              } 
              tied.append(dataZero)
            else:
              isTied = True
              data = {
                "id" : sortedCount[x]['id'],
                "count" : sortedCount[x]['count'],
                "title" : sortedCount[x]['title']
              } 
              tied.append(data) 
      
      #If there is a "counter tie" the list containing the information of the tied images is sorted alphabetically by the images' title     
      if(isTied == True):
        sorted(tied, key = lambda i: i['title']) 

      #Sets the file path of the image that is the closest match to the search
      path = "images/" + tied[0]['id'] + ".jpg"

      #Applies a filter to the image depending on what was selected in the main window
      manipulation = self.manipCombo.currentText()
      if(manipulation == "Grayscale"):
        self.grayscale(path)
        path = 'images/gray.jpg'
      
      elif(manipulation == "Sepia"):
        self.sepia(path)
        path = 'images/sepia.jpg'

      elif(manipulation == "Negative"):
        self.negative(path)
        path = 'images/negative.jpg'

      elif(manipulation == "Thumbnail"):
        self.thumbnail(path)
        path = 'images/thumbnail.jpg'

      #Displays the image in a new window.q
      self.new_window = NewWindow()
      newLay = QVBoxLayout()
      pixLabel = QLabel(self.new_window)
      pixmap = QPixmap(path)
      pixLabel.setPixmap(pixmap)
      newLay.addWidget(pixLabel)
      self.new_window.setLayout(newLay)
      self.new_window.resize(pixmap.width(),pixmap.height())
      self.new_window.show()



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())


