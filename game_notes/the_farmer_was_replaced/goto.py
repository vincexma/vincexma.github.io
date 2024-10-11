ws = get_world_size()
def goto_x(x):
	ws = get_world_size()
	px = get_pos_x()
	dl = px + ws - x
	dr = x - px
	if px > x:
		dl = px - x
		dr = ws - px + x
	if dl < dr:
		for i in range(dl):
			move(West)
	else:
		for i in range(dr):
			move(East)
				
def goto_y(y):
	ws = get_world_size()
	py = get_pos_y()
	dd = py + ws - y
	du = y - py
	if py > y:
		dd = py - y
		du = ws - py + y
	if dd < du:
		for i in range(dd):
			move(South)
	else:
		for i in range(du):
			move(North)
				
def goto(x, y):
	goto_x(x)
	goto_y(y)

def goto_cord(cord):
    goto(cord[0], cord[1])

def cord_to_ind(cord):
	return cord[0] * ws + cord[1]
def ind_to_cord(ind):
	return (ind // ws, ind % ws)
	
goto(0,0)