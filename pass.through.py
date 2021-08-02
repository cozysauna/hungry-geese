def pass_through(self, sy, sx, length, adj=False):
    dist = self.generate_table(-1)
    if adj:
        q = deque([(sy, sx, 1)])
    else:
        q = deque([(sy, sx, 0)])
    move_cell_cnt = 0
    while q:
        y, x, cost = q.popleft()
        if dist[y][x] != -1:
            continue
        dist[y][x] = cost
        move_cell_cnt += 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = (y + dy) % 7, (x + dx) % 11
            if self.still_table[ny][nx] == -1:
                q.append((ny, nx, cost+1))
            elif self.still_table[ny][nx] <= cost:
                return False

    if move_cell_cnt >= length:
        return False
    return True
