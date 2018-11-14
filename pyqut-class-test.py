import sys
from PYWT5.QtWidgets import QApplication, QWidget

class Example(QWidget):
	def __init__(self):
		super().__init__(self, x = 0, y = 0, w = 400, h=400, title="")
		self.setGeometry(x, y, w, h)
		self.setWindowTitle("title")
		self.show()

app = QApplication(sys.argv)
ex = Example()
ex2 = Example(100, 100, 200, 200, "Hello?")
sys.exit(app.exec_())
