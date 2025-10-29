def multiMove(casas, dir):
	for i in range(casas):
		move(dir)
		
def resetPosition():
	multiMove(get_pos_x(), West)
	multiMove(get_pos_y(), South)