ws = get_world_size()
def seed_sunflowers():
    sfm = [[], [], [], [], [], [], [], [], []]
    # plant
    for px in range(ws):
        for py in range(ws):
            if get_water() < 0.75:
                use_item(Items.Water_Tank)
            if num_items(Items.Sunflower_Seed) == 0:
                trade(Items.Sunflower_Seed, ws**2)
            plant(Entities.Sunflower)
            sfm[15 - measure()] += [[px, py]]
            move(North)
        move(East)
    # harvest
    for sfl in sfm:
        for sf in sfl:
            goto_cord(sf)
            harvest()
goto(0, 0)
seed_sunflowers()