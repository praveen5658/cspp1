def is_diagnol_forward(main_list, turn):
    cou = 0
    for lo_op in range(3):
        if not main_list[lo_op][lo_op] is turn:
            cou += 1
    if cou == 0:
        return True
    return False
def is_diagnol_backward(main_list, turn):
    cou = 0
    in_loop = 2
    for lo_op in range(3):
        if not main_list[lo_op][in_loop] is turn:
            cou += 1
        in_loop -= 1
    if cou == 0:
        return True
    return False
def is_horizontal(main_list, turn):
    cou = 0
    for lo_op in range(3):
        for in_loop in range(3):
            if not main_list[lo_op][in_loop] is turn:
                cou += 1
        if cou == 0:
            return True
        cou = 0
    return False
def is_vertical(main_list, turn):
    cou = 0
    for lo_op in range(3):
        for in_loop in range(3):
            if not main_list[in_loop][lo_op] is turn:
                cou += 1
        if cou == 0:
            return True
        cou = 0
    return False
def winner(row_one, row_two, row_three, turn):
    game_printing(row_one, row_two, row_three)
    print()
    print("Congratulations user:", turn, " You Won!")
def get_input(turn):
    print()
    print("Turn :",turn)
    print(" Enter the position")
    li_st = input().split()
    return int(li_st[0]), int(li_st[1])
def game_printing(row_one, row_two, row_three):
    print("Game is :")
    print()
    print(' '.join(row_one))
    print(' '.join(row_two))
    print(' '.join(row_three))
    # boolean = is_horizontal(row_one, row_two, row_three)
    # print(boolean)
    # if boolean:
    #     print("Game Over !")
    #     print("Congratulations ",turn," You won!")
    #     return 4, 4
    # else:
        
def main():
    # cou = 0
    # num = 0
    # row_one = ['-','-','-']
    # row_two = ['-','-','-']
    # row_three = ['-','-','-']
    # main_list = [row_one, row_two, row_three]
    # while cou < 9:
    #     if cou % 2 == 0:
    #         turn = 'X'
    #     else:
    #         turn = 'O' 
    #     game_printing(row_one, row_two, row_three)
    #     (row, column) = get_input(turn)
    #     main_list[row][column] = turn
    #     boolean = (is_horizontal(main_list, turn) or is_vertical(main_list, turn) or is_diagnol_forward(main_list, turn) or is_diagnol_backward(main_list, turn))
    #     if boolean:
    #         winner(row_one, row_two, row_three, turn)
    #         num = 1
    #         break
    #     cou += 1
        # game_printing(row_one, row_two, row_three)
        # (row, column) = get_input('O')
        # main_list[row][column] = 'O'
        # print(is_horizontal(main_list, 'O'))
        # print(is_vertical(main_list, 'O'))
        # print(is_diagnol_forward(main_list, 'O'))
        # print(is_diagnol_backward(main_list, 'O'))
    # if num == 0:
    #     print("Game is Tie")
    cou = 0
    x_count = 0
    o_count = 0
    char_count = 0
    other_char = 0
    row_one = input().split()
    row_two = input().split()
    row_three = input().split()
    main_list = [row_one, row_two, row_three]
    for lo_op in range(3):
        for in_loop in range(3):
            if main_list[lo_op][in_loop] == 'x':
                x_count += 1
            elif main_list[lo_op][in_loop] == 'o':
                o_count += 1
            elif main_list[lo_op][in_loop] == '.':
                char_count += 1
            else:
                other_char += 1
    if other_char != 0:
        print("invalid input")
    elif x_count > o_count + 1 or o_count > x_count + 1:
        print("invalid game")
    else:
        turn_x = 'x'
        boolean_x = (is_horizontal(main_list, turn_x) or is_vertical(main_list, turn_x) or is_diagnol_forward(main_list, turn_x) or is_diagnol_backward(main_list, turn_x))
        turn_o = 'o'
        boolean_o = (is_horizontal(main_list, turn_o) or is_vertical(main_list, turn_o) or is_diagnol_forward(main_list, turn_o) or is_diagnol_backward(main_list, turn_o))
        if boolean_x and boolean_o:
            print("invalid game")
            cou += 1
        if boolean_x and cou == 0:
            print(turn_x)
            cou += 1
        if boolean_o and cou == 0:
            print(turn_o)
            cou += 1
        if cou == 0:
            print("draw")
if __name__ == '__main__':
    main()
