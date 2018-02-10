from Consts import *

def onUnitBuilt(city, unit):
	iPlayer = city.getOwner()
	if (unit.getUnitType() == iPopulation):
		unit.kill(False, iPlayer)
		city.changePopulation(1)