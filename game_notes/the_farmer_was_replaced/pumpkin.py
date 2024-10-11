ws = get_world_size()
def seed_pumpkins():
    pholes = []
	for px in range(ws):
		for py in range(ws):
            if get_entity_type() == Entities.Pumpkin and not can_harvest():
                pholes.append((px, py))
			elif can_harvest():
				harvest()
			seed(Entities.Pumpkin)
			pholes.append((px, py))
			move(North)
		move(East)
	while len(pholes):
		i = len(pholes) - 1
		for d in range(len(pholes)):
			goto_cord(pholes[i - d])
			if can_harvest():
				pholes.pop(i - d)
			else:
				seed(Entities.Pumpkin)
goto(0, 0)
seed_pumpkins()
harvest()