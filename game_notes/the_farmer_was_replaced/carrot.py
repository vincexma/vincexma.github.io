ws = get_world_size()
def seed_carrots():
	for px in range(5):
		for py in range(ws):
			if can_harvest():
				harvest()
			if num_items(Items.Carrot_Seed) == 0:
				trade(Items.Carrot_Seed, get_world_size() ** 2)
			seed(Entities.Carrots)
			move(North)
		move(East)
seed_carrots()
htill_all()