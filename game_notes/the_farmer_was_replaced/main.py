ws = get_world_size()
def stock_inventory(amt=100000):
	if num_items(Items.Power) < amt:
		seed_sunflowers()
	elif num_items(Items.Hay) < amt:
		seed_hay()
	elif num_items(Items.Wood) < amt:
		seed_wood()
	elif num_items(Items.Carrot) < amt:
		seed_carrots()
	elif num_items(Items.Pumpkin) < amt:
		seed_pumpkins()
	elif num_items(Items.Gold) < 40000:
		run_maze()
		field_init()
	elif num_items(Items.Cactus) < 5000:
		seed_cacti()
	else:
		return False
	return True

field_init()
while stock_inventory():
	goto(0, 0)
field_init()
