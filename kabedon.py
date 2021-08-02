# Try to kill enemy with WALL
def kabedon(self, obs):
     y, x = row_col(self.my_head, 11)
      adj_enemy = []
       for i in self.enemy_idxs:
            enemy_head = obs.geese[i][0]
            ey, ex = row_col(enemy_head, 11)
            if self.is_adjacent(y, x, ey, ex):
                adj_enemy.append(i)
        if not adj_enemy:
           return []

        for eidx in adj_enemy:
            enemy_head = obs.geese[eidx][0]
            ey, ex = row_col(enemy_head, 11)
            empty_cell = []
            for dy, dx in self.dydx:
                ny, nx = (ey + dy) % 7, (ex + dx) % 11
                if self.still_table[ny][nx] == -1:
                    empty_cell.append((ny, nx))
            if len(empty_cell) != 1:
               continue
            empty_y, empty_x = empty_cell[0]
            # ???????
            opdy, opdx = (ey-y) % 7, (ex-x) % 11
            opy, opx = (ey + opdy) % 7, (ex + opdx) % 11
            if opy == empty_y and opx == empty_x:
                continue

            # ENEMY MUST MOVE THE CERTAIN DIRECTION
            # enemy =>  empty
            # ??????
            dy, dx = (empty_y-ey) % 7, (empty_x-ex) % 11
            # ?
            move = -1
            yy, xx = y, x
            while move < 20:
                move += 1
                yy = (yy + dy) % 7
                xx = (xx + dx) % 11
                ey = (ey + dy) % 7
                ex = (ex + dx) % 11
                # I BUMP
                if not(self.still_table[yy][xx] <= move):
                    break

                # ENEMY MUST BUMP
                if not(self.still_table[ey][ex] <= move):
                  # Check if I can escape
                    if self.still_table[(yy-opdy) % 7][(xx-opdx) %11] <= move+1:
                        return self.find_direction_array(y, x, y+dy, x+dx)

                else:
                    # ENEMY CAN ESCAPE
                    if self.still_table[(ey+opdy) % 7][(ex+opdx) %11] <= move+1:
                        break

        return []
