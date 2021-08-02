# avoid dying without getting any food
def starving(self, obs):
    if not(30 <= self.turn <= 39):
        return []
    y, x = row_col(self.my_head, 11)
    if len(self.me) == 1:
        for food in obs.food:
            food_y, food_x = row_col(food, 11)
            if self.is_adjacent(y, x, food_y, food_x):
                return self.find_direction_array(y,  x, food_y, food_x)
    return []
