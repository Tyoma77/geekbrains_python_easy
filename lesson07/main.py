import lesson07.keg as keg
import lesson07.ticket as ticket


def main():
    print('Сыграем? Д/Н')
    ans = input()
    if ans.lower() == 'д':
        ticket_computer = ticket.Ticket()
        ticket_player = ticket.Ticket()
        kegs = keg.Kegs()
        while len(kegs.kegs_list) > 1:
            kegs.new_keg()
            k = kegs.current_keg

            ticket_player.print_ticket()
            ticket_computer.print_ticket()
            ticket_computer.replace(k)
            #while True:
            #    print('Зачеркнуть бочонок? Д/Н')
             #   na = input()
              #  if na.lower() == 'д':
               #     try:
                #        ticket_player.check_keg(k)
                 #   except ValueError:
                  #      print("Вы прогирали!")
                   #     break
                    #else:
                     #   ticket_player.replace(k)
                      #  break




if __name__ == '__main__':
    main()
