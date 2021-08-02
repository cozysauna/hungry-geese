def count_over_check(self, s, i):
    for a in range(4):
        if (s, i, a) not in self.Qsa:
            continue
        if self.Nsa[(s, i, a)] >= 75:
            #                 counts = [self.Nsa[(s, i, a)] if (s, i, a) in self.Nsa else 0 for a in range(4)]
            #                 print(counts)
            self.flag = False
            return True
    return False
