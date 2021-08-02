def check_mate(self, obs):
    my_head_y, my_head_x = row_col(self.my_head, 11)
    foods = obs.food

    # Must_Check_Mate
    must_check_mate = set()
    for i in self.enemy_idxs:
        enemy_head = obs.geese[i][0]
        enemy_head_y, enemy_head_x = row_col(enemy_head, 11)
        if self.pass_through(enemy_head_y, enemy_head_x, len(obs.geese[i])):
            must_check_mate.add(i)

    for dy, dx in self.dydx:
        nx_y, nx_x = (my_head_y + dy) % 7, (my_head_x + dx) % 11
        if self.still_table[nx_y][nx_x] != -1:
            continue  # WALL
        flag = False
        self.still_table[nx_y][nx_x] = len(obs.geese[self.my_idx])

        # if still_table[ny_y][nx_x] == food: => add one to still_table
        # ADD 1
        nx_cor = self.row_col_to_cor(nx_y, nx_x)
        if nx_cor in foods:
            for e in obs.geese[self.my_idx]:
                e_y, e_x = row_col(e, 11)
                self.still_table[e_y][e_x] += 1

        for i in self.enemy_idxs:
            if i in must_check_mate:
                continue
            enemy_head = obs.geese[i][0]
            enemy_head_y, enemy_head_x = row_col(enemy_head, 11)
            # continue => break
            if self.is_adjacent(nx_y, nx_x, enemy_head_y, enemy_head_x):
                flag = False
                break
            if self.pass_through(enemy_head_y, enemy_head_x, len(obs.geese[i])):
                flag = True

        # REMOVE 1
        if nx_cor in foods:
            for e in obs.geese[self.my_idx]:
                e_y, e_x = row_col(e, 11)
                self.still_table[e_y][e_x] -= 1

        self.still_table[nx_y][nx_x] = -1
        if flag:
            return self.find_direction_array(my_head_y, my_head_x, nx_y, nx_x)

    return []
