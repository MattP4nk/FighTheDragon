#Fight The Dragon GUI
import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCursor


class Main_Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Fight The Dragon")
		self.setFixedWidth(1000)
		self.setStyleSheet("background: #000000;")
		self.show()
		self.setLayout(QGridLayout())
		
		
		#FONDO
		image = QPixmap("dragon.png")
		holder = QLabel()
		holder.setPixmap(image)
		self.layout().addWidget(holder, 0, 0, Qt.AlignmentFlag.AlignCenter)

		#BOTONES
		attack = QPushButton("Attack")
		defence = QPushButton("Defence")
		special = QPushButton("Class Abilitys")
		self.layout().addWidget(attack)
		self.layout().addWidget(defence)
		self.layout().addWidget(special)

app = QApplication(sys.argv)
window = Main_Window()
window.show()
sys.exit(app.exec())