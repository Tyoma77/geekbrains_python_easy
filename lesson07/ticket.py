import random


class Ticket:
    def __init__(self):
        self.tmp_list = [i for i in range(1, 91)]
        self.ticket = []
        for i in range(3):
            self.ticket.append([])
            for j in range(5):
                r = random.choice(self.tmp_list)
                self.tmp_list.remove(r)
                self.ticket[i].append(r)
            self.ticket[i] = sorted(self.ticket[i])
            for k in range(4):
                self.ticket[i].insert(random.randint(0, len(self.ticket[i])), ' ')

    def print_ticket(self):
        print('-' * 25)
        for l in range(3):
            for m in range(len(self.ticket[l])):
                print(self.ticket[l][m], end=' ')

            print()
        print('-' * 25)

    def check_keg(self, num):
        if num not in self.ticket:
            raise ValueError

    def replace(self, n):
            for i in range(3):
                for j in range(9):
                    if self.ticket[i][j] == n:
                        self.ticket[i][j] = '-'
                        if self.ticket.count('-') == 15:
                            print('Victory')

    def check_victory(self):
        if self.ticket.count('-') == 15:
            raise IndexError
