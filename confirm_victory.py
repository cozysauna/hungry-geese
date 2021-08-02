def confirm_victory(self, obs):
    my_head_y, my_head_x = row_col(self.my_head, 11)
    enemy_idx = self.enemy_idxs[0]
    enemy = obs.geese[enemy_idx]
    enemy_head = enemy[0]
    enemy_length = len(enemy)
    if self.my_length < enemy_length:
        return []
    if len(self.able_direction[enemy_idx]) != 1:
        return []

    dy, dx = self.dydx[self.able_direction[enemy_idx][0]]
    enemy_y, enemy_x = row_col(enemy_head, 11)
    nx_enemy_y = (enemy_y + dy) % 7
    nx_enemy_x = (enemy_x + dx) % 11
    if self.is_adjacent(my_head_y, my_head_x, nx_enemy_y, nx_enemy_x):
        return self.find_direction_array(my_head_y, my_head_x, nx_enemy_y, nx_enemy_x)

    return []
