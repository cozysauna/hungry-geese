def middle_cells(self, y, x, yy, xx):
    if y == yy:
        if (x+2) % 11 == xx:
            return (y, (x+1) % 11)
        else:
            return (y, (x-1) % 11)
    else:
        if (y+2) % 7 == yy:
            return ((y+1) % 7, x)
        else:
            return ((y-1) % 7, x)
