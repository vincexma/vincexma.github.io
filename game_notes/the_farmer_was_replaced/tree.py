ws = get_world_size()
def seed_wood():
	for px in range(ws):
		for py in range(ws):
			if can_harvest():
				harvest()
			if (px + py) % 2:
				seed(Entities.Bush)
			else:
				seed(Entities.Tree)
			move(North)
		move(East)
seed_wood()
htill_all()