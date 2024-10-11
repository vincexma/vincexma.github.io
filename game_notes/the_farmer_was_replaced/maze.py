ws = get_world_size()
def summon_hedge():
	plant(Entities.Bush)
	while not can_harvest():
		do_a_flip()
	while get_entity_type() == Entities.Bush:
		if num_items(Items.Fertilizer) == 0:
			trade(Items.Fertilizer, 10)
		use_item(Items.Fertilizer)

def annoy_treasure():
#	if num_items(Items.Fertilizer) == 0:
#		harvest()
#		return None
	next = measure()
	while(get_entity_type() == Entities.Treasure):
		if num_items(Items.Fertilizer) == 0:
			harvest()
			return None
		use_item(Items.Fertilizer)
	return next

def step(dir):
	if dir == North:
		if move(West):
			return West
		elif move(North):
			return North
		else:
			return East
	if dir == East:
		if move(North):
			return North
		elif move(East):
			return East
		else:
			return South
	if dir == South:
		if move(East):
			return East
		elif move(South):
			return South
		else:
			return West
	if dir == West:
		if move(South):
			return South
		elif move(West):
			return West
		else:
			return North

def find_treasure():
	again = True
	while again != None:
		dir = North
		lim = 300
		while get_entity_type() != Entities.Treasure and lim:
			dir = step(dir)
			lim -= 1
		again = annoy_treasure()

def run_maze():
	summon_hedge()
	find_treasure()
run_maze()
field_init()