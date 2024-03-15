from PyQt6 import QtCore, QtGui, QtWidgets, uic 
from DragonClass import *
from PlayerClass import *
from random import randint
from time import sleep
import sys



app = QtWidgets.QApplication(sys.argv)
player = None

dragon = DragonClass.Dragon("Ancient Dragon", 1500, 30, 30, 60, 50)
class choiceWindow(QtWidgets.QDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi("choice.ui", self)
		self.caballier_Button.clicked.connect(self.choice1)
		self.caballier_Button.clicked.connect(self.Close)
		self.lancer_Button.clicked.connect(self.choice2)
		self.lancer_Button.clicked.connect(self.Close)
		self.archer_Button.clicked.connect(self.choice3)
		self.archer_Button.clicked.connect(self.Close)


	def choice1(self):
		Player, newlog = PlayerClass.Player.Choice(1)
		MainWindow.battle_log(window, newlog)
		global player
		player = Player
	def choice2(self):
		Player, newlog = PlayerClass.Player.Choice(2)
		MainWindow.battle_log(window, newlog)
		global player
		player = Player
	def choice3(self):
		Player, newlog = PlayerClass.Player.Choice(3)
		MainWindow.battle_log(window, newlog)
		global player
		player = Player


		

	def Close(self):
		choice.close()


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi("frame.ui", self)
		self.battle_Log.setStyleSheet("color: white; background: url(dragon.png); font: 12pt Arial;")
		self.dragon_Status.setStyleSheet("color: white; background-color: black;font: 12pt Arial;")
		self.player_Status.setStyleSheet("color: white; background-color: black; font: 12pt Arial;")

	def status(self):
		player_status = PlayerClass.Player.Status(player)
		self.player_Status.setText(player_status)
		dragon_status = DragonClass.Dragon.Status(dragon)
		self.dragon_Status.setText(dragon_status)

	def battle_log(self, newlog):
		log = "\n" + newlog
		self.battle_Log.append(log)

if __name__ == "__main__":
	window = MainWindow()
	choice = choiceWindow()
	window.show()
	choice.exec()
	MainWindow.status(window)
	sys.exit(app.exec())