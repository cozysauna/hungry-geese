def find_direction_array(self, y, x, yy, xx):  # y =>yy, x => xx
    # [NORTH, SOUTH, WEST, EAST]
    if (y-1) % 7 == yy:
        return [1, 0, 0, 0]
    if (y+1) % 7 == yy:
        return [0, 1, 0, 0]
    if (x-1) % 11 == xx:
        return [0, 0, 1, 0]
    if (x+1) % 11 == xx:
        return [0, 0, 0, 1]
