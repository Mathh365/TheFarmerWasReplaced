import crossWorld
import moveTo

def farmDeGrama(solicitado):
	gramaInicial = num_items(Items.Hay)
	clear()
	while (num_items(Items.Hay) - gramaInicial) < solicitado:
		crossWorld.harvestCrossTheWorld()
	clear()
	
def farmDeMadeira(solicitado):
	madeiraInicial = num_items(Items.Wood)
	clear()
	crossWorld.interLeaveFarm(Entities.Tree)
	while (num_items(Items.Wood) - madeiraInicial) < solicitado:
		crossWorld.harvestCrossTheWorld()
	clear()
	
def farmDeCenoura(solicitado):
	custoDaSemente = 4
	cenourasPorSementes = 4
	sementesNecessarias = solicitado / cenourasPorSementes
	materiaisNecessarios = sementesNecessarias * custoDaSemente
	
	if num_items(Items.Wood) < materiaisNecessarios:
		clear()
		while num_items(Items.Wood) < materiaisNecessarios:
			crossWorld.interLeaveFarm(Entities.Tree)
		clear()
		
	if num_items(Items.Hay) < materiaisNecessarios:
		clear()
		while num_items(Items.Hay) < materiaisNecessarios:
			crossWorld.farmCrossTheWorld(Entities.Grass)
		clear()
		
	crossWorld.tillCrossTheWorld()
	moveTo.resetPosition()
	cenouraInicial = num_items(Items.Carrot)
	while (num_items(Items.Carrot) - cenouraInicial) < solicitado:
		crossWorld.farmCrossTheWorld(Entities.Carrot)
	clear()