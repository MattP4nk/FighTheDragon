from PyQt6 import QtCore, QtGui, QtWidgets, uic 
import DragonClass, PlayerClass, sys
from random import randint
from time import sleep
from threading import Event


app = QtWidgets.QApplication(sys.argv)
player = None
dragon = DragonClass.Dragon("Ancient Dragon", 1500, 30, 30, 60, 50)
contador = 0

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
		self.attack_Button.clicked.connect(self.player_Attack)
		self.defence_Button.clicked.connect(self.player_Defence)
		#self.caballier_Button.clicked.connect(self.choice1)

	def player_Attack(self):
		message = PlayerClass.Player.Attack(player, dragon)
		MainWindow.battle_log(window, message)
		MainWindow.turn(self)

	def player_Defence(self):
		message = PlayerClass.Player.Defending(player)
		MainWindow.battle_log(window, message)
		MainWindow.turn(self)

	def dragon_Attack(self):
		objetive = dragon_objective()
		message = DragonClass.Dragon.Attack(dragon, objetive)
		MainWindow.battle_log(window, message)
		MainWindow.turn(self)

	def status(self): #registro de status y continuacion de juego
		player_status, player_flag = PlayerClass.Player.Status(player, dragon)
		self.player_Status.setText(player_status)
		dragon_status, dragon_flag = DragonClass.Dragon.Status(dragon)
		self.dragon_Status.setText(dragon_status)
		if player_flag == False or dragon_flag == False: #Check for deaths
			MainWindow.terminate(self)

	def terminate(self):
		self.attack_Button.setEnabled(False)
		self.defence_Button.setEnabled(False)
		self.class_Button.setEnabled(False)
		turns = int(contador / 2)
		if player.life > dragon.DragonLife:
			last_text = ("And this is how the "+ player.name +" defeated the Ancient Dragon! He only needed "+ str(turns) +" attacks to defeate him")
		else:
			last_text = ("... The dragon reign of terror never stopped. The hero was eaten in "+ str(turns) +" attacks...")
		MainWindow.battle_log(self, last_text)

	def battle_log(self, newlog):
		log = "\n" + newlog
		self.battle_Log.append(log)
		separator = "=" * 24
		self.battle_Log.append(separator)

	def turn(self): #Controlador de interfase y secuencia de turnos.
		MainWindow.status(self)
		global contador
		contador += 1
		if contador % 2 == 0:
			self.attack_Button.setEnabled(True)
			self.defence_Button.setEnabled(True)
			self.class_Button.setEnabled(True)
		else:
			self.attack_Button.setEnabled(False)
			self.defence_Button.setEnabled(False)
			self.class_Button.setEnabled(False)
			MainWindow.dragon_Attack(self)
		MainWindow.status(self)

def dragon_objective(): #Here it's defined the Dragon Attack objective 
	global player
	if player.aCompanion == 1:
		a = randint(1, 6)
		if a<3 or player.taunt == 1:
			objetive = bear
		else:
			objetive = player
	else:
			objetive = player
	return objetive


def main():
	turno = 0
	global contador
	choice.exec()
	window.show()




