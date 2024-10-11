ws = get_world_size()
def bubble_sort(val, dir=East, opd=West):
	if dir == East:
		goto(0, val)
	else:
		goto(val, 0)

	cacti = []
	for i in range(ws):
		cacti.append(measure())
		move(dir)
	for i in range(len(cacti) - 1):
		min_ind = i
		min_val = cacti[i]
		for j in range(len(cacti) - i):
			ind = i + j
			if cacti[ind] < min_val:
				min_ind = ind
				min_val = cacti[ind]
		if dir == East:
			goto_x(min_ind)
		else:
			goto_y(min_ind)
		for j in range(min_ind, i, -1):
			cacti[j], cacti[j - 1] = cacti[j - 1], cacti[j]
			swap(opd)
			move(opd)

def seed_cacti():
	goto(0, 0)
	trade(Items.Cactus_Seed, ws ** 2)
	for x in range(ws):
		for y in range(ws):
			if can_harvest():
				harvest()
			goto(x, y)
			plant(Entities.Cactus)
	for x in range(ws):
		bubble_sort(x, East, West)
	for y in range(ws):
		bubble_sort(y, North, South)
	harvest()

seed_cacti()