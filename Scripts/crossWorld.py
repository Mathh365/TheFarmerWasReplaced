import try
import moveTo

def tillCrossTheWorld():
	moveTo.resetPosition()
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			till()
			move(North)
		move(East)
		
def plantCrossTheWorld(semente):
	moveTo.resetPosition()
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			try.tryPlant(semente)
			move(North)
		move(East)
		
def harvestCrossTheWorld():
	moveTo.resetPosition()
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			try.tryHarvest()
			move(North)
		move(East)
		
def farmCrossTheWorld(semente):
	if (get_entity_type() != semente) or (get_entity_type() == None):
		plantCrossTheWorld(semente)
		harvestCrossTheWorld()
	else:
		harvestCrossTheWorld()
		
def getWaterCrossTheWorld():
	moveTo.resetPosition()
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			quick_print(get_water())
			move(North)
		move(East)
		

def interLeaveFarm(semente):
	comparador = 0
	isPar = True
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if isPar == True:
				comparador = 0
			else:
				comparador = 1
			if (get_pos_y() % 2 == comparador):
				try.tryPlant(semente)
				try.tryHarvest()
			move(North)
		isPar = not isPar
		move(East)
			