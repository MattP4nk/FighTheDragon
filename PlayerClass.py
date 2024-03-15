##self Class
from random import randint
import DragonClass
class Player:
	def __init__(self, name, attack, critical, defence, oAttack, oDefence, life, charge, choice):
		self.name = name
		self.attack = attack
		self.critical = critical
		self.defence = defence
		self.oAttack = oAttack
		self.oDefence = oDefence
		self.life = life
		self.charge = charge
		self.choice = choice
		self.SArmor = 0
		self.SArmorTimer = 0
		self.sacro = 0
		self.stun = 0
		self.defending = 0
		self.guide = 0
		self.miss = 0
		self.cover = 0
		self.taunt = 0
		self.aCompanion = 0
		self.sBomb = 0
		self.sArrow = 0
		self.sArrowNumber = 0
		self.Bleed = 0
		self.armorDown = 0 
		self.aDTimer = 0
		self.maim = 0
		self.maimTimer = 0

	def Choice(choice): #Here we pick the player type.
		if choice==1:
			player = Player("Caballier", 30, 60, 50, 20, 30, 100, 2, 1)
			text = ("You took the sword of Durandal!\n*Caballier history*\nIn front of the gates of the castle the dragons roars!")
			return player, text
		elif choice==2:
			player = Player("Lancer", 50, 60, 30, 30, 20, 100, 2, 2)
			text = ("The migthy Dragonlance shine in your hands\n*Lancer history*\nIn front of the gates of the castle the dragons roars!")
			return player, text
		elif choice==3:
			player = Player("Archer", 60, 70, 20, 40, 10, 100, 2, 3)
			text = ("The sacred bow, the heavy Balista\n*Archer history*\nIn front of the gates of the castle the dragons roars!")
			return player, text
		'''
		else:
			print("That's not a sacred weapon, we will pick one for you!")
			choice = randint (1,3)
			if choice==1:
				caballier = Player("Caballier", 30, 60, 50, 20, 30, 100, 2, 1)
				text = ("You took the sword of Durandal!\n*Caballier history*\nIn front of the gates of the castle the dragons roars!")
				return caballier, text
			elif choice==2:
				lancer = Player("Lancer", 50, 60, 30, 30, 20, 100, 2, 2)
				text = ("The migthy Dragonlance shine in your hands\n*Lancer history*\nIn front of the gates of the castle the dragons roars!")
				return lancer, text
			elif choice==3:
				archer = Player("Archer", 60, 70, 20, 40, 10, 100, 2, 3)
				text = ("The sacred bow, the heavy Balista\n*Archer history*\nIn front of the gates of the castle the dragons roars!")
				return archer, text
		'''
	def Status(self):
		effects = Player.TimerEffects(self, Dragon)
		armor = self.defence - self.armorDown + self.SArmor
		attack = self.attack - self.maim
		if self.choice ==4:
			unit = "COMPANION "
		else:
			unit = "PLAYER "
		status = (unit + " STATUS\n Life: " + str(self.life) + " Type: " + self.name + "\n Attack: " + str(attack) +" Defence: "+ str(armor))
		if self.sArrowNumber>0:
			status += ("\nSpecial Arrow left: ", self.sArrowNumber)
		if self.sacro>0:
			status += ("\nDurandal shines filled with sacred power!")
		if effects != "":
			status+= effects
		if self.life > 0:
			player_flag = True
		else:
			player_flag = False
		return status, player_flag

	def TimerEffects(self, Dragon):
		effects = ""
		#SArmor
		if Dragon.FireRain >0:
			FireDamage = randint (10, 15)
			self.life -= FireDamage
			effects += ("\nThe rain of fire hurts the "+self.name+" for "+ FireDamage+" points of damage\nFire Rain: "+ str(Dragon.FireRain)+" turns left")
		if self.aCompanion == 1:
			if bear.life <1:
				self.aCompanion =0
				bear.life = 200
		if self.SArmorTimer>0:
			self.SArmorTimer-=1
		else:
			self.SArmor = 0
		#guide
		if self.guide>0:
			self.guide-1
		else:
			self.critical =60
		#sBomb
		if self.sBomb>0:
			self.sBomb-=1
		#Bleed
		if self.Bleed >0:
			bleed = randint(10, 25)
			self.Bleed -=1
			effects+=("\nThe "+ self.name+" suffers "+ str(bleed) +" points of damage from bleeding!\nBleed: "+ str(self.Bleed)+" turns left")
			self.life -=bleed
			if self.Bleed==0:
				effects+=("\n...and the bleeding has stopped!")
		#armorDown
		if self.aDTimer>0:
			self.aDTimer-=1
		#maim
		if self.maimTimer>0:
			self.maimTimer-=1
		if self.stun == 1:
			effects+=("\nYou are stuned! You lose this turn!")
			self.stun =0
		return effects
	'''
	def Turn(self, objetive):
		
			return None
		else:
			try:
				TurnAction = int(input("1) ATTACK\n2) DEFEND\n3) SKILL\nWhat do you do?: "))
				pass
			except:
				print("And that's how you lose your turn!")
				return None
			if TurnAction > 3 or TurnAction<1:
				print("And that's how you lose your turn!")
				return None
			else:
				if TurnAction ==1:
					Player.Attack(self, objetive)
				elif TurnAction ==3:
					Player.Skill(self, objetive)
	'''			
	def Attack(self, objetive):
		text = []
		message = ""
		if self.choice==1 :
			swordAttack = randint(1,3)
			if swordAttack == 1:
				text.append("Your sword shines pointed at his neck...")
				b = randint (1, 50)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>=1 and Result<=10:
					text.append("... and you barely hit it it for " + str(Result) + " points of damage!")
				if Result>=11 and Result<=20:
					text.append("... and your shallow cut does " + str(Result) + " points of damage!")
				elif Result>=20 and Result<=50:
					objetive.DBleed += randint(2,5)
					text.append("... and tears apart his neck for " + str(Result) + "points of damage!!")
					text.append("The awful wound wont stop bleeding for " + str(objetive.DBleed) +" turns!" )
				elif Result>50:
					objetive.DragonLife = 0
					text.append("Your sword shines gold dealing" + str(Result) + " points of damage and separates the objetive's head from its body!!")
				elif Result == 0:
					text.append("...but you failed at cutting the objetive scales!") # Neck Attack
				if self.sacro > 0:
					text.append("The Sacred Light burns the objetive for " + str(self.sacro) + " points of sacred damage!") 
				objetive.DragonLife-= (Result + self.sacro)
				self.sacro = 0
			elif swordAttack ==2:
				text.append("You charge at the objetive's body, your sword ready for the kill...")
				b = randint (1, 50)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>=1 and Result<=10:
					text.append("... and you scratch it for " + str(Result) + " points of damage!")
				if Result>=11 and Result<=20:
					text.append("... and slash it for " + str(Result) + " points of damage!")
				elif Result>20:
					objetive.DDefBreak += randint(5, 10)
					if objetive.DDefBreak > 30:
						objetive.DDefBreak = 30
					objetive.DDefBreakTimer = randint(2, 4)
					text.append("... and break havoc for " + str(Result) + " points of damage!")
					text.append("You smashed its scales lowering its\ndefence for " + str(objetive.DDefBreakTimer -1) + " turns!")  
				elif Result<1:
					text.append("...but you failed at cutting the objetive scales!")
				if self.sacro > 0:
					text.append("The Sacred Light burns the objetive for " + str(self.sacro) +" points of sacred damage!") 
				objetive.DragonLife-= (Result + self.sacro)
				self.sacro = 0
			else:
				text.append("You aim to hack the objetive legs...")
				b = randint (1, 50)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>=1 and Result<=10:
					text.append("... and you bruise it for "+ str(Result) + " points of damage!")
				if Result>=11 and Result<=20:
					text.append("...and you manage to cut its flesh for "+ str(Result) +  " points of damage")
				elif Result>20:
					objetive.DAtkBreak += randint(5, 10)
					objetive.DAtkBreakTimer += randint(2, 4)
					text.append("... and you manage to maim the Dragon\nfor "+ str(Result) +  " points of damage and debuff it's attack for " +str(objetive.DAtkBreakTimer -1)+ " turns!")
				elif Result<1:
					text.append("... but you failed at cutting the objetive scales!")
				if self.sacro > 0:
					text.append("The Sacred Light punish the objetive for "+ str(self.sacro) + " points of sacred damage!")
				objetive.DragonLife-= (Result + self.sacro)
				self.sacro = 0
		elif self.choice==2:
			SpearAttack = randint(1, 3)
			if SpearAttack == 1: 
				text.append("Your spear roars hungry for its neck...")
				b = randint (-20, 70)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>0 and Result<19:
					text.append("... but its scales are really hard! You\nonly manage to do "+ str(Result) +  " points of damage!")
				elif Result>18:
					objetive.NoBreath = randint(2,4)
					text.append("... and pierces its neck for "+ str(Result) +  "points of damage!!")
					text.append("You pierced its fire sack. The Fire\nBreath won't be able to harm you for "+str(objetive.NoBreath -1)+ " turns!" )
				elif Result<1:  
					text.append("... but you failed to do anything!")
				objetive.DragonLife-=Result
			elif SpearAttack ==2:
				text.append("You aim for the objetive's heart with all your might...")
				b = randint (1, 50)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>0 and Result<19:
					text.append("... but the Dragon jumps back and you don't\nquite reach it! You scrath him for "+ str(Result) + " points of damage!")
				elif Result>19 and Result<60:
					objetive.SealedMagic= randint(2, 4)
					text.append("... and your spear pierces! You stab him\nin the chest for "+ str(Result) + " points of damage!")                            
					text.append("The Dragonlance shines sealing its magic\nfor "+ str(objetive.SealedMagic -1) + " turns!")
				elif Result>60:
					text.append("... The Dragonlance pierces its hearth!\nThe Dragon roars in pain falling to the ground dead!!")
				elif Result<1:
					text.append("... but you failed to do anything!")
				objetive.DragonLife-=Result
			else:
				text.append("The Dragonlance shines calling down lighting...")
				b = randint (1, 50)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>0 and Result<19:
					text.append("... and shocks the Dragon for "+ str(Result) +  " points of damage")
				elif Result>18:
					objetive.NoFlight =  randint(2, 4)
					text.append("... and smashes the objetive to the ground\nfor "+ str(Result) +  " points of damage breaking its wings for " + str(objetive.NoFlight) + " turns!")
				elif Result<1:
					text.append("... but you failed to do anything!")
				objetive.DragonLife-=Result
		elif self.choice==3:
			BowAttack = randint(1, 3)
			if BowAttack == 1:
				text.append("You steady your arm and aim for its eyes...")
				b = randint (-50, 75)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>0 and Result<19:
					text.append("... but the objetive managed to dodge the letal attack!\nYour arrow pierces its cheek for  "+ str(Result) +  " points of damage!")
				elif Result>18:
					objetive.NoVision = randint(1, 3)
					text.append("... and your bolt destroys its eye for "+ str(Result) + " points of damage!!")
					text.append("You pierced one of its eyes leaving it with a blindspot\nfor you to hide for " + str(objetive.NoVision) + " turns!" )
				elif Result<1:
					text.append("... but you failed to do anything!")
				if self.sArrowNumber>0:
					self.sArrowNumber -=1
					elemenDMG = randint(1, 100)
					elemenChance = randint(1, 100)
					if self.sArrow ==1:
						if elemenChance>70:
							text.append("The Lighting Arrow explodes dealing an extra " + str(elemenDMG) +"points of damage stuning the objetive!")
							objetive.Stun = 1
						else:
							text.append("The Lighting Arrow explodes dealing an extra " + str(elemenDMG) +"points of damage!")
					if self.sArrow ==2:
						if elemenChance>70:
							text.append("The Ice Arrow freezes the objetive dealing an extra " + str(elemenDMG) +"points of damage freezing the Dragon wings!")
							objetive.NoFlight = 2
						else:
							text.append("The Ice Arrow freezes the objetive dealing an extra " + str(elemenDMG) +"points of damage!")
					if self.sArrow ==3:
						elemenDMG = int(elemenDMG/10) +(elemenDMG%10>0)
						objetive.Poison += ElemenDMG
						elemenDMG = 0
						objetive.PoisonTimer += randint(1,3)
						text.append("The Poison Arrow intoxicates the objetive dealing an extra " + str(elemenDMG) +"points of damage for " +str(objetive.PoisonTimer) +"turns!")
					objetive.DragonLife -=elemenDMG
				objetive.DragonLife-=Result
			elif BowAttack==2:
				text.append("Remembering your training you aim for its reversed scale!")
				b = randint (-50, 75)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				if Result>0 and Result<19:
					text.append("... but the objetive dodged to the side!\nYour arrow pierces one of its arms for  "+ str(Result) +  " points of damage!")
				elif Result>18:
					objetive.Rage = randint(1,3)
					text.append("... Bullseye!! Your bolt pierces its most painfull\nspot for "+ str(Result) + " points of damage!!")
					text.append("The pain send it into a maddeing rage for " + str(objetive.Rage)+" turns!" )
				elif Result<1:
					text.append("... but you failed to do anything!")
				if self.sArrowNumber>0:
					self.sArrowNumber -=1
					elemenDMG = randint(1, 100)
					elemenChance = randint(1, 100)
					if self.sArrow ==1:
						if elemenChance>70:
							text.append("The Lighting Arrow explodes dealing an extra " + str(elemenDMG) +"points of damage stuning the objetive!")
							objetive.Stun = 1
						else:
							text.append("The Lighting Arrow explodes dealing an extra " + str(elemenDMG) +"points of damage!")
					if self.sArrow ==2:
						if elemenChance>70:
							text.append("The Ice Arrow freezes the objetive dealing an extra " + str(elemenDMG) +"points of damage freezing the Dragon wings!")
							objetive.NoFlight = 2
						else:
							text.append("The Ice Arrow freezes the objetive dealing an extra " + str(elemenDMG) +"points of damage!")
					if self.sArrow ==3:
						elemenDMG = int(elemenDMG/10) +(elemenDMG%10>0)
						objetive.Poison += elemenDMG
						elemenDMG = 0
						objetive.PoisonTimer += randint(1,3)
						text.append("The Poison Arrow intoxicates the objetive dealing an extra " + str(elemenDMG) +"points of damage for "+str(objetive.PoisonTimer) +"turns!")
					objetive.DragonLife -=elemenDMG
				objetive.DragonLife-=Result
			else:
				text.append("You shoot a rain of bolts!")
				SpA = 0
				Total = 0
				Daños =[]
				while SpA<5:
					b = randint (-50, 75)
					Result, DamText = Player.Damage(self, b, objetive)
					text.append(DamText)
					if Result>0:
						Daños.append(Result)
						Total += Result
						if self.sArrowNumber>0:
							self.sArrowNumber -=1
							elemenDMG = randint(1, 100)
							elemenChance = randint(1, 100)
							if self.sArrow ==1:
								if elemenChance>70:
									text.append("The Lighting Arrow explodes dealing an extra " + str(elemenDMG) +"points of damage stuning the objetive!")
									objetive.Stun = 1
								else:
									text.append("The Lighting Arrow explodes dealing an extra " + str(elemenDMG) +"points of damage!")
							if self.sArrow ==2:
								if elemenChance>70:
									text.append("The Ice Arrow freezes the objetive dealing an extra " + str(elemenDMG) +"points of damage freezing the Dragon wings!")
									objetive.NoFlight = 2
								else:
									text.append("The Ice Arrow freezes the objetive dealing an extra " + str(elemenDMG) +"points of damage!")
							if self.sArrow ==3:
								elemenDMG = int(elemenDMG/10) +(elemenDMG%10>0)
								objetive.Poison += ElemenDMG
								elemenDMG = 0
								objetive.PoisonTimer += randint(1,3)
								text.append("The Poison Arrow intoxicates the objetive dealing an extra " + str(elemenDMG) +"points of damage for "+str(objetive.PoisonTimer) +"turns!")
							objetive.DragonLife -=elemenDMG    
					SpA +=1
				if Total>0 and Total<19:
					text.append("... The objetive barely shield itself with its wings!\nYour arrows rain over it dealing "+ str(Daños)+" points of damage!")
				elif Total>18:
					text.append("...The rain of bolts hurts the objetive\nfor "+ str(Daños)+" points of damage!!")
				elif Total<1:    
					text.append("... but you failed to do anything!")
				objetive.DragonLife-=Total
		else:
			bearAttack = randint(1, 5)
			if bearAttack<3:
				b = randint (10, 40)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				text.append("Black bear uses Razor Edge!")
				if Result>0 and Result<5:
					text.append("The attack was not efective! Just a scrath for "+ str(Result) + " points of damage")
					objetive.DragonLife -= Result
				if Result>5 and Result<15:
					text.append("The attack lacerates for "+ str(Result) + " points of damage")
					objetive.DragonLife -= Result
				if Result>=15:
					text.append("The attack was really efective! Opens a huge wound for "+ str(Result) + " points of damage!!" )
					objetive.DragonLife -= Result
			elif bearAttack ==3:
				b = randint (1, 40)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				text.append("Black bear uses Bear Hug!")
				if Result>0 and Result<5:
					text.append("The hug was not efective! The objetive gets away with just "+ str(Result) + " points of damage")
					objetive.DragonLife -= Result
				if Result>5 and Result<15:
					text.append("Black bear catches the objetive and makes "+ str(Result) + " points of damage before letting it go!")
					objetive.DragonLife -= Result
				if Result>=15:
					text.append("Bear hug was really efective! the objetive's bones creak for "+ str(Result) + " points of damage and its locked for this turn!!" )
					objetive.Locked = 1                   
					objetive.DragonLife -= Result
			elif bearAttack ==4:
				b = randint (20, 40)
				Result, DamText = Player.Damage(self, b, objetive)
				text.append(DamText)
				text.append("Black bear uses Dark Bite!")
				if Result>0 and Result<5:
					text.append("The bite was not efective! Just a tiny mark on its scales for "+ str(Result) + " points of damage")
					objetive.DragonLife -= Result
				if Result>5 and Result<15:
					text.append("Black bear tastes objetive blood and makes "+ str(Result) + " points of damage!")
					objetive.DragonLife -= Result
				if Result>=15:
					text.append("Dark Bite was really efective! Black Bear tears apart the objetive for "+ str(Result) + " points of damage!" )                
					objetive.DragonLife -= Result
			else:
				text.append("Black bear uses TAUNT!!")
				self.taunt = 1
				text.append("The Dragon is fixed in killing Black bear!")
		for i in text:
			message += i
		if message != None:
			return message
	
	def Defending(self):
		if self.choice == 1:
			message =("Your shield calls for the spirits of your brothers! AEGIS: SHIELD WALL!")
			self.defending = 1
		elif self.choice == 2:
			message =("Nothing is safer that ancient knowledge. DENU'S PROTECTION: MANA SHIELD!")
			self.defending = 2
		else:
			message =("The time seems to slow down in the face of danger. ROGUE ARTS: UNCANNY DODGE!")
			self.defending =3
		return message

	def Damage(self, b, objetive):
		playerDamage = self.attack + b
		DragonDefence = objetive.DragonScales - objetive.DDefBreak

		if playerDamage > self.critical:
			Result = playerDamage - DragonDefence
			DamText = ("\nIT'S A CRITICAL HIT\n")
			if Result<10:
				Result = 10
		elif playerDamage> 0 and playerDamage< self.critical:
			DamText = ("\nThe "+self.name+" attack lands!\n")
			DragonDefence += randint(0, 15)
			Result = playerDamage- DragonDefence
			if Result<1:
				Result = 1
		else:
			Result = 0
			DamText = ("The Attack its too weak!")

		if objetive.DragonFlight == 1 and self.choice != 3:
			DamText = ("\nThe Dragon is high in the sky and "+ self.name +"s attack is inefective!\n")
			Result = 0
		elif objetive.DragonFlight == 1 and (self.choice == 3 or SpearAttack==3):
			DamText = ("\nThe Dragon can't hide from you in the sky!!\n")

		return Result, DamText
	def Defence(self, attack, objetive):
		DefText = ""
		selfDefence = self.defence - self.armorDown + self.SArmor
		if self.defending == 1:
			DefText +=("You meet the "+ attack+" head on with your shield ready!")
			selfDefence += randint(10, 50)
			self.defending = 0
		elif self.defending == 2:
			DefText+=("You wait for the "+ attack+" calmly behind your mana shield")
			selfDefence *=2
			self.defending = 0
		elif self.defending ==3:
			DefText+=("The time runs slow. You bet your life trying to avoid the"+ attack+"!")
			evasion = randint (1, 100)
			if evasion >75: 	
				selfDefence = 999
			self.defending = 0
		elif self.sBomb >0:
			Blind = randint (1, 100)
			if Blind>50:
				DefText+=("The "+ self.name+" hides in the smokescreen!")
				selfDefence = 999
			self.sBomb -=1
		else:
			DefText+=("You try to defend agains the "+ attack)
		return selfDefence, DefText
	def CounterAttack(self, objetive):
		counter = randint(1, 100)
		text = "\n"
		text2 = "\n"
		if self.choice == 1 and counter>90:
			if self.defending==1:
				text += ("... and the spirit of your brothers helps you to counter attack!!")
			else:
				text += ("... and you managed to counter attack!")
			text2 += Player.Attack(self, objetive)
		elif self.choice ==2 and counter>80:
			if self.defending==2:
				text +=("... and you don't lose the chance to attack!")
			else:
				text +=("... and responded with one of you own")
			text2 += Player.Attack(self, objetive)
		elif self.choice ==3 and counter>75:
			if self.name == "Bear":
				text += ("You take the opportunity that Black Bear has given you and attack!")
			elif self.defending==3:
				text += ("... before the time goes back to normal you counterattack!!")
			else:
				text += ("... your hunter instincts won't let this chance go!")
			text2 += Player.Attack(self, objetive)
		else:
			text = ("You failed at counterattacking!")
		text += text2
		return text		
	def Skill(self, objetive):
		if self.choice == 1:
			print("You pray for a miracle!")
			print("Number of miracles remaining: ", self.charge,".")
			miracle = int(input(print("1) Sacred Light\n2) Assistance\n3) Armor\n4) Changed my mind\n What do you pray for?")))
			if miracle ==1:
				self.charge -=1
				sacro= randint (25, 50)
				if self.life>99:
					print("The sacred light covers you! Durandal is energized!\nYour next attack will do ", sacro," points of extra damage!") 
					self.sacro += sacro
				else:
					self.life += sacro
					if self.life>100:
						power = self.life - 100
						healing = sacro - power
						self.life = 100
						self.sacro += power 
						print("You call the sacred light and healed yourself\nfor ", healing," point of life and your next attack will make an extra ", self.sacro," points of sacred damage!!")
					else:
						print("You call he sacred light and healed yourself\nfor, ", sacro," points of life!")
			elif miracle ==2:
				self.charge -=1
				self.guide = randint(2, 5)
				print("The will of god will guide you sword for ", self.guide, " turns! Your critical chance goes up!")
				self.critical -=20
			elif miracle ==3:
				print("God has blessed your armor for", self.SArmorTimer,"turns!")
				self.charge -=1
				self.SArmor += randint(15, 30)
				self.SArmorTimer = randint(2, 5)
			elif miracle ==4:
				self.Turn(self)
			else:
				self.charge -=1
				print("You lost your miracle!")
		elif self.choice ==2:
			print("You call for arcane power!")
			print("Number of spells remaining:", self.charge,".")
			power = int(input(print("1) Fireball\n2) Brick Wall\n3) Swamp Field\n4) Changed my mind\n What do you pray for?")))
			if power ==1:
				fireball = randint (35, 70)
				self.charge -=1
				objetive.DragonLife -= fireball
				print("You summon a powerful fireball, damaging the objetive for ", fireball," points of damage!")
			elif power==2:
				self.charge -=1
				self.cover = 1
				print("You raise a sturdy brick wall in front of you.")
			elif power==3:
				self.charge -=1
				objetive.Swamp = randint(2, 4)
				print("You transform the ground under the objetive into Quicksand for ", objetive.Swamp,"turns")
			elif power==4:
				self.Turn(self)
			else:
				self.charge -=1
				print("You lost your spell!")
		else:
			print("you check your backpack for a tool!")
			print("Number of tools reamaining: ", self.charge,".")
			if self.charge==0:
				print("You are out of tools!")
			tool = int(input(print("1) Magic Flute\n2) Smoke bomb\n3) Special Arrow\n4) Changed my mind\n What do you pray for?")))
			if tool ==1:
				if self.aCompanion ==0:
					self.charge -=1
					print("You call fort a powerful Black bear to aid you in battle")
					self.aCompanion = 1
					bear = Player("Bear", 20, 60, 30, 20, 30, 200, 0, 4)
				else:
					print("Your companion is still alive!")
					self.Skill(self)
			elif tool==2:
				self.charge -=1
				self.sBomb = randint(1, 3)
				print("You throw a smoke bomb at your feets! A dense wall of black smoke hides you from the objetive for ", self.sBomb," turns!")
			elif tool==3:
				self.charge -=1
				self.sArrow = randint(1, 3)
				self.sArrowNumber = randint(1, 7)
				if self.sArrowNumber >1:
					plural = "s!"
				else:
					plural = "!"
				if self.sArrow ==1:
					arrow = "Lighting" #Extra DMG and Stun chance arrow
				elif self.sArrow ==2:
					arrow = "Ice" #Extra DMG and Frozen wings chance arrow
				else:
					arrow = "Poison" #Poison DOT 
				print("From your magic quilver you took ", self.sArrowNumber," ", arrow," arrow", plural)
			elif tool==4:
				self.Turn(self)
			else:
				self.charge -=1
				print("And thats how you lose a tool!")