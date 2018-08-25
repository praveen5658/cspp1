'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
    Author : Praveen
    Date : 25-08-2018
'''
def first_row(sudoku):
    '''Sub function'''
    li_st1 = []
    li_st2 = []
    li_st3 = []
    for lo_op in range(0, 3):
        for in_loop in range(0, 3):
            li_st1.append(sudoku[lo_op][in_loop])
        for in_loop in range(3, 6):
            li_st2.append(sudoku[lo_op][in_loop])
        for in_loop in range(6, 9):
            li_st3.append(sudoku[lo_op][in_loop])
    if not (is_line(li_st1) and is_line(li_st2) and is_line(li_st3)):
        return False
    return True
def second_row(sudoku):
    '''Sub function'''
    li_st1 = []
    li_st2 = []
    li_st3 = []
    for lo_op in range(3, 6):
        for in_loop in range(0, 3):
            li_st1.append(sudoku[lo_op][in_loop])
        for in_loop in range(3, 6):
            li_st2.append(sudoku[lo_op][in_loop])
        for in_loop in range(6, 9):
            li_st3.append(sudoku[lo_op][in_loop])
    if not (is_line(li_st1) and is_line(li_st2) and is_line(li_st3)):
        return False
    return True
def third_row(sudoku):
    '''Sub function'''
    li_st1 = []
    li_st2 = []
    li_st3 = []
    for lo_op in range(6, 9):
        for in_loop in range(0, 3):
            li_st1.append(sudoku[lo_op][in_loop])
        for in_loop in range(3, 6):
            li_st2.append(sudoku[lo_op][in_loop])
        for in_loop in range(6, 9):
            li_st3.append(sudoku[lo_op][in_loop])
    if not (is_line(li_st1) and is_line(li_st2) and is_line(li_st3)):
        return False
    return True
def is_line(li_st):
    '''Sub function'''
    sample_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    sample_dictionary = {}
    # print(li_st)
    for lo_op in li_st:
        if lo_op in sample_list:
            if lo_op not in sample_dictionary:
                sample_dictionary[lo_op] = 1
            else:
                return False
    # print(set(list((sample_dictionary.keys()))))
    le_n = len(set(sample_dictionary.keys()))
    if le_n == 9:
        return True
    return False
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for lo_op in sudoku:
        boolean = is_line(lo_op)
        if not boolean:
            return False
    for lo_op in range(9):
        if len(sudoku[lo_op]) == 9:
            li_st = []
            for in_loop in range(9):
                li_st.append(str(sudoku[in_loop][lo_op]))
            # print(li_st)
            boolean = is_line(li_st)
            if not boolean:
                return False
    if not first_row(sudoku):
        return False
    if not second_row(sudoku):
        return False
    if not third_row(sudoku):
        return False
    return True
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
        i += 1
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
