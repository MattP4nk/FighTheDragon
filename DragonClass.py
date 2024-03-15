##Dragon Class
from random import randint
import PlayerClass
class Dragon:
	def __init__(self, DragonName, DragonLife, DragonScales, DragonAttack, DragonCrit, DragonBreath):
		self.DragonName = DragonName
		self.DragonLife = DragonLife
		self.DragonScales= DragonScales 
		self.DragonAttack = DragonAttack
		self.DragonCrit = DragonCrit
		self.DragonBreath= DragonBreath
		#From here its only status effects. 
		self.Swamp = 0
		self.Stun = 0
		self.Rage = 0
		self.NoVision = 0
		self.NoBreath = 0
		self.DDefBreak = 0
		self.DDefBreakTimer = 0
		self.DDefUp = 0
		self.DDefUpTimer = 0
		self.DAtkBreak = 0
		self.DAtkBreakTimer = 0
		self.DBleed = 0
		self.SealedMagic = 0
		self.DragonFlight = 0
		self.NoFlight = 0
		self.Locked = 0
		self.Poison = 0
		self.PoisonTimer = 0
		self.FireRain = 0
		self.lesserDragon = []

	def Status(self):
		attack = self.DragonAttack - self.DAtkBreak
		defence = self.DragonScales - self.DDefBreak + self.DDefUp
		status = (self.DragonName +"\nLife: " + str(self.DragonLife) + " Attack: "+ str(attack) +"\nDefence: " + str(defence))
		if self.DragonLife > 0:
			dragon_flag = True
		else:
			dragon_flag = False
		return status, dragon_flag
	def TimerEffects(self):
		if self.FireRain >0:
			self.FireRain -=1
			if self.FireRain <1:
				print("The sky has stopped crying fire!")
		if self.PoisonTimer>0:
			self.PoisonTimer -=1
			print("The Dragon suffers ", self.Poison,"points of damage from bleeding!")
			self.DragonLife -=self.Poison
			if self.PoisonTimer==0:
				print("...and the poison has stopped!")
		if self.DDefBreakTimer >0:
			self.DDefBreakTimer -=1
			if self.DDefBreakTimer ==0:
				print("The Dragon Scales has recovered!")
				self.DDefBreak =0
		if self.DAtkBreakTimer>0:
			self.DAtkBreakTimer-=1
			if self.DAtkBreakTimer ==0:
				print("The Dragon Attack has recovered!")
				self.DAtkBreak = 0
		if self.DDefUpTimer>0:
			self.DDefUpTimer-=1
			if self.DDefUpTimer==0:
				print("The Dragon Scales has turned back to normal")
				self.DDefUp =0
		if self.Swamp >0:
			self.Swamp -=1
			if self.Swamp>0:
				print("The battlefield is still filled with quicksand!")
			else:
				print("The battlefield turned back to its original form!")
		if self.Rage >0:
			self.Rage -=1
			if self.Rage>0:
				print("The Dragon rage is flaring!")
			else:
				print("The Dragon managed to calm itself!")
		if self.NoVision>0:
			self.NoVision-=1
			if self.NoVision>0:
				print("The Dragon eye keeps bleeding!")
			else:
				print("The Dragon eye has healed!")
		if self.DBleed >0:
			Bleed = randint(10, 25)
			self.DBleed -=1
			print("The Dragon suffers ", Bleed,"points of damage from bleeding!")
			self.DragonLife -=Bleed
			if self.DBleed==0:
				print("...and the bleeding has stopped!")
		if self.NoFlight >0:
			self.NoFlight-=1
			if self.NoFlight >0:
				print("The Dragon wings are immobilized!")
			else:
				print("The Dragon has freed its wings!!")
		if self.SealedMagic>0:
			self.SealedMagic-=1
			if self.SealedMagic>0:
				print("The Dragon magics its sealed!")
			else:
				print("The Dragon has recovered its magic!!")
		if self.NoBreath>0:
			self.NoBreath-=1
			if self.NoBreath>0:
				print("Fire and blood keeps gushing out the wound on its throat")
			else:
				print("The wound on its throat has healed!")
		print("*" * 30)

	def Turn(self, objetive):
		TurnAction = 1
		if self.Locked ==1:
			print("The Dragon its locked by Black Bear!!")
			self.Locked = 0
			return None
		if self.Rage>0:
			TurnAction =1
		if TurnAction == 1:#Dragon Attack
			Dragon.Attack(self, objetive)
		elif TurnAction ==2:#Dragon Magic
			Dragon.Magic(self)
		elif TurnAction ==3:#Dragon Flight
			print("3")
		elif TurnAction  ==4:#Dragon Breath
			print("4")
		else:
			print("5")

	def Attack(self, objetive):
		text = []
		message = ""
		text.append(self.DragonName+ " attacks!!")
		dragon_Attack = randint(1, 4)

		if dragon_Attack<=2:
			text.append("\nThe Dragon claw slash at"+ objetive.name+"..")
			b = randint (10, 40)
			Result, DamText = Dragon.Damage(self, b, "Dragon Claw", objetive)
			text.append(DamText)
			if Result==0:
				noDam = Dragon.NoDamage(self, objetive, "Dragon Claw")
				text.append(noDam)
			elif Result>=1 and Result<=5:
				text.append("\nThe attack barely scratches "+ objetive.name+"for"+ str(Result)+" points of damage")
			elif Result>=6 and Result<=15:
				text.append("\n... and lacerates "+ objetive.name +"for"+ str(Result)+" points of damage!")
			elif Result>=16:
				if objetive.name !="Bear":
					objetive.Bleed = randint(1,6)
					text.append("\nThe Dragon Claw rips "+ objetive.name +"flesh for"+ str(Result)+"points of damage. Your blood will fall to the ground for"+ str(objetive.Bleed) +"turns!")
				else:
					text.append("\nThe Dragon Claw rips "+ objetive.name +"flesh for"+ str(Result)+"points of damage.")
				if Result>25 and objetive.name !="Bear":
					text.append("\nThe pain is unbearable. You are stuned!")
					objetive.stun = 1
			objetive.life -= Result

		elif dragon_Attack ==3:
			text.append("\nThe Dragon Tail fall upon "+ objetive.name +" like a hammer!!")
			b = randint (0, 60)
			Result, DamText = Dragon.Damage(self, b, "Dragon Tail", objetive)
			text.append(DamText)
			if Result==0:
				noDam = Dragon.NoDamage(self, objetive, "Dragon Tail")
				text.append(noDam)
			elif Result>=1 and Result<=5:
				text.append("\nThe tail pushes "+ objetive.name +" aside for "+ str(Result)+" points of damage")
			elif Result>=6 and Result<=15:
				text.append("\n... and bruises "+ objetive.name +"for "+ str(Result)+" points of damage!")
			elif Result>=16:
				if objetive.name !="Bear":
					objetive.armorDown += randint (5, 10)
					objetive.aDTimer = randint(1, 3)
					text.append("\nThe Dragon Tail smashes "+ objetive.name +"agains the ground for "+ str(Result)+"points of damage. You armor is reduced by " + str(objetive.armorDown) +" points for "+ str(objetive.aDTimer) +" turns!")
				else:
					text.append("\nThe Dragon Tail smashes "+ objetive.name +"agains the ground for "+ str(Result)+"points of damage.")
				if Result>25 and objetive.name !="Bear":
					text.append("\nThe pain is unbearable. You are stuned!")
					objetive.stun = 1
			objetive.life -= Result

		elif dragon_Attack ==4:
			text.append("\nThe self launches with its jaws ready to devour the "+ objetive.name +"...")
			b = randint (-20, 80)
			Result, DamText = Dragon.Damage(self, b, "Dragon Maw", objetive)
			text.append(DamText)
			if Result ==0:
				noDam = Dragon.NoDamage(self, objetive, "Dragon Maw")
				text.append(noDam)
			elif Result>0 and Result<6:
				text.append("\n... and barely hits "+ objetive.name +" for "+ str(Result)+" points of damage")
			elif Result>5 and Result<16:
				text.append("\n... and takes a good bite from "+ objetive.name +" for "+ str(Result)+" points of damage!!")
			elif Result>15:
				if objetive.name !="Bear":
					objetive.maim += randint (5, 10)
					objetive.maimTimer += randint(1, 3)
					text.append("\n... And tears "+ objetive.name +" flesh for "+ str(Result)+" points of damage. Reducing your attack for "+ str(objetive.maim) +" points for "+ str(objetive.maimTimer) +" turns!")
				else:
					text.append("\n... And tears "+ objetive.name +" flesh for "+ str(Result)+" points of damage.")
				if Result>25 and objetive.name !="Bear":
					text.append("\nThe pain is unbearable. You are stuned!")
					objetive.stun = 1
			objetive.life -= Result
		for i in text:
			message += i
		if message != "":
			return message

	def NoDamage(self, objetive, attack): #This is just some prints in case the dragon does no damage.
		text = "\n"
		if objetive.defending==1:
			text+=("...the "+ attack+" coundnt scratch your Aegis")
		elif objetive.defending==2:
			text+=("\n... but even so the "+ attack+" can`t pass your mana shield")
		elif objetive.defending==3:
			text+=("\n... the Dragon loses sight of you and the "+ attack+" misses!!")
		else:
			text+=("\n... the "+ attack+" misses!!")
		text2 = PlayerClass.Player.CounterAttack(objetive, self)
		text += text2
		return text

	def Damage(self, b, attack, objetive): #Dragon Damage Calculations
		DamText = "\n"
		DragonAttack = self.DragonAttack + b
		if self.DragonFlight==1:
			DamText = ("The Dragon attacks "+ objetive.name +" from the skies, aims for"+ objetive.name +" and dives at fullspeed!!!")
			DragonAttack *= 2
			self.DragonFlight = 0
		if objetive.cover == 1 and objetive.name !="Bear":
			DamText =("\nYou shield yourself from all damage behind your wall. But the wall falls apart!")
			objetive.cover = 0
			DragonDamage = 0
		if self.Swamp>0 and self.DragonFlight == 0:
			DamText = ("\nThe Quicksand hinders its attack!")
			DragonAttack *=0.75
		if self.NoVision> 0:
			Blind = randint (1, 100)
			if Blind>50:
				DamText += ("\nThe"+ objetive.name +"hides in the Dragon blindspot!")
				DragonAttack = 0
		if self.Rage>0:
			DragonAttack *= 1.25
		objetiveDefence, DefText = PlayerClass.Player.Defence(objetive, attack, objetive.name)
		DamText += DefText
		DragonDamage = DragonAttack - objetiveDefence
		if DragonDamage>0:
			if DragonDamage > self.DragonCrit:
				DamText += ("\nThe "+ attack +" HITS AT MAXIMUM POWER")
				Result = DragonDamage * 1.25
			else:
				DamText += ("\nThe "+ attack +" hits")
				Result = DragonDamage
		else:
			DamText = ""
			Result = 0
		return Result, DamText

	def Magic(self):
		MagicChoice = randint (1, 3)
		#Fire Rain
		if MagicChoice == 1:
			self.FireRain = randint (2, 6)
			print("Las lagrimas de mis hermanos caidos bañaran esta tierra!")
			print("La lluvia de fuego castigara el terreno por ", self.FireRain," Turnos!!")
		#Call to the Void
		if MagicChoice == 2:
			print("Rise my brothers! From the shadows you shall rise!")
			print("A small dragon from the void raises from the shadows!")
			Dragon.NewDragon(self)
		#Song of the dragons
		if MagicChoice == 3:
			if len(self.lesserDragon) > 0:
				dCounter = 0
				print("The dragons joined their voices in song!")
				print("The", self.DragonName,"plays the song of the kingdom")
				for i in self.lesserDragon:
					i.DragonAttack *= 1.25
					i.DragonScales *= 1.25
					i.DragonLife *= 1.25
					dCounter += 1
					if dCounter == 1:
						print(i.DragonName,"the little dragon sings the song of fire!")
						print("The fire dances to the beat of the song and burns")



		#Song of Ilussions
	def Fligh(self):
		print("was")

	def NewDragon(self):
		i = len(self.lesserDragon) +1 #"+1" just to not have "Dragon Minnion 0"
		self.lesserDragon.append(Dragon("Dragon Minnion "+str(i), 100, 10, 10, 10, 20))
		
