ws = get_world_size()
def htill_all():
	for px in range(ws):
		for py in range(ws - 1):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			move(North)
		harvest()
		if get_ground_type() == Grounds.Turf:
			till()
		move(East)

def field_init():
	htill_all()
	goto(0, 0)

def seed(entity):
	if num_items(Items.Pumpkin_Seed) == 0:
		trade(Items.Pumpkin_Seed, 2 * (get_world_size() ** 2))

	if get_water() < 0.75:
		use_item(Items.Water_Tank)
	plant(entity)

field_init()