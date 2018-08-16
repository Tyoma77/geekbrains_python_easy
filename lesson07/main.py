import lesson07.keg as keg
import lesson07.ticket as ticket


import keg as keg
import ticket as ticket


def main():

    ticket_computer = ticket.Ticket('ai')
    ticket_player = ticket.Ticket(str(input('Введите имя \n')))
    kegs = keg.Kegs()
    lose = 0
    while True:
        kegs.new_keg()
        k = kegs.current_keg
        ticket_player.print_ticket()
        ticket_computer.print_ticket()
        
        k in ticket_computer
        if ticket_computer.check_victory():
            break
            
        while True:
            an = input('Зачеркнуть бочонок? д/н')
            if an.lower() == 'д':
                if k in ticket_player:
                    break
                else:
                    lose = 1
                    break
            elif an.lower() == 'н':
                if k in ticket_player:
                    lose = 1
                    break
                else:
                    break
            else:
                print('Введено неверное значение')
        
        if lose == 1:
            print('Вы проиграли')
            break
        
        if ticket_player.check_victory():
            break


if __name__ == '__main__':
    main()
