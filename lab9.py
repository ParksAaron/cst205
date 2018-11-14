import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

@pyqtSlot()
def button1_on_click(my_window):
	my_label.setText("Button 1 clicked")

@pyqtSlot()
def button2_on_click(my_window):
	my_label.setText("Button 2 clicked")

my_qt_app = QApplication(sys.argv)
my_window = QWidget()
my_window.setGeometry(0, 0, 400, 300)
my_window.setWindowTitle('Lab 9')
my_label = QLabel(my_window)
my_label.setGeometry(QtCore.QRect(0, 0, 300, 50))
my_label.setText('Aaron Parks')
button1 = QPushButton("Button 1", my_window)
button1.move(100, 70)
button1.clicked.connect(lambda: button1_on_click(my_window))
button2 = QPushButton("Button 2", my_window)
button2.move(150, 140)
button2.clicked.connect(lambda: button2_on_click(my_window))
my_window.show()
sys.exit(my_qt_app.exec_())
