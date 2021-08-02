def update_direction(self, obs):
    self.able_direction = [[] for _ in range(4)]
    for i in self.enemy_idxs:
        goose = obs.geese[i]
        head = goose[0]
        head_y, head_x = row_col(head, 11)
        for j, (dy, dx) in enumerate(self.dydx):
            ny, nx = (head_y+dy) % 7, (head_x+dx) % 11
            # -1, 0
            if self.still_table[ny][nx] <= 0:
                self.able_direction[i].append(j)

    head_y, head_x = row_col(self.my_head, 11)
    avoid = 10
    if self.last_action != None:
        avoid = self.last_action // 2 * 2 + (self.last_action + 1) % 2
    for j, (dy, dx) in enumerate(self.dydx):
        if avoid == j:
            continue
        ny, nx = (head_y+dy) % 7, (head_x+dx) % 11
        # -1, 0
        if self.still_table[ny][nx] <= 0:
            self.able_direction[self.my_idx].append(j)
