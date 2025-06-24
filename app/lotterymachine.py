import os
import random

def tiledraw():
    # Return 8 random unique tiles
    all_tiles = [tile for tile in os.listdir("static/tiledraw") if tile.endswith(".svg")]
    selected = random.sample(all_tiles, 8)
    return sorted(selected)

def show_tiledraw_options():
    all_tiles = [tile for tile in os.listdir("static/tiledraw") if tile.endswith(".svg")]
    return sorted(all_tiles)  