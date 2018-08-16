import random


class Kegs:
    def __init__(self):
        self.kegs_list = [i for i in range(1, 91)]
        self.current_keg = None

    def new_keg(self):
        if len(self.kegs_list) > 0:
            self.current_keg = random.choice(self.kegs_list)
            self.kegs_list.remove(self.current_keg)
            print('Новый бочонок: {} (осталось {})'.format(self.current_keg, len(self.kegs_list)))
