import random

def screen():
    print(f'\n В Ы - {plr_is}')
    print("---------")
    print("  1 2 3")
    print("1", current_field[1], current_field[2], current_field[3], "3")
    print("4", current_field[4], current_field[5], current_field[6], "6")
    print("7", current_field[7], current_field[8], current_field[9], "9")
    print("  7 8 9\n")


def all_8_lines_assign(cur_f):
    a_8_l = [[cur_f[1], cur_f[2], cur_f[3], 1, 2, 3],
             [cur_f[4], cur_f[5], cur_f[6], 4, 5, 6],
             [cur_f[7], cur_f[8], cur_f[9], 7, 8, 9],
             [cur_f[1], cur_f[4], cur_f[7], 1, 4, 7],
             [cur_f[2], cur_f[5], cur_f[8], 2, 5, 8],
             [cur_f[3], cur_f[6], cur_f[9], 3, 6, 9],
             [cur_f[1], cur_f[5], cur_f[9], 1, 5, 9],
             [cur_f[3], cur_f[5], cur_f[7], 3, 5, 7]
      ]
    return a_8_l


def get_1st_turn():
    global YN
    YN = input("Что ж, сыграем в крестики-нолики... начнёте первыми? Y/N ").upper()
    if YN != "Y" and YN != "N":
        get_1st_turn()


def next_turn(t_numb):
    global current_field
    global all_8_lines
    if not check_endgame():
        if t_numb % 2 == 1:
            screen()
            current_field = move(current_field, igrok_is_X)
        else:
            comp_turn()
        all_8_lines = all_8_lines_assign(current_field)


def check_endgame():
    global endgame
    for i in range(len(all_8_lines)):
        if all_8_lines[i][0] == all_8_lines[i][1] == all_8_lines[i][2] != "-":
            if all_8_lines[i][0] == plr_is:
                endgame = "win"
            if all_8_lines[i][0] == comp_is:
                endgame = "loose"
            return endgame
    if "-" not in current_field[1:]:

        endgame = "draw"
        return endgame


def move(cur_f, X):
    move_input = input(f"Ваш ход - введите номер клетки 1-9 \n (легенда - вокруг игрового поля)\n")
    if move_input.isdigit():
        move_input = int(move_input)
        if 1 <= move_input <= 9 and cur_f[int(move_input)] == "-":
            if X:
                cur_f[move_input] = "X"
                return cur_f
            else:
                cur_f[move_input] = "0"
                return cur_f
    print("Некорректно")
    screen()
    move(cur_f, X)
    return cur_f


def comp_turn():
    global current_field
    global get2corners
    if check4win_and_danger(comp_is, plr_is):
        check4win_and_danger(comp_is, plr_is)
#        print("+ проверка на автопродолжение")
        return
    if comp_is == "X" and turn_number == 2:
#        print("ход 2 комп Х?")
        if current_field[2] == "0" or current_field[6] == "0":
            current_field[7] = "X"
            return
        if current_field[4] == "0" or current_field[8] == "0":
            current_field[3] = "X"
            return
        if current_field[1] == "0":
            current_field[9] = "X"
            return
        if current_field[3] == "0":
            current_field[7] = "X"
            return
        if current_field[9] == "0":
            current_field[1] = "X"
            return
        if current_field[7] == "0":
            current_field[3] = "X"
            return
    if comp_is == "X" and empty_corner():
#        print("нашелся угол")
        current_field[empty_corner()] = "X"
        return
    if comp_is == "X" and good_line():
#        print("нашлась строка")
        current_field[good_line()] = "X"
        return


  #  print(f"перед {comp_is} ход {turn_number}")

    while comp_is == "0":
        if turn_number == 2:
            if current_field[5] == "-":
                current_field[5] = "0"
                return
            if current_field[5] == "X":
                current_field[(empty_edge())] = "0"
                get2corners = True
#                print(f" get2corn = {get2corners}")
                return
            else:
                get2corners = False

        if turn_number == 4 and not get2corners:
#            print(f"чек на контру 4 ход без Гет2 {check_empty_counter_edge()}")
            if romb():
                current_field[(romb())] = "0"
 #               print("нашел ромб")
                return
            if current_field[2] == current_field[8] == "X" or current_field[4] == current_field[6] == "X":
                current_field[empty_edge()] = "0"
                return
            if current_field[1] or current_field[3] or current_field[7] or current_field[9] == "X":
#                print("проверели проты?")
                current_field[check_empty_counter_edge()] = "0"
                return



        if turn_number > 2:
            if get2corners:
 #               print(",ход больше 2б будем искать угол")
 #               print(f" get2corn = {get2corners}")
                if turn_number == 6:
                    if any_good_line():
                        current_field[any_good_line()] = "0"
                        return
                    #good_diagonal()
                if empty_edge():
                    current_field[empty_edge()] = "0"
 #                   print(f"край - {empty_edge()}")
                    return
                else:
  #                  print("первый рандом")
                    comp_random()
                    return
            if not get2corners:
                if good_diagonal():
                    current_field[good_diagonal()] = "0"
  #                  print("поставили диагональ")
                    return
                if empty_edge():
                    current_field[(empty_edge())] = "0"
                    return
                else:
  #                  print("второй рандом")
                    comp_random()
                    return
        else:
  #          print("третий рандом")
            comp_random()
            return
#

def empty_corner():
 #   print("ищем угол")
    if current_field[4] == current_field[1] == current_field[2] == "-":
        return 1
    if current_field[2] == current_field[3] == current_field[6] == "-":
        return 3
    if current_field[6] == current_field[9] == current_field[8] == "-":
        return 9
    if current_field[8] == current_field[7] == current_field[4] == "-":
        return 7
    else:
        return False

def romb():
 #   print("ромб ищем")
    if current_field[4] == current_field[2] == "X":
    #    print("ret1")
        return 1
    if current_field[2] == current_field[6] == "X":
     #   print("ret3")
        return 3
    if current_field[6] == current_field[8] == "X":
     #   print("ret9")
        return 9
    if current_field[8] == current_field[4] == "X":
     #   print("ret9")
        return 7
    else:
   #     print("нашел фолт")
        return False

def good_line():
#    print("ищем крест")
    if current_field[2] == current_field[8] == "-" and current_field[5] == comp_is:
 #       print("нашли крест")
        return random.randrange(2,8,6)
    if current_field[4] == current_field[6] == "-" and current_field[5] == comp_is:
  #      print("нашли крест")
        return random.randrange(4,6,2)
    else:
        return False


def any_good_line():
#    print("ищем ЛИНИИ")
    for i in range(8):
        count = 0
        for j in range(3):
            if all_8_lines[i][j] == "0":
                count += 1
            if  all_8_lines[i][j] == "-":
                count += 5
                if count == 11:
  #                  print("нашли ЛИНИЮ")
                    return all_8_lines[i][j+3]


def good_diagonal():
 #   print("ищем диагональ")
    for j in [6, 7]:
        if (comp_is and "-") in all_8_lines[j] and plr_is not in all_8_lines[j]:
            for i in range(3):
                if (all_8_lines[j][i]) == "-":
    #                print("нашли диаг")
                    return all_8_lines[j][i+3]
    if current_field[4] == current_field[6] == "-" and current_field[5] == comp_is:
 #       print("нашли крест")
        return random.randrange(4,6,2)
    else:
        return False


def empty_edge():
    global current_field
    j = [1, 3, 7, 9]
    for i in set(j):
 #       print(f"ищем край - опрос{i}")
    #    print(current_field[i])
        if current_field[i] == "-":
     #       print(f"вернул край {i}")
            return i
    return False




def check_empty_counter_edge():
   # print("ищем контр")
    if current_field[1] == "X":
        if current_field[9] == "-":
            return 9
    if current_field[3] == "X":
        if current_field[7] == "-":
            return 7
    if current_field[7] == "X":
        if current_field[3] == "-":
            return 3
    if current_field[9] == "X":
        if current_field[1] == "-":
            return 1
    else:
        return 2



def comp_random():
  #  print("пошел комп рандом")
    global current_field
    i = 1
    while i < 10:
        if current_field[i] == "-":
            current_field[i] = comp_is
            return
        else:
            i += 1


def check4win_and_danger(chkr, cbck):
    global current_field
    checker, callback = chkr, cbck
    if count_elem(checker):
        current_field[count_elem(checker)] = checker
        return True
    if count_elem(callback):
        current_field[count_elem(callback)] = checker
        return True


def count_elem(checkXorY):
    for i in range(len(all_8_lines)):
        countj = 0
        for j in range(len(all_8_lines[i])):
            if all_8_lines[i][j] == "-":
                countj += 1
        if all_8_lines[i][0] == all_8_lines[i][1] == checkXorY and all_8_lines[i][2] == "-" \
                or all_8_lines[i][1] == all_8_lines[i][2] == checkXorY and all_8_lines[i][0] == "-" \
                or all_8_lines[i][0] == all_8_lines[i][2] == checkXorY and all_8_lines[i][1] == "-":
            for j in range(3):
                if all_8_lines[i][j] == "-":
                    return all_8_lines[i][j + 3]


def final():
    screen()
    if endgame == "win":
        print("WinWinWin... YEAH!")
    if endgame == "loose":
        print(" ПОТРАЧЕНКО\nне твой день")
    if endgame == "draw":
        print("НИЧЬЯ! ПОПРОБУЙ ЕЩЕ РАЗ!")



get2corners = False

get_1st_turn()
igrok_is_X = YN == "Y"

if igrok_is_X:
    plr_is = "X"
    comp_is = "0"
else:
    plr_is = "0"
    comp_is = "X"

current_field = ["-" for i in range(10)]

if not igrok_is_X:
    current_field[5] = "X"

all_8_lines = all_8_lines_assign(current_field)

for turn_number in range(1,11):
    next_turn(turn_number)
final()
