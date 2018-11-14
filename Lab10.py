import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtGui import QColor

colors = {
	"Pick a color": ["", ""],
	"Peach Puff": [(255, 218, 185), "FFDAB9"],
	"Powder Blue": [(176, 224, 230), "B0E0E6"]
}

class NewWindow(QWidget):
	def __init__(self):
		super().__init__()
		
class Window(QWidget):
    def __init__(self):
    	super().__init__()

    	self.my_combo_box = QComboBox()
    	self.my_combo_box.addItems(colors)
    	self.rgb = QLabel("RGB: ")
    	self.hexa = QLabel("Hex: ")
    	self.showColor = QPushButton('View the color')

    	vbox = QVBoxLayout()
    	vbox.addWidget(self.my_combo_box)
    	vbox.addWidget(self.rgb)
    	vbox.addWidget(self.hexa)
    	vbox.addWidget(self.showColor)

    	self.setLayout(vbox)
    	self.my_combo_box.currentIndexChanged.connect(self.update_ui)
    	self.showColor.clicked.connect(self.open_window)
    	self.setWindowTitle("Colors!")

    @pyqtSlot()
    def open_window(self):
    	my_text = self.my_combo_box.currentText()
    	my_index = self.my_combo_box.currentIndex()
    	self.new_window = NewWindow()
    	self.new_window.setAutoFillBackground(True)
    	backgroundColor = self.new_window.palette()
    	backgroundColor.setColor(self.new_window.backgroundRole(), QColor(colors[my_text][0][0], colors[my_text][0][1], colors[my_text][0][2]))
    	self.new_window.setPalette(backgroundColor)
    	self.new_window.show()

	@pyqtSlot()
    def update_ui(self):
    	my_text = self.my_combo_box.currentText()
    	my_index = self.my_combo_box.currentIndex()
    	self.rgb.setText(f'RGB: {colors[my_text][0]}')
    	self.hexa.setText(f'Hex: {colors[my_text][1]}')

app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())