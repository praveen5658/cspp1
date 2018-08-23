'''
Author : Praveen
Date : 23-08-2018
'''
def mult_matrix(matrix_1,row_size1,column_size1, matrix_2, row_size2, column_size2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if column_size1 != row_size1:
        print("Error: Matrix shapes invalid for mult")
        return
    final_matrix = []
    for lo_op in range(row_size1):
        li_st = []
        for inner_loop in range(column_size2):
            num_ber = 0
            for in_inner_loop in range(row_size2):
                num_ber += matrix_1[lo_op][in_inner_loop] * matrix_2[in_inner_loop][inner_loop]
            li_st.append(num_ber)
        final_matrix.append(li_st)
    return final_matrix

def add_matrix(matrix_1,row_size1,column_size1, matrix_2, row_size2, column_size2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if row_size1 != row_size2 or column_size1 != column_size2:
        print("Error: Matrix shapes invalid for addition")
        return
    final_matrix = []
    for lo_op in range(row_size1):
        li_st = []
        for inner_loop in range(column_size1):
            li_st.append(matrix_1[lo_op][inner_loop] + matrix_2[lo_op][inner_loop])
        final_matrix.append(li_st)
    return final_matrix

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    first_matrix = []
    first_size = (input()).split(',')
    row_size1 = int(first_size[0])
    column_size1 = int(first_size[1])
    for lo_op in range(row_size1):
        li_st = (input()).split()
        sample_list = []
        for inner_loop in range(column_size1):
            sample_list.append(int(li_st[inner_loop]))
        first_matrix.append(sample_list)
    return first_matrix, row_size1, column_size1

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    (first_matrix, row_size1, column_size1) = read_matrix()
    (second_matrix, row_size2, column_size2) = read_matrix()
    print(add_matrix(first_matrix,row_size1,column_size1, second_matrix, row_size2, column_size2))
    print(mult_matrix(first_matrix,row_size1,column_size1, second_matrix, row_size2, column_size2))

if __name__ == '__main__':
    main()
