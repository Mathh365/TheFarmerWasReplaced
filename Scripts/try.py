def tryWater():
	if get_water() < 0.5:
		while get_water() < 0.75:
			use_item(Items.Water)

def tryPlant(semente):
	if (get_entity_type() != semente) or (get_entity_type() == None):
		tryWater()
		plant(semente)
	
def tryHarvest():
	if can_harvest():
		semente = get_entity_type()
		harvest()
		tryPlant(semente)